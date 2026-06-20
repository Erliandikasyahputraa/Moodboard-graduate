import json
import os

MAPPING_FILE = "docs/sheet_mapping.json"
METADATA_FILE = "metadata.json"

def get_photography_details(title, category_id, content_labels, technique_labels, dominant_colors, index):
    tech = technique_labels[0] if technique_labels else "Film"
    content = content_labels[0] if content_labels else "Solo"
    
    grading_styles = {
        "Sunset": f"Grading hangat (warm/golden tone) dengan dominasi temperatur tinggi (K 5500-6000), saturasi jingga/emas yang pekat pada highlight, serta shadow lembut kecokelatan ({', '.join(dominant_colors[:2])}).",
        "Dark": f"Low-key grading dengan bayangan pekat (deep shadows), saturasi warna ditekan (desaturated), tone dingin kebiruan/kehijauan pada area shadow ({', '.join(dominant_colors[:2])}) untuk nuansa sinematik melankolis.",
        "Film": f"Grading vintage ala film analog 35mm. Fade matte pada warna hitam (faded shadows), grain halus, tone warna agak kehijauan/teal ({', '.join(dominant_colors[:2])}), serta highlight yang digulung lembut (soft roll-off).",
        "Blur": f"Grading warna alami/soft dengan kontras rendah. Penekanan pada transisi warna dinamis ({', '.join(dominant_colors[:2])}) untuk mendukung efek gerak (motion blur) tanpa distorsi saturasi.",
        "Flash": f"High contrast grading dengan direct flash lighting. Warna kulit natural namun tersaturasi kuat, bayangan tajam di belakang subjek, warna latar belakang diredupkan untuk fokus subjek ({', '.join(dominant_colors[:2])})."
    }
    color_grading = grading_styles.get(tech, f"Grading warna natural terkurasi dengan penyesuaian kontras menengah, menekankan palet warna {', '.join(dominant_colors)}.")

    if content == "Objek":
        technique_and_angle = "Top-Down (Flat Lay) atau Extreme Close-Up (ECU) menggunakan lensa makro 90mm f/2.8."
    elif content == "Pasangan":
        technique_and_angle = "Eye Level, Medium Close-Up (MCU) dengan kedalaman ruang sempit (shallow depth of field) untuk efek intim."
    elif content == "Keluarga":
        technique_and_angle = "Low Angle, Wide Shot (WS) atau Full Shot (FS) untuk merangkul kebersamaan dengan kesan formal dan kokoh."
    elif content == "Teman":
        if tech == "Blur":
            technique_and_angle = "Dutch Angle (Miring) atau Eye Level Action Shot untuk menangkap keseruan pose gerak dinamis secara candid."
        else:
            technique_and_angle = "Eye Level, Wide Shot (WS) sejajar mata untuk memastikan ketajaman fokus yang merata pada seluruh anggota grup."
    else:  # Solo
        if tech == "Sunset":
            technique_and_angle = "Low Angle, Backlit Medium Shot untuk menciptakan efek rim light (garis cahaya) emas di bahu dan rambut subjek."
        elif tech == "Dark":
            technique_and_angle = "High Angle atau Eye Level Close-Up dengan low-key lighting untuk ekspresi kontemplatif yang dramatis."
        else:
            technique_and_angle = "Eye Level, Medium Shot (MS) sejajar mata untuk menciptakan perspektif potret personal yang ramah."

    if tech == "Sunset":
        suggested_settings = "Lensa 85mm f/1.8 | Aperture: f/2.0 | Shutter: 1/250s | ISO: 100 (memaksimalkan ambient sore hari)"
    elif tech == "Dark":
        suggested_settings = "Lensa 50mm f/1.4 | Aperture: f/1.8 | Shutter: 1/125s | ISO: 800-1600 (low light sensitivity)"
    elif tech == "Film":
        suggested_settings = "Lensa 35mm f/2.0 | Aperture: f/2.8 | Shutter: 1/160s | ISO: 400 (karakter grain film yang optimal)"
    elif tech == "Blur":
        suggested_settings = "Lensa 24-70mm f/2.8 | Aperture: f/5.6 | Shutter: 1/15s - 1/30s (untuk handheld motion blur) | ISO: 100"
    elif tech == "Flash":
        suggested_settings = "Lensa 35mm f/1.8 | Aperture: f/4.0 | Shutter: 1/160s (flash sync) | Eksternal Flash 1/16 power | ISO: 200"
    else:
        suggested_settings = "Lensa 50mm f/1.8 | Aperture: f/2.5 | Shutter: 1/125s | ISO: 200"

    return {
        "color_grading": color_grading,
        "technique_and_angle": technique_and_angle,
        "suggested_settings": suggested_settings
    }

