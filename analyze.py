import os
import json
import time
import base64
import hashlib
import urllib.request
import urllib.error
import ssl

# Konfigurasi
IMAGE_DIR = "pict Moodboard wisuda"
METADATA_FILE = "metadata.json"
MODEL_NAME = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

# Delay untuk mematuhi limit 12 RPM (Request Per Minute) -> jeda ~8 detik per request
REQUEST_DELAY = 8.0

def get_api_key():
    # Mengambil API key dari environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Mencoba membaca dari file .env jika ada
        if os.path.exists(".env"):
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("GEMINI_API_KEY="):
                        api_key = line.split("=")[1].strip()
                        break
    return api_key

def calculate_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def get_mime_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg']:
        return 'image/jpeg'
    elif ext == '.png':
        return 'image/png'
    elif ext == '.webp':
        return 'image/webp'
    return 'application/octet-stream'

def call_gemini_api(payload, api_key):
    url = f"{API_URL}?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    # Menghindari masalah sertifikat SSL pada beberapa sistem
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    # Retry logic dengan Exponential Backoff
    max_retries = 5
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                res_body = response.read().decode('utf-8')
                return json.loads(res_body)
        except urllib.error.HTTPError as e:
            # Handle rate limit (429) atau server error (503/500)
            if e.code in [429, 500, 503]:
                if e.code == 429:
                    wait_time = 30 * (attempt + 1)
                    print(f"[Warning] Rate Limit Terlampaui (429). Menunggu {wait_time} detik agar kuota kembali terisi (Percobaan {attempt + 1}/{max_retries})...")
                else:
                    wait_time = 2 ** (attempt + 1)
                    print(f"[Warning] HTTP Error {e.code}. Mengulang dalam {wait_time} detik (Percobaan {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
            else:
                print(f"[Error] HTTP Error {e.code}: {e.read().decode('utf-8')}")
                raise e
        except Exception as e:
            wait_time = 2 ** (attempt + 1)
            print(f"[Warning] Error koneksi: {e}. Mengulang dalam {wait_time} detik (Percobaan {attempt + 1}/{max_retries})...")
            time.sleep(wait_time)
            
    raise Exception("Gagal menghubungi API setelah beberapa kali percobaan.")

def analyze_single_image(filepath, api_key):
    mime_type = get_mime_type(filepath)
    with open(filepath, "rb") as image_file:
        img_b64 = base64.b64encode(image_file.read()).decode('utf-8')
        
    prompt = """Anda adalah seorang kurator seni editorial, sutradara film indie, dan penutur cerita. 
Misi Anda adalah menganalisis gambar ini dari sudut pandang estetika naratif, atmosfer, memori, emosi, dan rasa sensorik. 
Hindari deskripsi datar yang hanya menyebutkan objek di gambar secara harfiah. 
Fokuslah pada makna mendalam, suasana, dan rasa nostalgia.

Berikan respons dalam format JSON murni dengan struktur persis seperti berikut (jangan tambahkan markdown codeblock ```json):
{
  "title": "Judul puitis dan sinematik pendek dalam bahasa Indonesia (bukan nama file/deskripsi harfiah)",
  "description": "Penjelasan atmosferis, emosional, dan naratif seperti potongan adegan film coming-of-age dalam bahasa Indonesia (1-2 kalimat)",
  "tone": "Nuansa emosional (misal: Nostalgia Hangat, Kesepian Sunyi, Harapan Manis, Perpisahan Syahdu)",
  "dominant_colors": ["3 kode warna HEX dominan yang paling mewakili palet gambar ini, contoh: #HEX1"],
  "aesthetic_tags": ["3-5 tag estetika dalam bahasa Inggris/Indonesia, contoh: cinematic, grainy, vintage"],
  "sensory_details": {
    "visual_description": "Deskripsi visual detail dari apa yang sebenarnya terlihat pada gambar dalam bahasa Indonesia",
    "implied_sound": "Suara atau musik apa yang seolah-olah terdengar dari adegan ini? (1 frasa singkat)",
    "implied_season": "Musim, cuaca, atau waktu yang tersirat dari gambar ini (1 frasa singkat)"
  },
  "story_prompt": "Satu kalimat pemantik cerita kreatif yang diinspirasikan oleh gambar ini dalam bahasa Indonesia"
}"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inlineData": {
                            "mimeType": mime_type,
                            "data": img_b64
                        }
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    response_data = call_gemini_api(payload, api_key)
    
    # Parsing output teks dari response Gemini
    try:
        text_content = response_data['candidates'][0]['content']['parts'][0]['text']
        # Bersihkan jika Gemini menyertakan ```json ... ```
        text_content = text_content.strip()
        if text_content.startswith("```json"):
            text_content = text_content[7:]
        if text_content.endswith("```"):
            text_content = text_content[:-3]
        text_content = text_content.strip()
        
        parsed_json = json.loads(text_content)
        return parsed_json
    except Exception as e:
        print(f"[Error] Gagal memproses JSON dari API untuk {os.path.basename(filepath)}: {e}")
        # Kembalikan struktur default jika gagal
        return {
            "title": os.path.basename(filepath),
            "description": "Gagal menganalisis gambar ini secara otomatis.",
            "tone": "Netral",
            "dominant_colors": ["#808080"],
            "aesthetic_tags": ["error"],
            "sensory_details": {
                "visual_description": "Tidak tersedia",
                "implied_sound": "Tidak tersedia",
                "implied_season": "Tidak tersedia"
            },
            "story_prompt": "Tuliskan cerita Anda sendiri tentang gambar ini."
        }

def run_clustering_and_macro_analysis(compiled_descriptions, api_key):
    print("\n--- Memulai Tahap 2: Analisis Makro & Pengelompokan Kategori ---")
    
    prompt = f"""Anda adalah kepala kurator pameran seni visual kontemporer. 
Anda memiliki daftar data deskripsi dari kumpulan gambar moodboard bertema kelulusan/wisuda/akhir masa kuliah.
Tugas Anda adalah membaca seluruh ringkasan deskripsi gambar di bawah ini, menemukan benang merah emosional yang menyatukan mereka, lalu menghasilkan:
1. collection_theme: Tema besar yang menyatukan seluruh koleksi.
2. collection_summary: Ringkasan kuratorial tentang keseluruhan suasana dan isi moodboard.
3. collection_story: Narasi puitis yang menghubungkan gambar-gambar tersebut sebagai satu cerita perjalanan.
4. categories: 5 sampai 8 kategori puitis yang bernilai seni (exhibition themes) untuk mengelompokkan gambar-gambar ini. Berikan id, name (nama puitis), dan description kuratorial untuk setiap kategori.
5. image_mappings: Memetakan setiap ID gambar ke salah satu id kategori yang Anda buat.

Berikut adalah kompilasi deskripsi gambar:
{json.dumps(compiled_descriptions, indent=2)}

Berikan respons dalam format JSON murni dengan struktur persis seperti berikut (jangan tambahkan markdown codeblock ```json):
{{
  "collection_theme": "Tema besar koleksi (Bahasa Indonesia)",
  "collection_summary": "Ringkasan kuratorial keseluruhan (Bahasa Indonesia)",
  "collection_story": "Narasi puitis penghubung cerita (Bahasa Indonesia)",
  "categories": [
    {{
      "id": "slug-kategori-1",
      "name": "Nama Kategori Puitis",
      "description": "Deskripsi kuratorial kategori"
    }}
  ],
  "image_mappings": {{
    "gambar_id_1": "slug-kategori-x",
    "gambar_id_2": "slug-kategori-y"
  }}
}}"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    response_data = call_gemini_api(payload, api_key)
    
    try:
        text_content = response_data['candidates'][0]['content']['parts'][0]['text']
        text_content = text_content.strip()
        if text_content.startswith("```json"):
            text_content = text_content[7:]
        if text_content.endswith("```"):
            text_content = text_content[:-3]
        text_content = text_content.strip()
        
        parsed_json = json.loads(text_content)
        return parsed_json
    except Exception as e:
        print(f"[Error] Gagal memproses JSON Analisis Makro: {e}")
        # Fallback default
        return {
            "collection_theme": "Kenangan Masa Kuliah",
            "collection_summary": "Koleksi gambar curahan emosi seputar kelulusan dan persahabatan.",
            "collection_story": "Kisah tentang perjalanan yang diakhiri dengan perpisahan hangat.",
            "categories": [
                {
                    "id": "uncategorized",
                    "name": "Lensa Kenangan",
                    "description": "Momen-momen yang terekam secara acak sepanjang perjalanan."
                }
            ],
            "image_mappings": {}
        }

def main():
    api_key = get_api_key()
    if not api_key:
        print("[Error] GEMINI_API_KEY tidak ditemukan di environment variable maupun file .env!")
        print("Silakan buat file .env dengan isi: GEMINI_API_KEY=your_actual_key")
        return
        
    if not os.path.exists(IMAGE_DIR):
        print(f"[Error] Folder gambar '{IMAGE_DIR}' tidak ditemukan!")
        return

    # Memuat cache metadata yang sudah ada
    existing_data = {}
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except Exception as e:
            print(f"[Warning] Gagal membaca metadata.json yang sudah ada: {e}. Membuat dari awal.")

    images_cache = {}
    # Kita salin gambar yang sudah berhasil diproses sebelumnya dari format lama/baru
    if "images" in existing_data and isinstance(existing_data["images"], list):
        for img in existing_data["images"]:
            images_cache[img["filename"]] = img

    # Cari file gambar di direktori
    all_files = os.listdir(IMAGE_DIR)
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    image_files = [f for f in all_files if f.lower().endswith(image_extensions)]
    
    print(f"Menemukan {len(image_files)} file gambar di folder '{IMAGE_DIR}'.")
    
    processed_images = []
    has_changes = False

    # TAHAP 1: Analisis Gambar Individual
    for idx, filename in enumerate(image_files):
        filepath = os.path.join(IMAGE_DIR, filename)
        file_hash = calculate_md5(filepath)
        
        # Cek apakah gambar sudah ada di cache
        cached_img = images_cache.get(filename)
        if cached_img and cached_img.get("id") == file_hash:
            print(f"[{idx+1}/{len(image_files)}] Skip {filename} (Menggunakan cache...)")
            processed_images.append(cached_img)
        else:
            print(f"[{idx+1}/{len(image_files)}] Menganalisis {filename} dengan Gemini Vision...")
            # Panggil API
            analysis = analyze_single_image(filepath, api_key)
            
            # Tambahkan field id & filename ke hasil analisis
            analysis["id"] = file_hash
            analysis["filename"] = filename
            
            processed_images.append(analysis)
            has_changes = True
            
            # Tulis ke file sementara agar progres tidak hilang jika terhenti
            temp_output = {"images": processed_images}
            with open(METADATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(temp_output, f, ensure_ascii=False, indent=2)
                
            # Jeda waktu (delay) untuk mematuhi rate limit API
            time.sleep(REQUEST_DELAY)

    # TAHAP 2: Analisis Makro & Pengelompokan Kategori
    # Kita lakukan analisis makro jika ada perubahan gambar atau jika analisis makro sebelumnya belum ada
    needs_macro = has_changes or "collection_theme" not in existing_data or not existing_data.get("categories")
    
    if needs_macro and len(processed_images) > 0:
        # Buat deskripsi terkompilasi yang ringkas untuk dikirim ke Gemini
        compiled_desc = []
        for img in processed_images:
            compiled_desc.append({
                "id": img["id"],
                "title": img["title"],
                "description": img["description"],
                "tone": img["tone"],
                "aesthetic_tags": img["aesthetic_tags"]
            })
            
        macro_result = run_clustering_and_macro_analysis(compiled_desc, api_key)
        
        # Petakan kembali kategori ke gambar masing-back
        mappings = macro_result.get("image_mappings", {})
        
        # Update kategori untuk setiap gambar
        for img in processed_images:
            img_id = img["id"]
            img["category_id"] = mappings.get(img_id, "uncategorized")
            
        # Bentuk data final
        final_data = {
            "collection_theme": macro_result.get("collection_theme", ""),
            "collection_summary": macro_result.get("collection_summary", ""),
            "collection_story": macro_result.get("collection_story", ""),
            "categories": macro_result.get("categories", []),
            "images": processed_images
        }
        
        with open(METADATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(final_data, f, ensure_ascii=False, indent=2)
            
        print("\n[Success] Analisis makro selesai dan metadata.json berhasil dibuat!")
    else:
        # Jika tidak ada perubahan gambar dan analisis makro sudah ada, pertahankan data lama
        if not needs_macro:
            print("\n[Info] Tidak ada perubahan gambar dan analisis makro sudah ada. Caching penuh aktif.")
        else:
            print("\n[Warning] Tidak ada gambar yang bisa dianalisis.")

if __name__ == "__main__":
    main()