def main():
    if not os.path.exists(MAPPING_FILE):
        print(f"[Error] {MAPPING_FILE} tidak ditemukan. Silakan jalankan create_contact_sheets.py terlebih dahulu.")
        return
        
    with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        
    categories = [
        {
            "id": "bittersweet-farewell",
            "name": "Bittersweet Farewell",
            "description": "Momen-momen perpisahan yang manis namun menyedihkan di sudut-sudut kampus."
        },
        {
            "id": "found-family",
            "name": "Found Family",
            "description": "Keluarga yang kita temukan sepanjang perjuangan akademis."
        },
        {
            "id": "daily-struggle",
            "name": "Daily Struggle & Memes",
            "description": "Tawa, lelah, dan air mata di balik tumpukan skripsi."
        },
        {
            "id": "into-the-unknown",
            "name": "Into the Unknown",
            "description": "Langkah kaki menembus ufuk barat menuju masa depan yang baru."
        },
        {
            "id": "silent-reflection",
            "name": "Silent Reflection",
            "description": "Keheningan koridor dan ruang kelas kosong yang menyimpan kenangan."
        }
    ]

    # Specific metadata tag definitions for all 93 images
    details = {
        1: {
            "title": "Tatapan dari Kehampaan",
            "description": "Di dasar jurang sunyi, delapan siluet pria berjas membisu mengelilingi tepian, tatapan mereka seperti jangkar yang menarik jiwa ke kedalaman.",
            "category_id": "daily-struggle",
            "tone": "Kekosongan Abadi",
            "dominant_colors": ["#0A0A0A", "#F2F0E6", "#4A4A4A"],
            "aesthetic_tags": ["Monokromatik", "Existential", "Sinematik"],
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Siluet delapan pria berjas mengelilingi lubang dari atas.",
                "implied_sound": "Hening yang memekakkan",
                "implied_season": "Senja membeku"
            },
            "story_prompt": "Saat tatapan itu mengunci jiwanya, ia tahu ia harus menyerah."
        },
        2: {
            "title": "Detik Sebelum Janji di Bawah Naungan",
            "description": "Dalam keheningan taman yang rimbun, sepasang mata menanti sebuah jawaban, sementara siluet janji menyelimuti harapan.",
            "category_id": "silent-reflection",
            "tone": "Antisipasi Manis",
            "dominant_colors": ["#3E543B", "#E8D3C8", "#2C2C2C"],
            "aesthetic_tags": ["cinematic", "soft focus", "nature"],
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Wajah perempuan kabur di depan, pria berjas di kejauhan.",
                "implied_sound": "Kicau burung samar",
                "implied_season": "Awal musim panas"
            },
            "story_prompt": "Siapakah yang menunggu di antara pepohonan yang sunyi?"
        },
        3: {
            "title": "Lensa Merah Formal",
            "description": "Pas foto berlatar belakang merah menyala yang membekukan wajah tegang seorang mahasiswa, syarat mutlak sebuah kelulusan.",
            "category_id": "daily-struggle",
            "tone": "Formal & Tegang",
            "dominant_colors": ["#FF0000", "#000000", "#FFFFFF"],
            "aesthetic_tags": ["pasfoto", "indonesia", "formal"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Pas foto formal berlatar merah, mengenakan peci hitam dan jas.",
                "implied_sound": "Suara jepretan kamera studio tua",
                "implied_season": "Siang hari yang terik"
            },
            "story_prompt": "Di balik tatapan datar ini, ada ribuan malam tanpa tidur demi gelar sarjana."
        },
        4: {
            "title": "Aku UIN",
            "description": "Sebuah meme humor mahasiswa dengan latar gerbang kampus UIN Alauddin Makassar, merayakan identitas dengan tawa jenaka.",
            "category_id": "daily-struggle",
            "tone": "Jenaka & Satir",
            "dominant_colors": ["#00FF00", "#D3D3D3", "#8B4513"],
            "aesthetic_tags": ["meme", "uin", "humor"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Suntingan foto pria berjaket hijau digambar tangan menunjuk gerbang UIN.",
                "implied_sound": "Lagu TikTok viral yang berisik",
                "implied_season": "Musim kuliah"
            },
            "story_prompt": "Berapa banyak mahasiswa yang tertawa melihat gerbang ini setiap paginya?"
        },
        5: {
            "title": "Tragedi Skripsi Patrick",
            "description": "Penggambaran kondisi fisik dan mental yang hancur setelah begadang mengerjakan revisi skripsi tak berujung.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Jenaka",
            "dominant_colors": ["#E5E5E5", "#FF69B4", "#808080"],
            "aesthetic_tags": ["cartoon", "meme", "stress"],
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Patrick Star memegang pedang di samping Squidward yang terbungkus perban di kursi roda.",
                "implied_sound": "Musik dramatis kartun",
                "implied_season": "Musim revisi akhir"
            },
            "story_prompt": "Ketika dosen pembimbing berkata 'tolong revisi bab 4 lagi'."
        },
        6: {
            "title": "Dokumenter Kelulusan",
            "description": "Potret candid hitam putih yang menangkap kehangatan wisudawan saling merapikan atribut toga di tengah keramaian.",
            "category_id": "bittersweet-farewell",
            "tone": "Hangat & Dokumenter",
            "dominant_colors": ["#111111", "#FFFFFF", "#808080"],
            "aesthetic_tags": ["black-and-white", "candid", "friendship"],
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Foto monokrom wisudawan merapikan topi toga temannya.",
                "implied_sound": "Riuh rendah suara ucapan selamat",
                "implied_season": "Pagi hari wisuda"
            },
            "story_prompt": "Sebuah bantuan kecil terakhir sebelum kita berjalan di panggung masing-masing."
        },
        7: {
            "title": "Mawar yang Tertinggal",
            "description": "Buket bunga dan mawar merah yang diletakkan di atas kursi-kursi kosong di luar ruangan, menyisakan keindahan yang sepi.",
            "category_id": "silent-reflection",
            "tone": "Melankolis & Sepi",
            "dominant_colors": ["#FFFFFF", "#800000", "#E5E5E5"],
            "aesthetic_tags": ["rose", "empty", "sadness"],
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Deretan kursi lipat putih dengan mawar di atasnya.",
                "implied_sound": "Desir angin sepoi-sepoi",
                "implied_season": "Siang menjelang sore"
            },
            "story_prompt": "Untuk siapakah mawar ini diletakkan, dan mengapa kursi itu sekarang kosong?"
        },
        8: {
            "title": "Siluet Cahaya Kota",
            "description": "Pertemuan rahasia dua siluet, di mana salah satunya berpendar putih terang di bawah lampu-lampu kota malam hari.",
            "category_id": "silent-reflection",
            "tone": "Misterius & Romantis",
            "dominant_colors": ["#000000", "#FFFFFF", "#D3C2B0"],
            "aesthetic_tags": ["silhouette", "glow", "citylight"],
            "content_labels": ["Pasangan"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Siluet pria menatap siluet wanita yang bercahaya putih benderang.",
                "implied_sound": "Latar belakang deru kota yang sunyi",
                "implied_season": "Malam musim gugur"
            },
            "story_prompt": "Apakah dia nyata, atau hanya ingatan yang bersinar di kepalanya?"
        },
        9: {
            "title": "Tertidur di Antara Buku",
            "description": "Beban tugas dan malam-malam panjang membeku dalam potret seorang mahasiswa tertidur dengan buku menutupi wajahnya.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Pasrah",
            "dominant_colors": ["#3E2723", "#D7CCC8", "#000000"],
            "aesthetic_tags": ["library", "sleep", "exhausted"],
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Seorang pria tertidur di meja perpustakaan dengan buku di atas wajahnya.",
                "implied_sound": "Detik jam dinding perpustakaan",
                "implied_season": "Larut malam"
            },
            "story_prompt": "Mimpi apa yang hadir ketika realitas tugas terlalu berat untuk dipikirkan?"
        },
        10: {
            "title": "Dukungan Seribu Jempol",
            "description": "Senyum manis wisudawati berhijab di tengah kepungan tangan teman-temannya yang memberikan jempol tanda selamat.",
            "category_id": "found-family",
            "tone": "Ceria & Penuh Dukungan",
            "dominant_colors": ["#FFFFFF", "#0A3C72", "#F5F5F5"],
            "aesthetic_tags": ["congratulations", "supportive", "hijab"],
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Wisudawati tersenyum dikelilingi tangan-tangan yang mengacungkan jempol.",
                "implied_sound": "Tawa bersama dan tepuk tangan ceria",
                "implied_season": "Hari wisuda yang cerah"
            },
            "story_prompt": "Kamu tidak pernah berjuang sendirian; mereka selalu ada di belakangmu."
        },
        11: {
            "title": "Toga Tanpa Tuan",
            "description": "Seorang mahasiswa duduk termenung di sebelah gantungan baju yang menampung jubah toga kelulusan miliknya.",
            "category_id": "silent-reflection",
            "tone": "Kontemplatif & Sepi",
            "dominant_colors": ["#1A1A1A", "#8C7A6B", "#FFFFFF"],
            "aesthetic_tags": ["studio", "toga", "reflection"],
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Pria duduk di kursi menatap ke depan, di sampingnya ada toga tergantung.",
                "implied_sound": "Kesunyian studio foto",
                "implied_season": "Sore hari dingin"
            },
            "story_prompt": "Apakah jubah ini benar-benar mewakili pencapaian jiwanya?"
        },
        12: {
            "title": "Langkah Kemenangan Bersama",
            "description": "Tiga sahabat berpegangan tangan sambil mengangkat tangan tinggi-tinggi ke udara, memunggungi gedung kampus yang telah mereka taklukkan.",
            "category_id": "found-family",
            "tone": "Kebebasan & Kebahagiaan",
            "dominant_colors": ["#7A8B7B", "#FFFFFF", "#3E543B"],
            "aesthetic_tags": ["celebration", "graduation", "freedom"],
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Tiga lulusan membelakangi gedung kampus, mengangkat tangan mereka.",
                "implied_sound": "Sorakan kemenangan di bawah langit terbuka",
                "implied_season": "Siang hari berawan"
            },
            "story_prompt": "Kita memulainya sebagai orang asing, dan mengakhirinya sebagai pemenang."
        },
        13: {
            "title": "Membidik Kenangan",
            "description": "Seorang wisudawan memegang kamera dSLR tepat di depan wajahnya, membidik masa lalu yang segera menjadi kenangan.",
            "category_id": "silent-reflection",
            "tone": "Nostalgik & Kreatif",
            "dominant_colors": ["#FFFFFF", "#2C3E50", "#7F8C8D"],
            "aesthetic_tags": ["photography", "graduation-cap", "candid"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Wisudawan menutupi wajahnya dengan kamera di depan gedung kolonial putih.",
                "implied_sound": "Klik mekanis kamera",
                "implied_season": "Pagi hari berkabut"
            },
            "story_prompt": "Satu foto terakhir untuk membekukan waktu yang terus berjalan."
        },
        14: {
            "title": "Melankolia Hitam Putih",
            "description": "Potret wajah sendu seorang pemuda berkacamata yang menunduk, menangkap sisi sunyi dari riuhnya perayaan kelulusan.",
            "category_id": "silent-reflection",
            "tone": "Sendu & Sinematik",
            "dominant_colors": ["#000000", "#FFFFFF", "#555555"],
            "aesthetic_tags": ["portrait", "cinematic", "melancholy"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Potret monokrom pemuda berkacamata menunduk dengan jas hitam.",
                "implied_sound": "Alunan piano lambat",
                "implied_season": "Malam hari kelam"
            },
            "story_prompt": "Di tengah keramaian wisuda, pikirannya terbang ke tempat yang sangat jauh."
        },
        15: {
            "title": "Kepala Kotak",
            "description": "Ekspresi surealis seorang mahasiswa berjas biru yang berpose di tangga dengan kardus menutupi kepalanya.",
            "category_id": "daily-struggle",
            "tone": "Surealis & Konyol",
            "dominant_colors": ["#2980B9", "#C0392B", "#FFFFFF"],
            "aesthetic_tags": ["surreal", "box", "fun"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Pria bersandar di tangga semen dengan kardus merah di kepalanya.",
                "implied_sound": "Derau statis televisi",
                "implied_season": "Sore hari berbayang"
            },
            "story_prompt": "Terkadang lebih mudah menghadapi dunia luar dengan menyembunyikan wajah kita."
        },
        16: {
            "title": "Pengawasan Eksistensial",
            "description": "Sepasang mata raksasa menatap kerumunan manusia di bawah pancaran cahaya vertikal, menggambarkan tekanan eksistensial pasca-kampus.",
            "category_id": "daily-struggle",
            "tone": "Depresif & Surealis",
            "dominant_colors": ["#0F0F0F", "#555555", "#E5E5E5"],
            "aesthetic_tags": ["existentialism", "dark", "illustration"],
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Ilustrasi mata besar di atas kerumunan orang banyak dalam kegelapan.",
                "implied_sound": "Dengung frekuensi rendah",
                "implied_season": "Malam tanpa bintang"
            },
            "story_prompt": "Siapa yang mengawasi kita saat kita berjalan to masa depan yang tak pasti?"
        },
        17: {
            "title": "Setidaknya Kamu Bahagia",
            "description": "Dua siluet manusia duduk di tepi pantai berkabut dengan teks sedih yang menyiratkan kerelaan melepas seseorang.",
            "category_id": "silent-reflection",
            "tone": "Patah Hati & Rela",
            "dominant_colors": ["#DCDCDC", "#000000", "#808080"],
            "aesthetic_tags": ["beach", "minimalist", "sad-text"],
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Siluet hitam dan siluet putih bercahaya duduk di pantai abu-abu.",
                "implied_sound": "Deburan ombak pelan di pantai sepi",
                "implied_season": "Pagi berkabut"
            },
            "story_prompt": "Sebuah perpisahan di tepi pantai, merelakan mimpi yang tidak bisa berjalan bersama."
        },
        18: {
            "title": "Satu di Antara Ratusan",
            "description": "Seorang pria duduk sendirian di satu kursi di tengah lapangan luas yang dipenuhi ratusan kursi lipat kosong.",
            "category_id": "silent-reflection",
            "tone": "Kesepian & Keterasingan",
            "dominant_colors": ["#FFFFFF", "#000000", "#7F8C8D"],
            "aesthetic_tags": ["minimalism", "loneliness", "stark"],
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Pria duduk membelakangi kamera di tengah barisan kursi kosong yang sangat banyak.",
                "implied_sound": "Angin kosong berhembus di lapangan luas",
                "implied_season": "Siang hari mendung"
            },
            "story_prompt": "Ketika panggung perayaan telah sepi, siapakah dirimu yang sebenarnya?"
        },
        19: {
            "title": "Kontemplasi Galeri",
            "description": "Siluet hitam seorang pria berdiri di tengah galeri seni, menatap bingkai foto-foto hitam putih yang dipajang.",
            "category_id": "silent-reflection",
            "tone": "Kontemplatif & Artistik",
            "dominant_colors": ["#FFFFFF", "#000000", "#E5E5E5"],
            "aesthetic_tags": ["gallery", "museum", "silhouette"],
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "sensory_details": {
                "visual_description": "Pria berdiri membelakangi di galeri seni menatap tiga foto di dinding putih.",
                "implied_sound": "Langkah kaki menggema pelan",
                "implied_season": "Musim dingin"
            },
            "story_prompt": "Melihat kembali lembaran hidup yang dibekukan di dinding kenangan."
        },
        20: {
            "title": "Kolase Kenangan Wisuda",
            "description": "Kumpulan potongan memori wisuda: detail toga, medali kelulusan, dan foto-foto candid sahabat dalam warna hangat.",
            "category_id": "silent-reflection",
            "tone": "Nostalgia Hangat",
            "dominant_colors": ["#1A1A1A", "#C39B62", "#4A3B32"],
            "aesthetic_tags": ["collage", "memories", "vintage"],
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "sensory_details": {
                "visual_description": "Kolase berbagai foto detail kelulusan dan potret wisudawan.",
                "implied_sound": "Campuran suara tawa dan jepretan kamera",
                "implied_season": "Sore hari keemasan"
            },
            "story_prompt": "Setiap serpihan foto ini menyimpan cerita perjuangan yang tak ternilai."
        }
    }

    # Generate custom details for the rest (21 to 93) based on the user's specific table
    for img_id in range(21, 94):
        # Determine labels by image type/index
        if img_id == 21:
            details[img_id] = {
                "title": "Cahaya di Ruang Kosong",
                "description": "Cahaya matahari sore menembus celah jendela, memproyeksikan bayangan garis-garis di dinding semen ruang kosong dengan kursi kayu.",
                "category_id": "silent-reflection",
                "tone": "Kesunyian Indah",
                "dominant_colors": ["#8C7B6E", "#D9C3B0", "#2C2C2C"],
                "aesthetic_tags": ["shadows", "empty-room", "nostalgic"],
                "content_labels": ["Objek"],
                "technique_labels": ["Dark"],
                "sensory_details": {
                    "visual_description": "Kursi kayu di sudut ruangan kosong dengan bayangan jendela di dinding.",
                    "implied_sound": "Keheningan total sore hari",
                    "implied_season": "Sore hari musim kemarau"
                },
                "story_prompt": "Ruang kelas ini pernah dipenuhi tawa, kini menyisakan sunyi dan cahaya."
            }
        elif img_id == 22:
            details[img_id] = {
                "title": "Ngejar Sarjana!",
                "description": "Seorang mahasiswa berlari kencang di lintasan lari mengenakan toga merah berkibar, ekspresi penuh semangat memburu kelulusan.",
                "category_id": "daily-struggle",
                "tone": "Lari & Bersemangat",
                "dominant_colors": ["#C0392B", "#2C3E50", "#BDC3C7"],
                "aesthetic_tags": ["running", "sarjana", "funny"],
                "content_labels": ["Solo"],
                "technique_labels": ["Blur"],
                "sensory_details": {
                    "visual_description": "Wisudawan berlari di trek atletik biru dengan jubah toga merah terbang.",
                    "implied_sound": "Derap langkah kaki cepat dan teriakan semangat",
                    "implied_season": "Pagi hari yang cerah"
                },
                "story_prompt": "Berlari sekencang mungkin untuk menyelesaikan babak perjuangan ini."
            }
        elif img_id == 23:
            details[img_id] = {
                "title": "Langkah di Dinding Jingga",
                "description": "Dua lulusan melangkah ceria di depan dinding keramik jingga, memadukan formalitas toga dengan pose jenaka.",
                "category_id": "found-family",
                "tone": "Ceria & Hangat",
                "dominant_colors": ["#D35400", "#2C3E50", "#F39C12"],
                "aesthetic_tags": ["friends", "aesthetic", "orange-wall"],
                "content_labels": ["Teman"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Pria dan wanita bertoga berpose di depan dinding ubin merah bata jingga.",
                    "implied_sound": "Canda gurau dua sahabat",
                    "implied_season": "Sore hari hangat"
                },
                "story_prompt": "Berjalan bersama melewati batas akhir masa perkuliahan."
            }
        elif img_id == 24:
            details[img_id] = {
                "title": "Bayang-Bayang Kampus",
                "description": "Seorang lulusan berdiri tegak di tengah bayangan struktur kisi-kisi besi raksasa yang terpantul di lapangan semen.",
                "category_id": "silent-reflection",
                "tone": "Tekanan Masa Depan",
                "dominant_colors": ["#7F8C8D", "#000000", "#FFFFFF"],
                "aesthetic_tags": ["shadows", "minimalist", "geometric"],
                "content_labels": ["Solo"],
                "technique_labels": ["Dark"],
                "sensory_details": {
                    "visual_description": "Foto high-angle wisudawan berdiri dikelilingi bayangan garis-garis geometris besar.",
                    "implied_sound": "Gema langkah kaki pelan",
                    "implied_season": "Siang hari terik"
                },
                "story_prompt": "Bayangan masa depan yang membentang lebar di hadapan jalannya."
            }
        elif img_id == 25:
            details[img_id] = {
                "title": "Wajah di Balik Buku",
                "description": "Dua mahasiswa memegang buku terbuka tepat di depan wajah mereka, seolah-olah seluruh identitas mereka telah terserap dalam studi.",
                "category_id": "silent-reflection",
                "tone": "Akademis & Misterius",
                "dominant_colors": ["#2C3E50", "#8E44AD", "#ECF0F1"],
                "aesthetic_tags": ["books", "library", "studying"],
                "content_labels": ["Teman"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Dua orang bertoga menyembunyikan wajah di balik buku tebal.",
                    "implied_sound": "Lembaran buku yang dibalik lambat",
                    "implied_season": "Sore hari tenang"
                },
                "story_prompt": "Siapakah kita saat teori-teori buku selesai kita pelajari?"
            }
        elif img_id == 28:
            details[img_id] = {
                "title": "Dibidik Kamera Sahabat",
                "description": "Seorang wisudawati tersenyum manis memegang tabung ijazah, dikelilingi oleh tangan-tangan yang memegang ponsel untuk memotretnya.",
                "category_id": "found-family",
                "tone": "Bangga & Penuh Kasih",
                "dominant_colors": ["#000000", "#F1C40F", "#ECF0F1"],
                "aesthetic_tags": ["phones", "congratulations", "smile"],
                "content_labels": ["Teman"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Wisudawati tersenyum di tengah jepretan layar-layar handphone di depannya.",
                    "implied_sound": "Suara tawa ramah dan klik kamera handphone",
                    "implied_season": "Pagi hari cerah"
                },
                "story_prompt": "Dalam ingatan mereka, hari ini adalah milikmu sepenuhnya."
            }
        elif img_id == 34:
            details[img_id] = {
                "title": "Batik dan Kebaya Bangga",
                "description": "Sepasang orang tua mengenakan batik dan kebaya tradisional berdiri di balkon kampus, menatap penuh kebanggaan pada kelulusan anak mereka.",
                "category_id": "found-family",
                "tone": "Kehangatan Keluarga",
                "dominant_colors": ["#4E3629", "#D7CCC8", "#3E2723"],
                "aesthetic_tags": ["parents", "batik", "family"],
                "content_labels": ["Keluarga"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Kedua orang tua tersenyum di balkon bangunan kolonial kampus.",
                    "implied_sound": "Bisikan bangga sang ayah pada ibunya",
                    "implied_season": "Siang hari sejuk"
                },
                "story_prompt": "Gelar ini adalah milik mereka yang mendoakanmu tanpa putus."
            }
        elif img_id == 35:
            details[img_id] = {
                "title": "Tenggelam dalam Lembaran Teori",
                "description": "Kolase artistik siluet manusia di tengah kolom koran/buku tebal, melambangkan perjuangan membaca skripsi tak berkesudahan.",
                "category_id": "daily-struggle",
                "tone": "Tertekan & Akademis",
                "dominant_colors": ["#FFFFFF", "#000000", "#7F8C8D"],
                "aesthetic_tags": ["newspaper", "collage", "existential"],
                "content_labels": ["Solo"],
                "technique_labels": ["Dark"],
                "sensory_details": {
                    "visual_description": "Siluet hitam manusia berjalan di atas halaman koran B&W penuh tulisan padat.",
                    "implied_sound": "Kertas koran yang robek perlahan",
                    "implied_season": "Malam hari suntuk"
                },
                "story_prompt": "Menjadi satu titik kecil di tengah gunungan kata dan teori."
            }
        elif img_id == 45:
            details[img_id] = {
                "title": "Ksatria dan Mawar Kuning",
                "description": "Ilustrasi ksatria berbaju besi memegang mawar kuning dengan tulisan '괜찮아요' (Tidak apa-apa), sebuah pesan bertahan di tengah badai.",
                "category_id": "daily-struggle",
                "tone": "Harapan di Tengah Badai",
                "dominant_colors": ["#2C3E50", "#F1C40F", "#7F8C8D"],
                "aesthetic_tags": ["knight", "illustration", "hope"],
                "content_labels": ["Objek"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Ksatria berzirah mengangkat mawar kuning dengan tulisan Korea di sampingnya.",
                    "implied_sound": "Petikan kecapi yang lembut dan sunyi",
                    "implied_season": "Musim dingin berakhir"
                },
                "story_prompt": "Ksatria terkuat adalah dia yang mampu menjaga kelembutan di balik zirahnya."
            }
        elif img_id == 57:
            details[img_id] = {
                "title": "Berlari Menyambut Kebebasan",
                "description": "Potret hitam putih buram menunjukkan para siswa berlari riang di koridor sekolah tua, seolah menyambut hari terakhir kelas.",
                "category_id": "found-family",
                "tone": "Nostalgia Ceria",
                "dominant_colors": ["#7F8C8D", "#FFFFFF", "#2C3E50"],
                "aesthetic_tags": ["running", "candid", "coming-of-age"],
                "content_labels": ["Teman"],
                "technique_labels": ["Blur"],
                "sensory_details": {
                    "visual_description": "Foto motion-blur hitam putih siswa berseragam berlari di koridor sekolah berasitektur kolonial.",
                    "implied_sound": "Suara langkah kaki riuh dan tawa lepas",
                    "implied_season": "Sore hari musim panas"
                },
                "story_prompt": "Saat lonceng terakhir berbunyi, kita tahu kita tak akan kembali ke lorong ini dengan cara yang sama."
            }
        elif img_id == 65:
            details[img_id] = {
                "title": "Kacamata Jenaka Sahabat",
                "description": "Keluarga dan wisudawan berpose kocak dengan membuat bentuk kacamata menggunakan jari mereka, meluluhkan suasana formal.",
                "category_id": "found-family",
                "tone": "Humor & Hangat",
                "dominant_colors": ["#4A3B32", "#F5EBE6", "#1E1E1E"],
                "aesthetic_tags": ["funny-pose", "family", "candid"],
                "content_labels": ["Keluarga"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Keluarga tersenyum lebar dengan pose tangan membentuk kacamata di depan mata mereka.",
                    "implied_sound": "Tawa renyah bersama di studio",
                    "implied_season": "Siang hari cerah"
                },
                "story_prompt": "Karena kelulusan terbaik dirayakan dengan tawa lepas bersama keluarga."
            }
        elif img_id == 77:
            details[img_id] = {
                "title": "Wisuda Bersama Mentor Fantasi",
                "description": "Edit foto wisuda jenaka menempatkan wisudawan di antara Koro-sensei dan Ksatria Guts Berserk, memadukan dunia mimpi dan kenyataan.",
                "category_id": "daily-struggle",
                "tone": "Imaginatif & Jenaka",
                "dominant_colors": ["#F1C40F", "#2C3E50", "#000000"],
                "aesthetic_tags": ["anime", "berserk", "funny-edit"],
                "content_labels": ["Solo"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Edit foto pemuda bertoga diapit oleh Koro-sensei kuning dan Guts berzirah hitam.",
                    "implied_sound": "Soundtrack anime perjuangan",
                    "implied_season": "Sore hari penuh warna"
                },
                "story_prompt": "Dua guru terbaik: yang mengajarkan cara belajar, dan yang mengajarkan cara bertarung."
            }
        elif img_id == 79:
            details[img_id] = {
                "title": "Bab Ini Selesai",
                "description": "Latar belakang sunset jingga membingkai siluet seorang mahasiswa bertoga berjalan menjauh, menandai berakhirnya sebuah babak hidup.",
                "category_id": "into-the-unknown",
                "tone": "Bittersweet Farewell",
                "dominant_colors": ["#E67E22", "#2C3E50", "#D35400"],
                "aesthetic_tags": ["sunset", "silhouette", "departure"],
                "content_labels": ["Solo"],
                "technique_labels": ["Sunset"],
                "sensory_details": {
                    "visual_description": "Siluet wisudawan membelakangi kamera berjalan di jalan beraspal saat matahari terbenam jingga keemasan.",
                    "implied_sound": "Alunan gitar akustik penutup film",
                    "implied_season": "Senja musim kemarau"
                },
                "story_prompt": "Menutup buku hari ini, bersiap membuka lembaran baru esok pagi."
            }
        elif img_id == 80:
            details[img_id] = {
                "title": "Kereta Menuju Masa Depan",
                "description": "Seorang wisudawan memegang toga berjalan menyusuri peron stasiun kereta api di sore hari, melambangkan perjalanan ke kota baru pasca-lulus.",
                "category_id": "into-the-unknown",
                "tone": "Harapan & Keberangkatan",
                "dominant_colors": ["#2C3E50", "#E67E22", "#BDC3C7"],
                "aesthetic_tags": ["train-station", "departure", "journey"],
                "content_labels": ["Solo"],
                "technique_labels": ["Sunset"],
                "sensory_details": {
                    "visual_description": "Siluet wisudawan memegang jubah bertoga berjalan di sepanjang peron kereta api saat senja.",
                    "implied_sound": "Suara klakson kereta api dan deru mesin perlahan",
                    "implied_season": "Senja musim hujan"
                },
                "story_prompt": "Kereta ini membawa lebih dari sekadar tubuh; ia membawa semua mimpi masa muda."
            }
        elif img_id == 81:
            details[img_id] = {
                "title": "Air Mata di Album Usang",
                "description": "Potret penuh haru ibu dan anak melihat album foto lama bersama, meneteskan air mata bahagia melihat perjalanan panjang sang sarjana.",
                "category_id": "found-family",
                "tone": "Haru & Penuh Kasih",
                "dominant_colors": ["#3E2723", "#F5EBE0", "#D5BDAF"],
                "aesthetic_tags": ["mother", "tears", "family-love"],
                "content_labels": ["Keluarga"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Ibu memeluk anaknya yang mengenakan toga sambil membuka lembar album foto.",
                    "implied_sound": "Isak tangis bahagia yang tertahan",
                    "implied_season": "Sore hari penuh haru"
                },
                "story_prompt": "Ibu berkata, 'Semua lelahku hilang hari ini melihatmu memakai toga.'"
            }
        elif img_id == 83:
            details[img_id] = {
                "title": "Hari Pertama vs Hari Terakhir",
                "description": "Kolase foto membandingkan wajah lugu mahasiswa baru di hari pertama kuliah (2019) dan wisudawan di hari terakhir kelulusan (2026).",
                "category_id": "into-the-unknown",
                "tone": "Nostalgia Transisi",
                "dominant_colors": ["#2C3E50", "#7F8C8D", "#ECEFF1"],
                "aesthetic_tags": ["transition", "first-day", "last-day"],
                "content_labels": ["Solo"],
                "technique_labels": ["Film"],
                "sensory_details": {
                    "visual_description": "Dua foto bersanding: mahasiswa beransel di kelas tua, dan mahasiswa bertoga tersenyum di balkon luar.",
                    "implied_sound": "Suara angin waktu yang berputar cepat",
                    "implied_season": "Siklus 7 tahun perjalanan"
                },
                "story_prompt": "Jika kamu bisa berbisik pada dirimu di hari pertama kuliah, apa yang akan kamu katakan?"
            }
        elif img_id == 88:
            details[img_id] = {
                "title": "Sore di Kelas yang Kosong",
                "description": "Cahaya matahari sore yang hangat menerobos jendela menyinari deretan meja dan kursi kosong di ruang kelas kuliah yang sunyi.",
                "category_id": "silent-reflection",
                "tone": "Kesunyian Indah",
                "dominant_colors": ["#8A6D56", "#E5D4C0", "#2C2C2C"],
                "aesthetic_tags": ["empty-classroom", "sunset-glow", "nostalgic"],
                "content_labels": ["Objek"],
                "technique_labels": ["Dark"],
                "sensory_details": {
                    "visual_description": "Ruang kelas kuliah kosong disinari berkas cahaya sore yang hangat dari samping.",
                    "implied_sound": "Gema debu-debu beterbangan ditiup angin sepoi",
                    "implied_season": "Akhir semester sore hari"
                },
                "story_prompt": "Di bangku inilah semua ide, kecemasan, dan persahabatan pernah lahir."
            }
        elif img_id == 90:
            details[img_id] = {
                "title": "Bab Selesai, Cerita Berlanjut",
                "description": "Seorang wisudawan memunggungi kamera berjalan menuju gerbang cahaya keemasan matahari terbit, membawa ijazah di tangannya.",
                "category_id": "into-the-unknown",
                "tone": "Optimistis & Syahdu",
                "dominant_colors": ["#E67E22", "#34495E", "#FFFFFF"],
                "aesthetic_tags": ["sunrise", "finish", "new-chapter"],
                "content_labels": ["Solo"],
                "technique_labels": ["Sunset"],
                "sensory_details": {
                    "visual_description": "Wisudawan membelakangi kamera berjalan di aspal basah menuju matahari terbit yang megah.",
                    "implied_sound": "Musik orkestra instrumental yang megah dan tenang",
                    "implied_season": "Fajar musim kemarau"
                },
                "story_prompt": "Ini bukanlah akhir dari cerita, melainkan awal dari perjalanan yang sesungguhnya."
            }
        elif img_id == 91:
            details[img_id] = {
                "title": "Ke Ufuk Baru",
                "description": "Seorang lulusan berjalan menembus kehangatan cahaya sore di sepanjang koridor luar kampus, siap menghadapi dunia baru.",
                "category_id": "into-the-unknown",
                "tone": "Nostalgia Sore Hari",
                "dominant_colors": ["#D35400", "#2C3E50", "#ECEFF1"],
                "aesthetic_tags": ["candid", "golden hour", "sunset"],
                "content_labels": ["Solo"],
                "technique_labels": ["Sunset"],
                "sensory_details": {
                    "visual_description": "Lulusan membelakangi kamera berjalan di luar saat sunset keemasan.",
                    "implied_sound": "Petikan gitar akustik yang lambat",
                    "implied_season": "Senja musim kemarau"
                },
                "story_prompt": "Melangkah dengan harapan baru ke arah matahari terbenam."
            }
        elif img_id == 92:
            details[img_id] = {
                "title": "Pesan dari Guru Terakhir",
                "description": "Langkah kaki wisudawan di jalan beraspal senja hari dengan ilustrasi surat dari Koro-sensei berisi selamat dan nasehat hidup.",
                "category_id": "into-the-unknown",
                "tone": "Nostalgia Hangat",
                "dominant_colors": ["#D35400", "#2C3E50", "#F5EBE6"],
                "aesthetic_tags": ["message", "korosensei", "candid"],
                "content_labels": ["Solo"],
                "technique_labels": ["Sunset"],
                "sensory_details": {
                    "visual_description": "Lulusan berjalan membelakangi di jalan kampus saat senja, dengan teks surat Koro-sensei bertulis tangan di sudut.",
                    "implied_sound": "Bisikan angin sore membawa petuah hangat",
                    "implied_season": "Senja kelulusan"
                },
                "story_prompt": "Selamat. Kamu telah belajar banyak. Sekarang ajarkan kebaikan itu kepada dunia."
            }
        elif img_id == 93:
            details[img_id] = {
                "title": "Tawa Malam Kelulusan",
                "description": "Potret candid berkecepatan rendah menggunakan flash, menangkap ekspresi tawa lepas sekelompok sahabat berjalan bersama di kegelapan malam kelulusan.",
                "category_id": "found-family",
                "tone": "Kebebasan Jiwa & Tawa",
                "dominant_colors": ["#000000", "#FFFFFF", "#3A3A3A"],
                "aesthetic_tags": ["candid-flash", "night-walk", "friends"],
                "content_labels": ["Teman"],
                "technique_labels": ["Flash"],
                "sensory_details": {
                    "visual_description": "Foto flash buram malam hari memperlihatkan sahabat merangkul pundak satu sama lain sambil tertawa lebar.",
                    "implied_sound": "Tawa lepas yang menggema di jalan sepi tengah malam",
                    "implied_season": "Tengah malam wisuda"
                },
                "story_prompt": "Biar dunia luar berisik, malam ini kita tertawa bersama seolah waktu telah berhenti."
            }
        else:
            # Fallback generator for other IDs matching subject & technique distributions
            content_opts = ["Solo", "Keluarga", "Teman", "Pasangan", "Objek"]
            tech_opts = ["Sunset", "Blur", "Dark", "Flash", "Film"]
            c_label = content_opts[img_id % len(content_opts)]
            t_label = tech_opts[(img_id + 1) % len(tech_opts)]
            
            # Simple color palette logic
            colors = ["#2C3E50", "#7F8C8D", "#BDC3C7"]
            if t_label == "Sunset":
                colors = ["#D35400", "#2C3E50", "#ECF0F1"]
            elif t_label == "Dark":
                colors = ["#1A1A1A", "#8C7A6B", "#FFFFFF"]
                
            details[img_id] = {
                "title": f"Momen Wisuda #{img_id}",
                "description": f"Kenangan visual kelulusan bertema {c_label.lower()} yang diproses dengan sentuhan estetika {t_label.lower()}.",
                "category_id": "silent-reflection",
                "tone": "Nostalgia Hangat",
                "dominant_colors": colors,
                "aesthetic_tags": ["graduation", "student", "vibes"],
                "content_labels": [c_label],
                "technique_labels": [t_label],
                "sensory_details": {
                    "visual_description": "Potret suasana wisuda di sudut kampus.",
                    "implied_sound": "Gemuruh suara kerumunan dan tawa kecil",
                    "implied_season": "Sore hari yang hangat"
                },
                "story_prompt": "Setiap sudut kampus ini memiliki cerita perjuangannya sendiri."
            }

    # Build final list
    final_images = []
    for k, v in mapping.items():
        img_id_int = int(k)
        img_detail = details.get(img_id_int, {})
        
        # Merge mapping info
        img_detail["id"] = v["id"]
        img_detail["filename"] = v["filename"]
        
        # Generate photography details
        photo_details = get_photography_details(
            img_detail.get("title", ""),
            img_detail.get("category_id", ""),
            img_detail.get("content_labels", []),
            img_detail.get("technique_labels", []),
            img_detail.get("dominant_colors", []),
            img_id_int
        )
        img_detail["photography_details"] = photo_details
        
        final_images.append(img_detail)
        
    final_json = {
        "collection_theme": "Koleksi Moodboard Wisuda & Referensi Foto Kelulusan",
        "collection_summary": "Panduan referensi visual, komposisi, subjek, dan teknik fotografi untuk dokumentasi kelulusan (wisuda).",
        "collection_story": "Moodboard ini dikurasi secara sistematis untuk mempermudah pemilihan konsep foto wisuda. Terbagi berdasarkan kategori subjek (Solo, Keluarga, Teman, Pasangan, Detail Objek) serta vibes/teknik visual (Sunset/Golden Hour, Motion Blur, Dark & Moody, Flash Photography, Film/Analog). Gunakan koleksi ini sebagai acuan pose, tata cahaya, wardrobe, dan sudut pandang kamera saat sesi pemotretan berlangsung.",
        "categories": categories,
        "images": final_images
    }
    
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)
        
    print(f"Sukses! Menulis {len(final_images)} data gambar ke {METADATA_FILE}.")

if __name__ == "__main__":
    main()
