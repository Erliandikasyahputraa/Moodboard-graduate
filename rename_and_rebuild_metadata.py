import os
import json
import hashlib
import shutil

IMAGE_DIR = "pict Moodboard wisuda"
MAPPING_FILE = "docs/sheet_mapping.json"
METADATA_FILE = "metadata.json"

def calculate_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def main():
    if not os.path.exists(MAPPING_FILE):
        print(f"[Error] {MAPPING_FILE} tidak ditemukan!")
        return

    with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
        sheet_mapping = json.load(f)

    categories = [
        {
            "id": "bittersweet-farewell",
            "name": "Bittersweet Farewell",
            "description": "Momen-momen perpisahan yang manis namun menyedihkan di sudut-sudut kampus."
        },
        {
            "id": "found-family",
            "name": "Found Family",
            "description": "Keluarga dan sahabat yang kita temukan sepanjang perjuangan akademis."
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

    # Mappings for all 93 images (100% Curated)
    curated_data = {
        1: {
            "new_name": "existential-circle-dark.jpg",
            "title": "Tatapan dari Kehampaan",
            "description": "Di dasar jurang sunyi, delapan siluet pria berjas membisu mengelilingi tepian, tatapan mereka seperti jangkar yang menarik jiwa ke kedalaman.",
            "category_id": "daily-struggle",
            "tone": "Kekosongan Abadi",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#0A0A0A", "#F2F0E6", "#4A4A4A"],
            "aesthetic_tags": ["Monokromatik", "Existential", "Sinematik"],
            "sensory_details": {
                "visual_description": "Siluet delapan pria berjas mengelilingi lubang dari atas.",
                "implied_sound": "Hening yang memekakkan",
                "implied_season": "Senja membeku"
            },
            "story_prompt": "Saat tatapan itu mengunci jiwanya, ia tahu ia harus menyerah."
        },
        2: {
            "new_name": "couple-garden-candid.jpg",
            "title": "Detik Sebelum Janji di Bawah Naungan",
            "description": "Dalam keheningan taman yang rimbun, sepasang mata menanti sebuah jawaban, sementara siluet janji menyelimuti harapan.",
            "category_id": "silent-reflection",
            "tone": "Antisipasi Manis",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#3E543B", "#E8D3C8", "#2C2C2C"],
            "aesthetic_tags": ["cinematic", "soft focus", "nature"],
            "sensory_details": {
                "visual_description": "Wajah perempuan kabur di depan, pria berjas di kejauhan.",
                "implied_sound": "Kicau burung samar",
                "implied_season": "Awal musim panas"
            },
            "story_prompt": "Siapakah yang menunggu di antara pepohonan yang sunyi?"
        },
        3: {
            "new_name": "solo-formal-pasfoto-merah.png",
            "title": "Lensa Merah Formal",
            "description": "Pas foto berlatar belakang merah menyala yang membekukan wajah tegang seorang mahasiswa, syarat mutlak sebuah kelulusan.",
            "category_id": "daily-struggle",
            "tone": "Formal & Tegang",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FF0000", "#000000", "#FFFFFF"],
            "aesthetic_tags": ["pasfoto", "indonesia", "formal"],
            "sensory_details": {
                "visual_description": "Pas foto formal berlatar merah, mengenakan peci hitam dan jas.",
                "implied_sound": "Suara jepretan kamera studio tua",
                "implied_season": "Siang hari yang terik"
            },
            "story_prompt": "Di balik tatapan datar ini, ada ribuan malam tanpa tidur demi gelar sarjana."
        },
        4: {
            "new_name": "meme-aku-uin-makassar.jpg",
            "title": "Meme Aku UIN",
            "description": "Sebuah meme humor mahasiswa dengan latar gerbang kampus UIN Alauddin Makassar, merayakan identitas dengan tawa jenaka.",
            "category_id": "daily-struggle",
            "tone": "Jenaka & Satir",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#00FF00", "#D3D3D3", "#8B4513"],
            "aesthetic_tags": ["meme", "uin", "humor"],
            "sensory_details": {
                "visual_description": "Suntingan foto pria berjaket hijau digambar tangan menunjuk gerbang UIN.",
                "implied_sound": "Lagu TikTok viral yang berisik",
                "implied_season": "Musim kuliah"
            },
            "story_prompt": "Berapa banyak mahasiswa yang tertawa melihat gerbang ini setiap paginya?"
        },
        5: {
            "new_name": "meme-spongebob-perjuangan-revisi.jpg",
            "title": "Tragedi Skripsi Patrick",
            "description": "Penggambaran kondisi fisik dan mental yang hancur setelah begadang mengerjakan revisi skripsi tak berujung.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Jenaka",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#E5E5E5", "#FF69B4", "#808080"],
            "aesthetic_tags": ["cartoon", "meme", "stress"],
            "sensory_details": {
                "visual_description": "Patrick Star memegang pedang di samping Squidward yang terbungkus perban di kursi roda.",
                "implied_sound": "Musik dramatis kartun",
                "implied_season": "Musim revisi akhir"
            },
            "story_prompt": "Ketika dosen pembimbing berkata 'tolong revisi bab 4 lagi'."
        },
        6: {
            "new_name": "teman-candid-merapikan-toga.jpg",
            "title": "Dokumenter Kelulusan",
            "description": "Potret candid hitam putih yang menangkap kehangatan wisudawan saling merapikan atribut toga di tengah keramaian.",
            "category_id": "bittersweet-farewell",
            "tone": "Hangat & Dokumenter",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#111111", "#FFFFFF", "#808080"],
            "aesthetic_tags": ["black-and-white", "candid", "friendship"],
            "sensory_details": {
                "visual_description": "Foto monokrom wisudawan merapikan topi toga temannya.",
                "implied_sound": "Riuh rendah suara ucapan selamat",
                "implied_season": "Pagi hari wisuda"
            },
            "story_prompt": "Sebuah bantuan kecil terakhir sebelum kita berjalan di panggung masing-masing."
        },
        7: {
            "new_name": "detail-mawar-kursi-kosong.jpg",
            "title": "Mawar yang Tertinggal",
            "description": "Buket bunga dan mawar merah yang diletakkan di atas kursi-kursi kosong di luar ruangan, menyisakan keindahan yang sepi.",
            "category_id": "silent-reflection",
            "tone": "Melankolis & Sepi",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#800000", "#E5E5E5"],
            "aesthetic_tags": ["rose", "empty", "sadness"],
            "sensory_details": {
                "visual_description": "Deretan kursi lipat putih dengan mawar di atasnya.",
                "implied_sound": "Desir angin sepoi-sepoi",
                "implied_season": "Siang menjelang sore"
            },
            "story_prompt": "Untuk siapakah mawar ini diletakkan, dan mengapa kursi itu sekarang kosong?"
        },
        8: {
            "new_name": "pasangan-siluet-kota-malam.jpg",
            "title": "Siluet Cahaya Kota",
            "description": "Pertemuan rahasia dua siluet, di mana salah satunya berpendar putih terang di bawah lampu-lampu kota malam hari.",
            "category_id": "silent-reflection",
            "tone": "Misterius & Romantis",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#D3C2B0"],
            "aesthetic_tags": ["silhouette", "glow", "citylight"],
            "sensory_details": {
                "visual_description": "Siluet pria menatap siluet wanita yang bercahaya putih benderang.",
                "implied_sound": "Latar belakang deru kota yang sunyi",
                "implied_season": "Malam musim gugur"
            },
            "story_prompt": "Apakah dia nyata, atau hanya ingatan yang bersinar di kepalanya?"
        },
        9: {
            "new_name": "solo-tidur-perpustakaan-buku.jpg",
            "title": "Tertidur di Antara Buku",
            "description": "Beban tugas dan malam-malam panjang membeku dalam potret seorang mahasiswa tidur dengan buku menutupi wajahnya.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Pasrah",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#3E2723", "#D7CCC8", "#000000"],
            "aesthetic_tags": ["library", "sleep", "exhausted"],
            "sensory_details": {
                "visual_description": "Seorang pria tidur di meja perpustakaan dengan buku di atas wajahnya.",
                "implied_sound": "Detik jam dinding perpustakaan",
                "implied_season": "Larut malam"
            },
            "story_prompt": "Mimpi apa yang hadir ketika realitas tugas terlalu berat untuk dipikirkan?"
        },
        10: {
            "new_name": "teman-wisudawati-hijab-congrats.jpg",
            "title": "Dukungan Seribu Jempol",
            "description": "Senyum manis wisudawati berhijab di tengah kepungan tangan teman-temannya yang memberikan jempol tanda selamat.",
            "category_id": "found-family",
            "tone": "Ceria & Penuh Dukungan",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#0A3C72", "#F5F5F5"],
            "aesthetic_tags": ["congratulations", "supportive", "hijab"],
            "sensory_details": {
                "visual_description": "Wisudawati tersenyum dikelilingi tangan-tangan yang mengacungkan jempol.",
                "implied_sound": "Tawa bersama dan tepuk tangan ceria",
                "implied_season": "Hari wisuda yang cerah"
            },
            "story_prompt": "Kamu tidak pernah berjuang sendirian; mereka selalu ada di belakangmu."
        },
        11: {
            "new_name": "solo-toga-gantungan-termenung.jpg",
            "title": "Toga Tanpa Tuan",
            "description": "Seorang mahasiswa duduk termenung di sebelah gantungan baju yang menampung jubah toga kelulusan miliknya.",
            "category_id": "silent-reflection",
            "tone": "Kontemplatif & Sepi",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#1A1A1A", "#8C7A6B", "#FFFFFF"],
            "aesthetic_tags": ["studio", "toga", "reflection"],
            "sensory_details": {
                "visual_description": "Pria duduk di kursi menatap ke depan, di sampingnya ada toga tergantung.",
                "implied_sound": "Kesunyian studio foto",
                "implied_season": "Sore hari dingin"
            },
            "story_prompt": "Apakah jubah ini benar-benar mewakili pencapaian jiwanya?"
        },
        12: {
            "new_name": "teman-berpegangan-tangan-kampus.jpg",
            "title": "Langkah Kemenangan Bersama",
            "description": "Tiga sahabat berpegangan tangan sambil mengangkat tangan tinggi-tinggi ke udara, memunggungi gedung kampus yang telah mereka taklukkan.",
            "category_id": "found-family",
            "tone": "Kebebasan & Kebahagiaan",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#7A8B7B", "#FFFFFF", "#3E543B"],
            "aesthetic_tags": ["celebration", "graduation", "freedom"],
            "sensory_details": {
                "visual_description": "Tiga lulusan membelakangi gedung kampus, mengangkat tangan mereka.",
                "implied_sound": "Sorakan kemenangan di bawah langit terbuka",
                "implied_season": "Siang hari berawan"
            },
            "story_prompt": "Kita memulainya sebagai orang asing, dan mengakhirinya sebagai pemenang."
        },
        13: {
            "new_name": "solo-candid-bidik-kamera.jpg",
            "title": "Membidik Kenangan",
            "description": "Seorang wisudawan memegang kamera dSLR tepat di depan wajahnya, membidik masa lalu yang segera menjadi kenangan.",
            "category_id": "silent-reflection",
            "tone": "Nostalgik & Kreatif",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#2C3E50", "#7F8C8D"],
            "aesthetic_tags": ["photography", "graduation-cap", "candid"],
            "sensory_details": {
                "visual_description": "Wisudawan menutupi wajahnya dengan kamera di depan gedung kolonial putih.",
                "implied_sound": "Klik mekanis kamera",
                "implied_season": "Pagi hari berkabut"
            },
            "story_prompt": "Satu foto terakhir untuk membekukan waktu yang terus berjalan."
        },
        14: {
            "new_name": "solo-kacamata-portrait-bw.jpg",
            "title": "Melankolia Hitam Putih",
            "description": "Potret wajah sendu seorang pemuda berkacamata yang menunduk, menangkap sisi sunyi dari riuhnya perayaan kelulusan.",
            "category_id": "silent-reflection",
            "tone": "Sendu & Sinematik",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#000000", "#FFFFFF", "#555555"],
            "aesthetic_tags": ["portrait", "cinematic", "melancholy"],
            "sensory_details": {
                "visual_description": "Potret monokrom pemuda berkacamata menunduk dengan jas hitam.",
                "implied_sound": "Alunan piano lambat",
                "implied_season": "Malam hari kelam"
            },
            "story_prompt": "Di tengah keramaian wisuda, pikirannya terbang ke tempat yang sangat jauh."
        },
        15: {
            "new_name": "solo-candid-kardus-kepala.jpg",
            "title": "Kepala Kotak",
            "description": "Ekspresi surealis seorang mahasiswa berjas biru yang berpose di tangga dengan kardus menutupi kepalanya.",
            "category_id": "daily-struggle",
            "tone": "Surealis & Konyol",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2980B9", "#C0392B", "#FFFFFF"],
            "aesthetic_tags": ["surreal", "box", "fun"],
            "sensory_details": {
                "visual_description": "Pria bersandar di tangga semen dengan kardus merah di kepalanya.",
                "implied_sound": "Derau statis televisi",
                "implied_season": "Sore hari berbayang"
            },
            "story_prompt": "Terkadang lebih mudah menghadapi dunia luar dengan menyembunyikan wajah kita."
        },
        16: {
            "new_name": "existential-eyes-crowd.jpg",
            "title": "Pengawasan Eksistensial",
            "description": "Sepasang mata raksasa menatap kerumunan manusia di bawah pancaran cahaya vertikal, menggambarkan tekanan eksistensial pasca-kampus.",
            "category_id": "daily-struggle",
            "tone": "Depresif & Surealis",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#0F0F0F", "#555555", "#E5E5E5"],
            "aesthetic_tags": ["existentialism", "dark", "illustration"],
            "sensory_details": {
                "visual_description": "Ilustrasi mata besar di atas kerumunan orang banyak dalam kegelapan.",
                "implied_sound": "Dengung frekuensi rendah",
                "implied_season": "Malam tanpa bintang"
            },
            "story_prompt": "Siapa yang mengawasi kita saat kita berjalan ke masa depan yang tak pasti?"
        },
        17: {
            "new_name": "pasangan-pantai-minimalist-graphic.jpg",
            "title": "Setidaknya Kamu Bahagia",
            "description": "Dua siluet manusia duduk di tepi pantai berkabut dengan teks sedih yang menyiratkan kerelaan melepas seseorang.",
            "category_id": "silent-reflection",
            "tone": "Patah Hati & Rela",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#DCDCDC", "#000000", "#808080"],
            "aesthetic_tags": ["beach", "minimalist", "sad-text"],
            "sensory_details": {
                "visual_description": "Siluet hitam dan siluet putih bercahaya duduk di pantai abu-abu.",
                "implied_sound": "Deburan ombak pelan di pantai sepi",
                "implied_season": "Pagi berkabut"
            },
            "story_prompt": "Sebuah perpisahan di tepi pantai, merelakan mimpi yang tidak bisa berjalan bersama."
        },
        18: {
            "new_name": "solo-lapangan-kursi-kosong-bw.jpg",
            "title": "Satu di Antara Ratusan",
            "description": "Seorang pria duduk sendirian di satu kursi di tengah lapangan luas yang dipenuhi ratusan kursi lipat kosong.",
            "category_id": "silent-reflection",
            "tone": "Kesepian & Keterasingan",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#000000", "#7F8C8D"],
            "aesthetic_tags": ["minimalism", "loneliness", "stark"],
            "sensory_details": {
                "visual_description": "Pria duduk membelakangi kamera di tengah barisan kursi kosong yang sangat banyak.",
                "implied_sound": "Angin kosong berhembus di lapangan luas",
                "implied_season": "Siang hari mendung"
            },
            "story_prompt": "Ketika panggung perayaan telah sepi, siapakah dirimu yang sebenarnya?"
        },
        19: {
            "new_name": "solo-siluet-art-gallery.jpg",
            "title": "Kontemplasi Galeri",
            "description": "Siluet hitam seorang pria berdiri di tengah galeri seni, menatap bingkai foto-foto hitam putih yang dipajang.",
            "category_id": "silent-reflection",
            "tone": "Kontemplatif & Artistik",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#FFFFFF", "#000000", "#E5E5E5"],
            "aesthetic_tags": ["gallery", "museum", "silhouette"],
            "sensory_details": {
                "visual_description": "Pria berdiri membelakangi di galeri seni menatap tiga foto di dinding putih.",
                "implied_sound": "Langkah kaki menggema pelan",
                "implied_season": "Musim dingin"
            },
            "story_prompt": "Melihat kembali lembaran hidup yang dibekukan di dinding kenangan."
        },
        20: {
            "new_name": "detail-kolase-toga-memories.jpg",
            "title": "Kolase Kenangan Wisuda",
            "description": "Kumpulan potongan memori wisuda: detail toga, medali kelulusan, dan foto-foto candid sahabat dalam warna hangat.",
            "category_id": "silent-reflection",
            "tone": "Nostalgia Hangat",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#1A1A1A", "#C39B62", "#4A3B32"],
            "aesthetic_tags": ["collage", "memories", "vintage"],
            "sensory_details": {
                "visual_description": "Kolase berbagai foto detail kelulusan dan potret wisudawan.",
                "implied_sound": "Campuran suara tawa dan jepretan kamera",
                "implied_season": "Sore hari keemasan"
            },
            "story_prompt": "Setiap serpihan foto ini menyimpan cerita perjuangan yang tak ternilai."
        },
        21: {
            "new_name": "detail-kursi-bayangan-jendela.jpg",
            "title": "Cahaya di Ruang Kosong",
            "description": "Cahaya matahari sore menembus celah jendela, memproyeksikan bayangan garis-garis di dinding semen ruang kosong dengan kursi kayu.",
            "category_id": "silent-reflection",
            "tone": "Kesunyian Indah",
            "content_labels": ["Objek"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#8C7B6E", "#D9C3B0", "#2C2C2C"],
            "aesthetic_tags": ["shadows", "empty-room", "nostalgic"],
            "sensory_details": {
                "visual_description": "Kursi kayu di sudut ruangan kosong dengan bayangan jendela di dinding.",
                "implied_sound": "Keheningan total sore hari",
                "implied_season": "Sore hari musim kemarau"
            },
            "story_prompt": "Ruang kelas ini pernah dipenuhi tawa, kini menyisakan sunyi dan cahaya."
        },
        22: {
            "new_name": "solo-ngejar-sarjana-running.jpg",
            "title": "Ngejar Sarjana!",
            "description": "Seorang mahasiswa berlari kencang di lintasan lari mengenakan toga merah berkibar, ekspresi penuh semangat memburu kelulusan.",
            "category_id": "daily-struggle",
            "tone": "Lari & Bersemangat",
            "content_labels": ["Solo"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#C0392B", "#2C3E50", "#BDC3C7"],
            "aesthetic_tags": ["running", "sarjana", "funny"],
            "sensory_details": {
                "visual_description": "Wisudawan berlari di trek atletik biru dengan jubah toga merah terbang.",
                "implied_sound": "Derap langkah kaki cepat dan teriakan semangat",
                "implied_season": "Pagi hari yang cerah"
            },
            "story_prompt": "Berlari sekencang mungkin untuk menyelesaikan babak perjuangan ini."
        },
        23: {
            "new_name": "teman-langkah-dinding-jingga.jpg",
            "title": "Langkah di Dinding Jingga",
            "description": "Dua lulusan melangkah ceria di depan dinding keramik jingga, memadukan formalitas toga dengan pose jenaka.",
            "category_id": "found-family",
            "tone": "Ceria & Hangat",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D35400", "#2C3E50", "#F39C12"],
            "aesthetic_tags": ["friends", "aesthetic", "orange-wall"],
            "sensory_details": {
                "visual_description": "Pria dan wanita bertoga berpose di depan dinding ubin merah bata jingga.",
                "implied_sound": "Canda gurau dua sahabat",
                "implied_season": "Sore hari hangat"
            },
            "story_prompt": "Berjalan bersama melewati batas akhir masa perkuliahan."
        },
        24: {
            "new_name": "solo-bayang-geometris-tinggi.jpg",
            "title": "Bayang-Bayang Kampus",
            "description": "Seorang lulusan berdiri tegak di tengah bayangan struktur kisi-kisi besi raksasa yang terpantul di lapangan semen.",
            "category_id": "silent-reflection",
            "tone": "Tekanan Masa Depan",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#7F8C8D", "#000000", "#FFFFFF"],
            "aesthetic_tags": ["shadows", "minimalist", "geometric"],
            "sensory_details": {
                "visual_description": "Foto high-angle wisudawan berdiri dikelilingi bayangan garis-garis geometris besar.",
                "implied_sound": "Gema langkah kaki pelan",
                "implied_season": "Siang hari terik"
            },
            "story_prompt": "Bayangan masa depan yang membentang lebar di hadapan jalannya."
        },
        25: {
            "new_name": "teman-wajah-balik-buku.jpg",
            "title": "Wajah di Balik Buku",
            "description": "Dua mahasiswa memegang buku terbuka tepat di depan wajah mereka, seolah-olah seluruh identitas mereka telah terserap dalam studi.",
            "category_id": "silent-reflection",
            "tone": "Akademis & Misterius",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2C3E50", "#8E44AD", "#ECF0F1"],
            "aesthetic_tags": ["books", "library", "studying"],
            "sensory_details": {
                "visual_description": "Dua orang bertoga menyembunyikan wajah di balik buku tebal.",
                "implied_sound": "Lembaran buku yang dibalik lambat",
                "implied_season": "Sore hari tenang"
            },
            "story_prompt": "Siapakah kita saat teori-teori buku selesai kita pelajari?"
        },
        26: {
            "new_name": "solo-digital-painting-silhouette-bench.jpg",
            "title": "Kehadiran yang Pudar",
            "description": "Lukisan digital syahdu menggambarkan seseorang yang terduduk sendirian di bangku taman di tepi air, dengan siluet bayangan transparan yang menemaninya secara imajiner.",
            "category_id": "silent-reflection",
            "tone": "Melankolis & Sunyi",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#5A6B7C", "#A2B5CD", "#2C353F"],
            "aesthetic_tags": ["digital-art", "silhouette", "lakeside"],
            "sensory_details": {
                "visual_description": "Lukisan digital bertema biru kelabu menampilkan seseorang di atas bangku kayu dan siluet memudar di sampingnya.",
                "implied_sound": "Suara deburan air dan embusan angin dingin",
                "implied_season": "Musim gugur yang sunyi"
            },
            "story_prompt": "Terkadang ingatan adalah satu-satunya teman yang tersisa di bangku dingin ini."
        },
        27: {
            "new_name": "teman-intip-topi-toga.jpg",
            "title": "Candid di Balik Toga",
            "description": "Toga wisuda diletakkan di pembatas bata, dengan dua pasang mata sahabat mengintip lucu dari sisi kanan dan kiri.",
            "category_id": "found-family",
            "tone": "Ceria & Jenaka",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#8B4513", "#2C3E50", "#FFFFFF"],
            "aesthetic_tags": ["funny-candid", "friends", "playful"],
            "sensory_details": {
                "visual_description": "Dua wajah mahasiswa bertoga mengintip dari balik dinding dengan topi kelulusan di atasnya.",
                "implied_sound": "Bisikan tawa kecil yang ditahan",
                "implied_season": "Siang hari cerah"
            },
            "story_prompt": "Hari kelulusan yang formal selalu memiliki celah untuk tawa jenaka sahabat."
        },
        28: {
            "new_name": "teman-wisudawati-ijazah-phones.jpg",
            "title": "Dibidik Kamera Sahabat",
            "description": "Seorang wisudawati tersenyum manis memegang tabung ijazah, dikelilingi oleh tangan-tangan yang memegang ponsel untuk memotretnya.",
            "category_id": "found-family",
            "tone": "Bangga & Penuh Kasih",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#000000", "#F1C40F", "#ECF0F1"],
            "aesthetic_tags": ["phones", "congratulations", "smile"],
            "sensory_details": {
                "visual_description": "Wisudawati tersenyum di tengah jepretan layar-layar handphone di depannya.",
                "implied_sound": "Suara tawa ramah dan klik kamera handphone",
                "implied_season": "Pagi hari cerah"
            },
            "story_prompt": "Dalam ingatan mereka, hari ini adalah milikmu sepenuhnya."
        },
        29: {
            "new_name": "solo-kebaya-tangga-modern.jpg",
            "title": "Langkah Anggun di Tangga Beton",
            "description": "Potret anggun seorang wisudawati berkebaya dan kain tradisional bertoga berdiri tegak di tangga modern berlatar arsitektur gedung minimalis.",
            "category_id": "silent-reflection",
            "tone": "Elegan & Tenang",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4F5D6B", "#FFFFFF", "#1E252B"],
            "aesthetic_tags": ["kebaya", "staircase", "architecture"],
            "sensory_details": {
                "visual_description": "Wisudawati menatap kamera dengan anggun di railing tangga luar berlatar fasad abu-abu.",
                "implied_sound": "Langkah sepatu di tangga beton",
                "implied_season": "Siang hari sejuk"
            },
            "story_prompt": "Tangga ini membawa langkahnya menuju panggung impian yang telah lama ia bangun."
        },
        30: {
            "new_name": "solo-blur-jalan-taman.jpg",
            "title": "Melangkah Terburu",
            "description": "Efek motion blur menangkap sesosok tubuh berjalan cepat melintasi tanaman rindang di luar gedung kampus saat sore hari.",
            "category_id": "into-the-unknown",
            "tone": "Dinamis & Misterius",
            "content_labels": ["Solo"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#E29B7A", "#2C3E50", "#8D6242"],
            "aesthetic_tags": ["motion-blur", "candid", "walking"],
            "sensory_details": {
                "visual_description": "Siluet buram sesosok pemuda yang melangkah cepat melewati hamparan taman berbunga.",
                "implied_sound": "Desau angin sore dan langkah kaki cepat",
                "implied_season": "Senja hari hangat"
            },
            "story_prompt": "Waktu bergerak cepat, menuntut kita melangkah tanpa pernah menoleh ke belakang."
        },
        31: {
            "new_name": "pasangan-drawing-pegangan-tangan.jpg",
            "title": "Genggaman Tangan Ilustrasi",
            "description": "Seni ilustrasi berbutir pasir (noise texture) yang memperlihatkan sepasang kekasih saling berpegangan erat dengan burung-burung terbang di atas laut luas.",
            "category_id": "silent-reflection",
            "tone": "Romantis & Melankolis",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D6C5B3", "#8C7E74", "#FFFFFF"],
            "aesthetic_tags": ["drawing", "holding-hands", "birds"],
            "sensory_details": {
                "visual_description": "Gambar bertekstur sketsa pasir monokromatik sepasang tangan bergandengan di tepi pantai.",
                "implied_sound": "Kicau camar di kejauhan",
                "implied_season": "Sore hari berangin"
            },
            "story_prompt": "Pegang tanganku, di mana pun batas akhir perjalanan kita nanti."
        },
        32: {
            "new_name": "solo-duduk-tangga-semen-1.jpg",
            "title": "Menanti Riuh Redam",
            "description": "Wisudawan berjas duduk tenang di tangga luar bangunan besar, dikelilingi oleh layout bingkai hijau minimalis.",
            "category_id": "silent-reflection",
            "tone": "Tenang & Kontemplatif",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D5DCD6", "#1E2B22", "#708075"],
            "aesthetic_tags": ["staircase", "green-frame", "candid"],
            "sensory_details": {
                "visual_description": "Pria berjas hitam duduk santai di tangga beton luar dengan panel samping hijau pekat.",
                "implied_sound": "Keheningan siang hari kampus",
                "implied_season": "Siang hari berawan"
            },
            "story_prompt": "Di antara tangga-tangga ini, ia menata kembali mimpi-mimpinya pasca-kelulusan."
        },
        33: {
            "new_name": "solo-duduk-tangga-semen-2.jpg",
            "title": "Sudut Refleksi Diri",
            "description": "Potret kontemplatif yang sama dari mahasiswa berjas di tangga dengan komposisi grafis hijau pekat di sampingnya.",
            "category_id": "silent-reflection",
            "tone": "Tenang & Sunyi",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D5DCD6", "#1E2B22", "#708075"],
            "aesthetic_tags": ["staircase", "candid", "minimalist"],
            "sensory_details": {
                "visual_description": "Pria berjas duduk santai di tangga beton luar dengan panel samping hijau pekat.",
                "implied_sound": "Suara embusan angin pelan",
                "implied_season": "Siang hari berawan"
            },
            "story_prompt": "Beristirahat sejenak dari riuhnya pesta wisuda di luar sana."
        },
        34: {
            "new_name": "keluarga-batik-kebaya-balkon.jpg",
            "title": "Batik dan Kebaya Bangga",
            "description": "Sepasang orang tua mengenakan batik dan kebaya tradisional berdiri di balkon kampus, menatap penuh kebanggaan pada kelulusan anak mereka.",
            "category_id": "found-family",
            "tone": "Kehangatan Keluarga",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4E3629", "#D7CCC8", "#3E2723"],
            "aesthetic_tags": ["parents", "batik", "family"],
            "sensory_details": {
                "visual_description": "Kedua orang tua tersenyum di balkon bangunan kolonial kampus.",
                "implied_sound": "Bisikan bangga sang ayah pada ibunya",
                "implied_season": "Siang hari sejuk"
            },
            "story_prompt": "Gelar ini adalah milik mereka yang mendoakanmu tanpa putus."
        },
        35: {
            "new_name": "solo-skripsi-koran-siluet.jpg",
            "title": "Tenggelam dalam Lembaran Teori",
            "description": "Kolase artistik siluet manusia di tengah kolom koran/buku tebal, melambangkan perjuangan membaca skripsi tak berkesudahan.",
            "category_id": "daily-struggle",
            "tone": "Tertekan & Akademis",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#FFFFFF", "#000000", "#7F8C8D"],
            "aesthetic_tags": ["newspaper", "collage", "existential"],
            "sensory_details": {
                "visual_description": "Siluet hitam manusia berjalan di atas halaman koran B&W penuh tulisan padat.",
                "implied_sound": "Kertas koran yang robek perlahan",
                "implied_season": "Malam hari suntuk"
            },
            "story_prompt": "Menjadi satu titik kecil di tengah gunungan kata dan teori."
        },
        36: {
            "new_name": "solo-kursi-pantai-sunyi.jpg",
            "title": "Dialog dalam Sepi",
            "description": "Dua kursi kayu di tepi pantai berkabut, salah satunya diduduki oleh sosok misterius berkerudung gelap yang menatap laut lepas.",
            "category_id": "silent-reflection",
            "tone": "Dingin & Hampa",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#E8E8E8", "#2F3E46", "#84A59D"],
            "aesthetic_tags": ["beach-chairs", "foggy", "hooded-figure"],
            "sensory_details": {
                "visual_description": "Foto minimalis dua kursi lipat di atas pasir abu-abu berlatar laut yang tertutup kabut tebal.",
                "implied_sound": "Deburan ombak dingin yang lambat dan sunyi",
                "implied_season": "Musim dingin basah"
            },
            "story_prompt": "Satu kursi kosong untuk jawaban yang tak pernah kembali ke pantai ini."
        },
        37: {
            "new_name": "solo-pegang-hp-depan-muka.jpg",
            "title": "Layar Wajah Ganda",
            "description": "Seorang wisudawati berpose di aula wisuda, menutupi wajahnya dengan smartphone yang menampilkan foto close-up wajahnya sendiri.",
            "category_id": "daily-struggle",
            "tone": "Kreatif & Main-main",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#7B1E26", "#F5EBE6", "#1E1E1E"],
            "aesthetic_tags": ["smartphone-pose", "toga", "creative-candid"],
            "sensory_details": {
                "visual_description": "Wisudawati memegang HP tepat di depan wajahnya yang menampilkan gambar potret mukanya sendiri.",
                "implied_sound": "Riuh obrolan wisuda di aula tertutup",
                "implied_season": "Siang hari hangat"
            },
            "story_prompt": "Identitas digital kita terkadang lebih nyata daripada wajah asli kita."
        },
        38: {
            "new_name": "solo-lorong-jembatan-siluet.jpg",
            "title": "Langkah di Bawah Jembatan",
            "description": "Foto high-contrast bayangan beton jalan layang/jembatan besar, menyisakan seberkas cahaya vertikal di mana sesosok manusia berjalan kecil di dasarnya.",
            "category_id": "into-the-unknown",
            "tone": "Eksistensial & Kontras",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#D9CDBF", "#5C5449"],
            "aesthetic_tags": ["underpass", "light-beam", "shadows"],
            "sensory_details": {
                "visual_description": "Kontras tinggi bayangan struktur beton besar dengan siluet orang berjalan di bawah celah sinar matahari.",
                "implied_sound": "Deru mesin kendaraan samar dari atas jalan layang",
                "implied_season": "Siang hari terik"
            },
            "story_prompt": "Berjalan menyusuri labirin beton kota, mencari ke mana berkas cahaya menuntun."
        },
        39: {
            "new_name": "detail-kartu-palet-warna.jpg",
            "title": "Palet Warna Kenangan",
            "description": "Flatlay kartu palet warna bernuansa hangat musim gugur (Linen, Weathered, Cafe Noir, Latte, Cedar, Mauve) yang melambangkan keindahan visual memori wisuda.",
            "category_id": "silent-reflection",
            "tone": "Estetik & Kalem",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#725B3E", "#A88670", "#44222D"],
            "aesthetic_tags": ["color-palette", "cards", "aesthetic"],
            "sensory_details": {
                "visual_description": "Delapan kartu palet warna diletakkan rapi di atas latar belakang foto alam bernuansa sendu.",
                "implied_sound": "Hening yang damai",
                "implied_season": "Sore hari tenang"
            },
            "story_prompt": "Setiap memori di kampus ini dicat dengan palet warna hangat yang tak akan pudar."
        },
        40: {
            "new_name": "pasangan-siluet-cahaya-pohon.jpg",
            "title": "Bayangan di Sisi Pohon",
            "description": "Seorang pemuda berpakaian putih bersandar pada pohon besar di hutan berkabut, menatap siluet cahaya putih benderang sesosok manusia di hadapannya.",
            "category_id": "silent-reflection",
            "tone": "Misterius & Fantasi",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#3B4E38", "#FFFFFF", "#2F352E"],
            "aesthetic_tags": ["nature", "glowing-silhouette", "foggy-woods"],
            "sensory_details": {
                "visual_description": "Pemuda berbaju putih bersandar di pohon besar menghadap siluet cahaya wanita di tengah kabut hijau hutan.",
                "implied_sound": "Kicau jangkrik hutan and keheningan misterius",
                "implied_season": "Pagi hari dingin berkabut"
            },
            "story_prompt": "Apakah dia nyata atau hanya ingatan yang membayangi jalan sunyi ini?"
        },
        41: {
            "new_name": "pasangan-siluet-cahaya-padang-rumput.jpg",
            "title": "Pertemuan di Ujung Padang",
            "description": "Seorang pemuda duduk di padang rumput hijau menatap siluet cahaya putih benderang sesosok wanita di sampingnya di bawah langit mendung.",
            "category_id": "silent-reflection",
            "tone": "Surealis & Tenang",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4F6D4F", "#DCDCDC", "#2F3E2F"],
            "aesthetic_tags": ["meadow", "glowing-silhouette", "cloudy-sky"],
            "sensory_details": {
                "visual_description": "Pria berambut gelap duduk membelakangi kamera di rumput hijau tinggi di samping siluet putih bersinar.",
                "implied_sound": "Desau angin rumput bergoyang",
                "implied_season": "Sore hari mendung"
            },
            "story_prompt": "Di padang sepi ini, batas antara ingatan dan kenyataan memudar."
        },
        42: {
            "new_name": "solo-siluet-cahaya-hutan.jpg",
            "title": "Gadis Cahaya di Jalan Setapak",
            "description": "Siluet putih benderang sesosok wanita berjalan menyusuri jalan setapak di tengah hutan pinus yang sunyi.",
            "category_id": "into-the-unknown",
            "tone": "Surealis & Melankolis",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#8C6B50", "#FFFFFF", "#4A3525"],
            "aesthetic_tags": ["silhouette-walk", "forest-path", "glowing"],
            "sensory_details": {
                "visual_description": "Siluet manusia bersinar putih berdiri di atas jalan tanah cokelat dikelilingi batang pohon pinus kabur.",
                "implied_sound": "Langkah kaki di atas daun kering yang patah",
                "implied_season": "Musim gugur dingin"
            },
            "story_prompt": "Ia berjalan sendirian membawa seberkas cahaya menembus kegelapan belantara."
        },
        43: {
            "new_name": "solo-kebaya-putih-blur-candi.jpg",
            "title": "Membeku di Gerbang Masa Lalu",
            "description": "Seorang wisudawati cantik mengenakan kebaya putih berpose dengan latar belakang bangunan kolonial kampus/candi yang sengaja dibuat blur lembut.",
            "category_id": "bittersweet-farewell",
            "tone": "Lembut & Nostalgik",
            "content_labels": ["Solo"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#FFFFFF", "#8C7A6B", "#DFD5C6"],
            "aesthetic_tags": ["portrait-wisuda", "soft-focus", "heritage-building"],
            "sensory_details": {
                "visual_description": "Wisudawati tersenyum manis membelakangi bangunan pilar megah bergaya kolonial yang kabur.",
                "implied_sound": "Sorak wisudawan di kejauhan yang diredam angin",
                "implied_season": "Pagi hari yang hangat"
            },
            "story_prompt": "Masa lalu membeku di belakangnya, sementara fajar baru menanti di depan matanya."
        },
        44: {
            "new_name": "solo-high-angle-lantai-putih.jpg",
            "title": "Titik Kecil Eksistensi",
            "description": "Foto high-angle hitam putih berjarak jauh menampilkan seorang mahasiswa bertoga yang berdiri sendirian di atas lantai ubin putih luas yang bersih.",
            "category_id": "silent-reflection",
            "tone": "Kesepian & Stark",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#000000", "#808080"],
            "aesthetic_tags": ["minimalism", "black-white", "high-angle"],
            "sensory_details": {
                "visual_description": "Satu orang bertoga kecil di tengah pola garis-garis ubin putih berukuran besar.",
                "implied_sound": "Gema langkah sepatu tunggal",
                "implied_season": "Siang hari mendung"
            },
            "story_prompt": "Di tengah dunia yang luas dan kosong, ia adalah pencari jalannya sendiri."
        },
        45: {
            "new_name": "detail-ksatria-mawar-kuning.jpg",
            "title": "Ksatria dan Mawar Kuning",
            "description": "Ilustrasi ksatria berbaju besi memegang mawar kuning dengan tulisan '괜찮아요' (Tidak apa-apa), sebuah pesan bertahan di tengah badai.",
            "category_id": "daily-struggle",
            "tone": "Harapan di Tengah Badai",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2C3E50", "#F1C40F", "#7F8C8D"],
            "aesthetic_tags": ["knight", "illustration", "hope"],
            "sensory_details": {
                "visual_description": "Ksatria berzirah mengangkat mawar kuning dengan tulisan Korea di sampingnya.",
                "implied_sound": "Petikan kecapi yang lembut dan sunyi",
                "implied_season": "Musim dingin berakhir"
            },
            "story_prompt": "Ksatria terkuat adalah dia yang mampu menjaga kelembutan di balik zirahnya."
        },
        46: {
            "new_name": "detail-arsitektur-gedung-putih.jpg",
            "title": "Geometri Fasad Kampus",
            "description": "Fasad bangunan kampus minimalis berwarna putih abu-abu dengan jendela-jendela hitam teratur, menyiratkan kebosanan perkuliahan harian.",
            "category_id": "silent-reflection",
            "tone": "Monoton & Melankolis",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#EBEBEB", "#2B2B2B", "#8C8C8C"],
            "aesthetic_tags": ["architecture", "minimalist", "facade"],
            "sensory_details": {
                "visual_description": "Bagian samping gedung beton putih bergaya modern fungsional dengan deretan jendela kotak hitam.",
                "implied_sound": "Dengung kipas angin kelas di kejauhan",
                "implied_season": "Siang hari berawan kelabu"
            },
            "story_prompt": "Dinding-dinding dingin ini telah menjadi saksi dari ribuan teori yang diujikan."
        },
        47: {
            "new_name": "detail-kertas-siluet-why-am-i-here.jpg",
            "title": "Mengapa Aku Di Sini?",
            "description": "Potongan kertas berbentuk siluet manusia berdiri di rumput dekat danau, bertuliskan coretan spidol 'WHY AM I HERE?' yang menggambarkan krisis eksistensial mahasiswa tingkat akhir.",
            "category_id": "daily-struggle",
            "tone": "Bingung & Krisis Eksistensi",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4F6B7E", "#FFFFFF", "#2A3C2A"],
            "aesthetic_tags": ["cutout-paper", "philosophical", "lakeside"],
            "sensory_details": {
                "visual_description": "Kertas putih berbentuk orang dengan tulisan bahasa Inggris diletakkan di rumput dengan latar belakang riak danau.",
                "implied_sound": "Suara gemercik air danau ditiup angin sepoi",
                "implied_season": "Sore hari sejuk"
            },
            "story_prompt": "Pertanyaan sederhana yang selalu mengetuk kepala di tengah-tengah kuliah teori yang rumit."
        },
        48: {
            "new_name": "solo-wisuda-outdoor-ac.jpg",
            "title": "Realitas dan Kebanggaan",
            "description": "Seorang lulusan membelakangi kamera dengan selempang merah gelar kelulusannya, berdiri di samping kompresor AC outdoor, menunjukkan humor kontras wisuda.",
            "category_id": "daily-struggle",
            "tone": "Satir & Humor Realitas",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#7E191B", "#1C1C1C"],
            "aesthetic_tags": ["funny-candid", "grad-sash", "outdoor-ac"],
            "sensory_details": {
                "visual_description": "Foto membelakangi seorang pria bercelana hitam berselempang merah di samping mesin AC outdoor putih di luar ruangan.",
                "implied_sound": "Dengung bising mesin AC outdoor",
                "implied_season": "Siang hari panas menyengat"
            },
            "story_prompt": "Di balik gelar yang megah, perjuangan mahasiswa sering kali sekompleks merawat mesin pendingin."
        },
        49: {
            "new_name": "solo-belajar-meja-buku-bw-1.jpg",
            "title": "Begadang Revisi",
            "description": "Potret hitam putih dramatis seorang mahasiswa memegang keningnya dengan lelah di meja belajar yang dipenuhi tumpukan buku skripsi.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Tertekan",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#555555"],
            "aesthetic_tags": ["black-white", "studying-hard", "night-revision"],
            "sensory_details": {
                "visual_description": "Mahasiswa menunduk memegang kepala di depan buku terbuka dengan secangkir kopi di sampingnya.",
                "implied_sound": "Hening malam diselingi coretan pulpen di kertas",
                "implied_season": "Dini hari sunyi"
            },
            "story_prompt": "Hanya secangkir kopi dingin dan tumpukan kertas yang menemaninya melewati malam penentuan ini."
        },
        50: {
            "new_name": "solo-belajar-meja-buku-bw-2.jpg",
            "title": "Ujung dari Kesabaran",
            "description": "Refleksi kontemplatif monokromatik dari perjuangan malam hari seorang mahasiswa dalam menyelesaikan revisi skripsi.",
            "category_id": "daily-struggle",
            "tone": "Lelah & Fokus",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#555555"],
            "aesthetic_tags": ["black-white", "exhausted", "library"],
            "sensory_details": {
                "visual_description": "Mahasiswa menunduk memegang kepala di depan buku terbuka dengan secangkir kopi di sampingnya.",
                "implied_sound": "Detak jam dinding yang lambat",
                "implied_season": "Larut malam"
            },
            "story_prompt": "Setiap halaman yang ia balik adalah satu langkah lebih dekat menuju pembebasan."
        },
        51: {
            "new_name": "solo-wisuda-segitiga-bingkai.jpg",
            "title": "Bingkai Perspektif Baru",
            "description": "Seorang lulusan berjas hitam berdiri bersandar di balkon semen kampus, dipotret secara artistik melalui bingkai berbentuk segitiga arsitektur bangunan.",
            "category_id": "silent-reflection",
            "tone": "Artistik & Kontemplatif",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#DCDCD9", "#2A2A2B", "#8C8C8A"],
            "aesthetic_tags": ["framing-composition", "architecture", "graduation-suit"],
            "sensory_details": {
                "visual_description": "Pria berjas hitam berdiri menengadah di koridor beton dilihat dari celah semen berbentuk segitiga.",
                "implied_sound": "Gema obrolan di kejauhan bangunan",
                "implied_season": "Siang hari berangin"
            },
            "story_prompt": "Dari sudut pandang ini, semua jalan menuju masa depan terlihat lebih menantang."
        },
        52: {
            "new_name": "solo-menatap-laut-kacamata-bw.jpg",
            "title": "Cakrawala Pikiran",
            "description": "Potret hitam putih dari samping seorang mahasiswa berkacamata yang menatap laut lepas berlatar awan mendung, memikirkan kelanjutan hidup pasca-lulus.",
            "category_id": "into-the-unknown",
            "tone": "Nostalgik & Syahdu",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#000000", "#FFFFFF", "#7F8C8D"],
            "aesthetic_tags": ["black-white", "seaside", "contemplative"],
            "sensory_details": {
                "visual_description": "Potret siluet profil samping pemuda berkacamata menatap ke arah laut luas.",
                "implied_sound": "Deru angin laut dan deburan ombak samar",
                "implied_season": "Sore hari mendung dingin"
            },
            "story_prompt": "Di ujung cakrawala sana, kota baru dengan impian baru menantinya untuk berlabuh."
        },
        53: {
            "new_name": "pasangan-siluet-senja.jpg",
            "title": "Senja Dua Jiwa",
            "description": "Sepasang kekasih berdiri berdekatan saat matahari terbenam keemasan, di mana sang wanita berpendar cahaya putih seperti ingatan yang indah.",
            "category_id": "silent-reflection",
            "tone": "Romantis & Hangat",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#F39C12", "#D35400", "#FFFFFF"],
            "aesthetic_tags": ["sunset", "silhouette", "glowing-soul"],
            "sensory_details": {
                "visual_description": "Pria bersandar di sisi wanita bercahaya putih benderang saat senja kuning keemasan di atas perbukitan.",
                "implied_sound": "Hening senja dan hembusan angin hangat",
                "implied_season": "Senja musim kemarau"
            },
            "story_prompt": "Saat matahari tenggelam, bayanganmu adalah satu-satunya hal hangat yang enggan kulepaskan."
        },
        54: {
            "new_name": "solo-kursi-kosong-laut.jpg",
            "title": "Membasuh Sunyi",
            "description": "Sesosok orang duduk di kursi kayu di tengah genangan air laut dangkal berkabut, menatap kursi kayu kosong di sampingnya.",
            "category_id": "silent-reflection",
            "tone": "Sunyi & Hampa",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#E5ECE9", "#5C6B73", "#93A8AC"],
            "aesthetic_tags": ["sea-chairs", "foggy", "surrealism"],
            "sensory_details": {
                "visual_description": "Seseorang menunduk duduk di kursi di dalam air laut datar berlatar langit putih bersih disandingkan kursi kosong.",
                "implied_sound": "Aliran air tenang menyentuh kaki kursi",
                "implied_season": "Pagi hari dingin"
            },
            "story_prompt": "Kursi itu diletakkan di sana untuk harapan yang tenggelam di dasar samudra kenangan."
        },
        55: {
            "new_name": "detail-symbol-berserk-merah.jpg",
            "title": "Segel Pengorbanan",
            "description": "Ilustrasi simbol 'Brand of Sacrifice' berwarna merah darah yang menetes di atas latar belakang hitam kelam, lambang perjuangan keras tanpa kenal menyerah.",
            "category_id": "daily-struggle",
            "tone": "Perjuangan Keras & Dark",
            "content_labels": ["Objek"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FF0000", "#3E0000"],
            "aesthetic_tags": ["berserk", "illustration", "blood-red"],
            "sensory_details": {
                "visual_description": "Lambang anime Berserk berwarna merah menyala dengan tetesan cat di latar belakang hitam pekat.",
                "implied_sound": "Derau angin malam yang mencekam",
                "implied_season": "Malam hari kelam"
            },
            "story_prompt": "Menanggung beban tanda ini di pundak kita, terus berjuang di tengah badai skripsi yang tak berujung."
        },
        56: {
            "new_name": "keluarga-collage-wisuda.jpg",
            "title": "Restu Ayah Ibu",
            "description": "Kolase foto kehangatan wisuda: orang tua memasangkan toga pada sang anak (atas), dan potret bangga bertiga di depan gedung kampus (bawah).",
            "category_id": "found-family",
            "tone": "Bangga & Penuh Haru",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#CBA370", "#ECE5DB", "#4A3E31"],
            "aesthetic_tags": ["family-love", "graduation-day", "parents"],
            "sensory_details": {
                "visual_description": "Kolase dua foto menampilkan momen pemasangan topi toga oleh orang tua dan foto pose bersama.",
                "implied_sound": "Suara tangis haru ibu dan bisikan selamat sang ayah",
                "implied_season": "Pagi hari wisuda yang cerah"
            },
            "story_prompt": "Senyuman mereka adalah pencapaian terbesar dari lembaran toga yang kupakai hari ini."
        },
        57: {
            "new_name": "teman-berlari-koridor-sekolah.jpg",
            "title": "Berlari Menyambut Kebebasan",
            "description": "Potret hitam putih buram menunjukkan para siswa berlari riang di koridor sekolah tua, seolah menyambut hari terakhir kelas.",
            "category_id": "found-family",
            "tone": "Nostalgia Ceria",
            "content_labels": ["Teman"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#7F8C8D", "#FFFFFF", "#2C3E50"],
            "aesthetic_tags": ["running", "candid", "coming-of-age"],
            "sensory_details": {
                "visual_description": "Foto motion-blur hitam putih siswa berseragam berlari di koridor sekolah berasitektur kolonial.",
                "implied_sound": "Suara langkah kaki riuh dan tawa lepas",
                "implied_season": "Sore hari musim panas"
            },
            "story_prompt": "Saat lonceng terakhir berbunyi, kita tahu kita tak akan kembali ke lorong ini dengan cara yang sama."
        },
        58: {
            "new_name": "solo-menatap-danau-kapal-bw.jpg",
            "title": "Dermaga Harapan",
            "description": "Foto monokrom membelakangi kamera seorang mahasiswa menatap permukaan danau yang tenang dengan beberapa kapal bersandar.",
            "category_id": "silent-reflection",
            "tone": "Sunyi & Tenang",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#000000", "#FFFFFF", "#8A8A8A"],
            "aesthetic_tags": ["lakeside", "monochrome", "boats"],
            "sensory_details": {
                "visual_description": "Pria berambut gelap membelakangi kamera di tepi air menatap jajaran perahu layar kecil.",
                "implied_sound": "Riak air tenang memukul tepian dermaga",
                "implied_season": "Sore hari sejuk mendung"
            },
            "story_prompt": "Kapal-kapal ini menanti pelayaran baru, sama seperti jiwanya yang siap bertualang ke kota asing."
        },
        59: {
            "new_name": "solo-tracking-bukit-hijau.jpg",
            "title": "Langkah Menembus Lembah",
            "description": "Seorang mahasiswa memakai topi berjalan menyusuri jalan setapak di tengah perbukitan hijau yang luas di bawah langit berawan.",
            "category_id": "into-the-unknown",
            "tone": "Petualangan & Kebebasan",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#6A8D56", "#E8ECE9", "#455E38"],
            "aesthetic_tags": ["hiking", "green-hills", "nature-walk"],
            "sensory_details": {
                "visual_description": "Seorang pemuda beransel berjalan di jalan setapak perbukitan hijau dikelilingi pepohonan di bawah awan putih.",
                "implied_sound": "Kicau burung liar dan gemerisik rerumputan padang",
                "implied_season": "Pagi hari musim semi yang cerah"
            },
            "story_prompt": "Tinggalkan kota dan teori sejenak, biarkan alam mengajarkan cara melangkah tanpa beban."
        },
        60: {
            "new_name": "solo-jalan-blur-wisuda-bw.jpg",
            "title": "Fokus di Tengah Riuh",
            "description": "Potret hitam putih seorang wisudawan bertoga berdiri diam di tengah koridor, sementara orang-orang di sekelilingnya melintas cepat dengan efek motion blur.",
            "category_id": "silent-reflection",
            "tone": "Fokus & Kontemplatif",
            "content_labels": ["Solo"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#000000", "#FFFFFF", "#7F7F7F"],
            "aesthetic_tags": ["black-white", "motion-blur", "focus"],
            "sensory_details": {
                "visual_description": "Wisudawan dengan medali berdiri tegak di tengah lorong beton sementara siluet orang lain buram berjalan cepat.",
                "implied_sound": "Gema riuh langkah orang banyak yang teredam di telinga",
                "implied_season": "Pagi hari wisuda"
            },
            "story_prompt": "Ketika semua orang bergegas merayakan kelulusan, ia terdiam memikirkan arti perpisahan ini."
        },
        61: {
            "new_name": "solo-jalan-blur-wisuda-bw-dup.jpg",
            "title": "Fokus di Tengah Riuh (Detail)",
            "description": "Potret monokromatik wisudawan bertoga berdiri di tengah keramaian kampus yang bergerak cepat dengan efek motion blur.",
            "category_id": "silent-reflection",
            "tone": "Fokus & Sunyi",
            "content_labels": ["Solo"],
            "technique_labels": ["Blur"],
            "dominant_colors": ["#000000", "#FFFFFF", "#7F7F7F"],
            "aesthetic_tags": ["black-white", "motion-blur", "candid"],
            "sensory_details": {
                "visual_description": "Wisudawan berdiri tegak di tengah lorong beton sementara siluet orang lain buram berjalan cepat.",
                "implied_sound": "Langkah kaki terburu-buru yang menggema",
                "implied_season": "Pagi hari wisuda"
            },
            "story_prompt": "Di tengah dunia yang bergerak cepat, carilah tempat hening di dalam jiwamu."
        },
        62: {
            "new_name": "solo-duduk-railing-tangga-hitam.jpg",
            "title": "Sudut Sepi Tangga Kampus",
            "description": "Sesosok orang berpakaian hitam bersandar lesu di railing tangga semen di dalam gedung kampus yang sepi.",
            "category_id": "silent-reflection",
            "tone": "Sepi & Melankolis",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#E8E8E8", "#2C3E50", "#7F8C8D"],
            "aesthetic_tags": ["staircase", "indoor", "lonely"],
            "sensory_details": {
                "visual_description": "Seseorang berbaju gelap duduk di atas anak tangga semen di dekat pagar pengaman besi putih.",
                "implied_sound": "Langkah kaki menjauh di koridor atas",
                "implied_season": "Sore hari sunyi"
            },
            "story_prompt": "Sudut tangga ini menyimpan sisa keluh kesah sebelum ujian akhir dimulai."
        },
        63: {
            "new_name": "detail-flatlay-atribut-wisuda.jpg",
            "title": "Atribut Kelulusan di Atas Rumput",
            "description": "Flatlay estetik di atas rumput hijau menampilkan selempang wisuda bertuliskan nama kelulusan, ijazah bersampul merah, dan medali emas wisuda.",
            "category_id": "bittersweet-farewell",
            "tone": "Bangga & Nostalgik",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#27ae60", "#c0392b", "#FFFFFF"],
            "aesthetic_tags": ["flatlay", "graduation-sash", "medal"],
            "sensory_details": {
                "visual_description": "Selempang hitam bertuliskan 'Dewi Sastriyani' diletakkan di atas rumput bersama map ijazah merah.",
                "implied_sound": "Bisikan angin sore di lapangan rumput kampus",
                "implied_season": "Sore hari cerah"
            },
            "story_prompt": "Benda-benda ini adalah bukti bisu dari perjuangan malam-malam panjang skripsi."
        },
        64: {
            "new_name": "solo-jalan-koridor-low-angle.jpg",
            "title": "Menembus Lorong Kampus",
            "description": "Potret low-angle seorang wisudawan memegang ijazah melangkah percaya diri di lorong beton kampus bergaya arsitektur modern.",
            "category_id": "into-the-unknown",
            "tone": "Bangga & Percaya Diri",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D5DCD6", "#2C3E50", "#708075"],
            "aesthetic_tags": ["low-angle", "walking-candid", "corridor"],
            "sensory_details": {
                "visual_description": "Wisudawan berjas memegang ijazah berjalan di bawah atap beton miring gedung modern.",
                "implied_sound": "Langkah tegap bergema di bawah beton",
                "implied_season": "Siang hari berawan"
            },
            "story_prompt": "Melangkah menembus batas akhir kampus, bersiap menaklukkan tantangan dunia luar."
        },
        65: {
            "new_name": "keluarga-candid-kacamata-jari.jpg",
            "title": "Kacamata Jenaka Sahabat",
            "description": "Keluarga dan wisudawan berpose kocak dengan membuat bentuk kacamata menggunakan jari mereka, meluluhkan suasana formal.",
            "category_id": "found-family",
            "tone": "Humor & Hangat",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4A3B32", "#F5EBE6", "#1E1E1E"],
            "aesthetic_tags": ["funny-pose", "family", "candid"],
            "sensory_details": {
                "visual_description": "Keluarga tersenyum lebar dengan pose tangan membentuk kacamata di depan mata mereka.",
                "implied_sound": "Tawa renyah bersama di studio",
                "implied_season": "Siang hari cerah"
            },
            "story_prompt": "Karena kelulusan terbaik dirayakan dengan tawa lepas bersama keluarga."
        },
        66: {
            "new_name": "solo-close-up-selempang.jpg",
            "title": "Potret Kebanggaan Almamater",
            "description": "Foto potret setengah badan seorang pemuda mengenakan jas wisuda dan selempang kelulusan putih di depan pilar gedung megah bergaya kolonial.",
            "category_id": "found-family",
            "tone": "Elegan & Bangga",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#ECEFF1", "#2C3E50", "#37474F"],
            "aesthetic_tags": ["portrait-wisuda", "graduation-sash", "classical-building"],
            "sensory_details": {
                "visual_description": "Pemuda berambut cokelat dengan setelan jas biru berselempang putih berdiri tegak di depan tiang pilar marmer putih.",
                "implied_sound": "Sorakan ucapan selamat di sekitar halaman studio",
                "implied_season": "Pagi hari cerah"
            },
            "story_prompt": "Gelar di pundak ini adalah janji awal untuk mengabdi pada kebaikan."
        },
        67: {
            "new_name": "pasangan-close-up-mata.jpg",
            "title": "Tatapan Kedekatan",
            "description": "Foto ekstrem close-up yang memotong wajah sepasang kekasih, memfokuskan pada pancaran sepasang mata mereka yang bersanding erat.",
            "category_id": "silent-reflection",
            "tone": "Intim & Romantis",
            "content_labels": ["Pasangan"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D5C5B5", "#2C1C12", "#D35400"],
            "aesthetic_tags": ["extreme-close-up", "eyes", "intimate"],
            "sensory_details": {
                "visual_description": "Dua mata bersanding sejajar dalam potongan foto potret dekat berwarna hangat jingga keemasan.",
                "implied_sound": "Helaan napas tenang dan hening",
                "implied_season": "Sore hari hangat"
            },
            "story_prompt": "Di dalam matamu, aku menemukan rumah tempat semua perjuangan perkuliahan ini berakhir dengan damai."
        },
        68: {
            "new_name": "keluarga-wisuda-berjalan-putih.jpg",
            "title": "Langkah Restu Putih",
            "description": "Seorang lulusan berjalan di antara ayah dan ibunya yang mengenakan busana muslim kebaya serba putih bersih di halaman depan gedung kampus tua.",
            "category_id": "found-family",
            "tone": "Penuh Restu & Hangat",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#FFFFFF", "#7F8C8D", "#1E1E1E"],
            "aesthetic_tags": ["parents-walk", "white-kebaya", "graduation-day"],
            "sensory_details": {
                "visual_description": "Wisudawan bertoga berjalan diapit orang tuanya yang tersenyum mengenakan batik dan kebaya serba putih.",
                "implied_sound": "Langkah kaki santai dan tawa ramah di jalan beraspal",
                "implied_season": "Pagi hari yang sejuk"
            },
            "story_prompt": "Setiap langkah kaki hari ini terasa ringan karena restu tulus yang mengiringi di kanan kiri."
        },
        69: {
            "new_name": "keluarga-dinding-merah-collage.jpg",
            "title": "Dinding Kenangan Keluarga",
            "description": "Kolase foto menampilkan potret wisudawan bersandar di dinding semen kelabu (atas) dan foto keluarga ceria berpose di depan dinding merah bata (bawah).",
            "category_id": "found-family",
            "tone": "Ceria & Hangat",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#C0392B", "#ECEFF1", "#2C3E50"],
            "aesthetic_tags": ["collage", "red-wall", "family-pose"],
            "sensory_details": {
                "visual_description": "Kolase foto wisudawan berjas bersandar di sudut beton minimalis dan foto berempat di balik pagar bata merah.",
                "implied_sound": "Suara tawa lepas empat orang",
                "implied_season": "Sore hari cerah"
            },
            "story_prompt": "Bersama mereka, dinding dingin kampus terasa hangat dan penuh warna."
        },
        70: {
            "new_name": "solo-jas-hijau-dasi.jpg",
            "title": "Gaya Setelan Klasik",
            "description": "Foto detail setelan jas berwarna hijau tua dengan kemeja putih, dasi garis-garis cokelat, dan kacamata bertengger di saku, lambang akademisi muda.",
            "category_id": "silent-reflection",
            "tone": "Formal & Klasik",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2D4A3E", "#D5C8B8", "#1E2A24"],
            "aesthetic_tags": ["suit-detail", "green-blazer", "gentleman-style"],
            "sensory_details": {
                "visual_description": "Potret close-up setelan blazer hijau tua bertekstur kasar dengan dasi bergaris dan kacamata di saku dada.",
                "implied_sound": "Hening tenang ruangan tertutup",
                "implied_season": "Siang hari sejuk"
            },
            "story_prompt": "Pakaian ini adalah zirah baru untuk pertempuran di dunia profesional pasca-kampus."
        },
        71: {
            "new_name": "solo-angkat-topi-toga-membelakangi.jpg",
            "title": "Hormat Terakhir Kampus",
            "description": "Seorang wisudawan membelakangi kamera berjalan di jalan setapak kampus, tangan kanannya mengangkat tinggi topi toga kelulusannya menyambut langit biru.",
            "category_id": "into-the-unknown",
            "tone": "Kebebasan & Harapan",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#4A1E20", "#ECEFF1", "#3E543B"],
            "aesthetic_tags": ["toga-raise", "back-view", "campus-garden"],
            "sensory_details": {
                "visual_description": "Lulusan membelakangi kamera mengangkat topi toga merah marunnya di tengah taman rindang kampus.",
                "implied_sound": "Desau angin dedaunan dan teriakan bebas wisudawan",
                "implied_season": "Siang hari cerah berawan"
            },
            "story_prompt": "Terima kasih untuk segalanya. Aku pamit untuk melangkah lebih jauh."
        },
        72: {
            "new_name": "teman-dinding-semen-hydrant.jpg",
            "title": "Persahabatan di Sudut Hydrant",
            "description": "Kolase foto persahabatan menampilkan kelompok wisudawan berpose santai di dekat kotak hydrant merah menyala di dinding semen abu-abu.",
            "category_id": "found-family",
            "tone": "Kompak & Ceria",
            "content_labels": ["Teman"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#C0392B", "#7F8C8D", "#FFFFFF"],
            "aesthetic_tags": ["collage", "hydrant-box", "friends-candid"],
            "sensory_details": {
                "visual_description": "Kolase dua foto menampilkan sahabat bertoga berpose santai di atas tembok pembatas semen dekat kotak hydrant.",
                "implied_sound": "Tawa renyah sekelompok sahabat bertukar cerita",
                "implied_season": "Siang hari cerah"
            },
            "story_prompt": "Kotak hydrant ini berwarna merah menyala, persis seperti semangat persahabatan kita yang tak padam ditiup angin perpisahan."
        },
        73: {
            "new_name": "solo-collage-shadow-dark.jpg",
            "title": "Bayangan Kesunyian Kampus",
            "description": "Kolase foto dramatis menampilkan bayangan panjang pilar bangunan di atas lantai semen luas di mana seorang mahasiswa berjalan melintas sendirian.",
            "category_id": "silent-reflection",
            "tone": "Misterius & Eksistensial",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#7F8C8D", "#FFFFFF"],
            "aesthetic_tags": ["collage", "shadows", "architectural-lines"],
            "sensory_details": {
                "visual_description": "Kolase tiga foto bayangan garis-garis pilar beton panjang berlatar siluet orang berjalan.",
                "implied_sound": "Langkah kaki menggema lambat di lorong beton",
                "implied_season": "Sore hari sunyi"
            },
            "story_prompt": "Dalam bayang-bayang ini, aku menata kembali semua teori yang pernah kupelajari."
        },
        74: {
            "new_name": "keluarga-rapikan-kebaya-wisudawati.jpg",
            "title": "Detail Kasih Sayang Ibu",
            "description": "Momen penuh kasih saat ibu merapikan kalung medali wisuda di leher anak perempuannya yang tersenyum cantik mengenakan kebaya.",
            "category_id": "found-family",
            "tone": "Lembut & Penuh Kasih",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#ECE9E2", "#F1C40F", "#4A3E3D"],
            "aesthetic_tags": ["mother-touch", "kebaya-detail", "love"],
            "sensory_details": {
                "visual_description": "Ibu tersenyum bangga membetulkan kalung wisuda anak perempuannya yang mengenakan kebaya krem berenda.",
                "implied_sound": "Bisikan lembut 'selamat ya nak' dari sang ibu",
                "implied_season": "Pagi hari wisuda yang sejuk"
            },
            "story_prompt": "Tangan lembut ibu adalah penopang tak terlihat di balik kesuksesan yang kuraih hari ini."
        },
        75: {
            "new_name": "solo-tunjuk-jari-tekanan-bw-1.jpg",
            "title": "Tekanan Eksistensial Pasca-Lulus",
            "description": "Foto hitam putih dramatis seorang pemuda bersandar pasrah di dinding, dikelilingi oleh bayangan tangan-tangan yang menunjuk ke arahnya, menyimbolkan tuntutan karier.",
            "category_id": "daily-struggle",
            "tone": "Tertekan & Eksistensial",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#7F7F7F"],
            "aesthetic_tags": ["black-white", "existential-pressure", "accused"],
            "sensory_details": {
                "visual_description": "Pemuda berjas menunduk di sudut dinding disinari cahaya remang sementara banyak tangan menunjuk ke arahnya.",
                "implied_sound": "Bisikan suara tuntutan yang memekakkan telinga",
                "implied_season": "Malam hari kelam"
            },
            "story_prompt": "Kapan kamu bekerja? Di mana kamu akan tinggal? Ribuan tanya mengepung jalannya."
        },
        76: {
            "new_name": "solo-tunjuk-jari-tekanan-bw-2.jpg",
            "title": "Sudut Ekspektasi",
            "description": "Refleksi monokromatik dari ketakutan mahasiswa tingkat akhir akan ekspektasi dunia luar setelah melepas toga.",
            "category_id": "daily-struggle",
            "tone": "Tertekan & Sunyi",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#7F7F7F"],
            "aesthetic_tags": ["black-white", "anxiety", "social-pressure"],
            "sensory_details": {
                "visual_description": "Pemuda berjas bersandar di dinding disinari cahaya remang sementara banyak tangan menunjuk ke arahnya.",
                "implied_sound": "Derau statis di dalam kepala",
                "implied_season": "Malam hari kelam"
            },
            "story_prompt": "Di sudut sepi ini, ia berjuang memaafkan ketidaksempurnaan dirinya."
        },
        77: {
            "new_name": "solo-koro-sensei-guts-edit.jpg",
            "title": "Wisuda Bersama Mentor Fantasi",
            "description": "Edit foto wisuda jenaka menempatkan wisudawan di antara Koro-sensei dan Ksatria Guts Berserk, memadukan dunia mimpi dan kenyataan.",
            "category_id": "daily-struggle",
            "tone": "Imaginatif & Jenaka",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#F1C40F", "#2C3E50", "#000000"],
            "aesthetic_tags": ["anime", "berserk", "funny-edit"],
            "sensory_details": {
                "visual_description": "Edit foto pemuda bertoga diapit oleh Koro-sensei kuning dan Guts berzirah hitam.",
                "implied_sound": "Soundtrack anime perjuangan",
                "implied_season": "Sore hari penuh warna"
            },
            "story_prompt": "Dua guru terbaik: yang mengajarkan cara belajar, dan yang mengajarkan cara bertarung."
        },
        78: {
            "new_name": "detail-infografis-bodybuilding.jpg",
            "title": "Transformasi Fisik Perjuangan",
            "description": "Infografis perbandingan bentuk tubuh mahasiswa dari kurus saat stres skripsi hingga berotot setelah rajin gym pasca-kelulusan.",
            "category_id": "daily-struggle",
            "tone": "Motivasi & Humor",
            "content_labels": ["Objek"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#1E1E1E", "#3A3A3A", "#FFFFFF"],
            "aesthetic_tags": ["infographic", "fitness", "comparison"],
            "sensory_details": {
                "visual_description": "Gambar sketsa perbandingan bentuk tubuh pria bertuliskan data berat badan dan massa otot.",
                "implied_sound": "Dentang beban besi di gym kampus",
                "implied_season": "Musim transisi"
            },
            "story_prompt": "Mengubah tekanan skripsi menjadi energi otot di ruang latihan."
        },
        79: {
            "new_name": "solo-sunset-chapter-closed.jpg",
            "title": "Bab Ini Selesai",
            "description": "Latar belakang sunset jingga membingkai siluet seorang mahasiswa bertoga berjalan menjauh, menandai berakhirnya sebuah babak hidup.",
            "category_id": "into-the-unknown",
            "tone": "Bittersweet Farewell",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#E67E22", "#2C3E50", "#D35400"],
            "aesthetic_tags": ["sunset", "silhouette", "departure"],
            "sensory_details": {
                "visual_description": "Siluet wisudawan membelakangi kamera berjalan di jalan beraspal saat matahari terbenam jingga keemasan.",
                "implied_sound": "Alunan gitar akustik penutup film",
                "implied_season": "Senja musim kemarau"
            },
            "story_prompt": "Menutup buku hari ini, bersiap membuka lembaran baru esok pagi."
        },
        80: {
            "new_name": "solo-station-train-departure.jpg",
            "title": "Kereta Menuju Masa Depan",
            "description": "Seorang wisudawan memegang toga berjalan menyusuri peron stasiun kereta api di sore hari, melambangkan perjalanan ke kota baru pasca-lulus.",
            "category_id": "into-the-unknown",
            "tone": "Harapan & Keberangkatan",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#2C3E50", "#E67E22", "#BDC3C7"],
            "aesthetic_tags": ["train-station", "departure", "journey"],
            "sensory_details": {
                "visual_description": "Siluet wisudawan memegang jubah bertoga berjalan di sepanjang peron kereta api saat senja.",
                "implied_sound": "Suara klakson kereta api dan deru mesin perlahan",
                "implied_season": "Senja musim hujan"
            },
            "story_prompt": "Kereta ini membawa lebih dari sekadar tubuh; ia membawa semua mimpi masa muda."
        },
        81: {
            "new_name": "keluarga-haru-tangis-ibu.jpg",
            "title": "Air Mata di Album Usang",
            "description": "Potret penuh haru ibu dan anak melihat album foto lama bersama, meneteskan air mata bahagia melihat perjalanan panjang sang sarjana.",
            "category_id": "found-family",
            "tone": "Haru & Penuh Kasih",
            "content_labels": ["Keluarga"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#3E2723", "#F5EBE0", "#D5BDAF"],
            "aesthetic_tags": ["mother", "tears", "family-love"],
            "sensory_details": {
                "visual_description": "Ibu memeluk anaknya yang mengenakan toga sambil membuka lembar album foto.",
                "implied_sound": "Isak tangis bahagia yang tertahan",
                "implied_season": "Sore hari penuh haru"
            },
            "story_prompt": "Ibu berkata, 'Semua lelahku hilang hari ini melihatmu memakai toga.'"
        },
        82: {
            "new_name": "solo-tangga-kaca-modern.jpg",
            "title": "Langkah Menembus Cahaya",
            "description": "Seorang lulusan berjalan menaiki tangga kaca modern dengan berkas sinar matahari menembus jendela kaca raksasa di sampingnya.",
            "category_id": "into-the-unknown",
            "tone": "Optimistis & Sinematik",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#ECEFF1", "#37474F", "#B0BEC5"],
            "aesthetic_tags": ["staircase", "glass-window", "light-beam"],
            "sensory_details": {
                "visual_description": "Wisudawan membelakangi kamera menaiki tangga beton di dalam gedung berkaca besar disinari cahaya matahari pagi.",
                "implied_sound": "Ketukan alas sepatu di anak tangga kayu stasiun",
                "implied_season": "Pagi hari cerah"
            },
            "story_prompt": "Setiap anak tangga yang kudaki membimbingku keluar dari labirin masa muda."
        },
        83: {
            "new_name": "solo-firstday-lastday-compare.jpg",
            "title": "Hari Pertama vs Hari Terakhir",
            "description": "Foto perbandingan visual mahasiswa baru beransel dan wisudawan mengenakan jubah toga berlatar gerbang kampus sore hari.",
            "category_id": "into-the-unknown",
            "tone": "Nostalgia Transisi",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2C3E50", "#7F8C8D", "#ECEFF1"],
            "aesthetic_tags": ["transition", "first-day", "last-day"],
            "sensory_details": {
                "visual_description": "Dua foto bersanding: mahasiswa beransel di kelas tua, dan mahasiswa bertoga tersenyum di balkon luar.",
                "implied_sound": "Suara angin waktu yang berputar cepat",
                "implied_season": "Siklus 7 tahun perjalanan"
            },
            "story_prompt": "Jika kamu bisa berbisik pada dirimu di hari pertama kuliah, apa yang akan kamu katakan?"
        },
        84: {
            "new_name": "solo-first-day-last-day-collage.jpg",
            "title": "Jejak Waktu di Kampus",
            "description": "Kolase perbandingan visual mahasiswa baru beransel dan wisudawan mengenakan jubah toga berlatar gerbang kampus sore hari.",
            "category_id": "into-the-unknown",
            "tone": "Nostalgia & Haru",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#2C3E50", "#D35400", "#FFFFFF"],
            "aesthetic_tags": ["collage", "time-travel", "memories"],
            "sensory_details": {
                "visual_description": "Kolase menampilkan wisudawan berdiri di tempat yang sama di koridor dengan selisih waktu 7 tahun.",
                "implied_sound": "Detak waktu yang berdering pelan",
                "implied_season": "Sore hari hangat"
            },
            "story_prompt": "Kita melangkah masuk sebagai pemimpi, dan melangkah keluar sebagai pemenang."
        },
        85: {
            "new_name": "solo-duduk-taman-malam-bw.jpg",
            "title": "Hening Malam Terakhir",
            "description": "Potret hitam putih wisudawan duduk termenung di atas bangku taman kampus di bawah naungan cahaya lampu temaram di keheningan malam kelulusan.",
            "category_id": "silent-reflection",
            "tone": "Sunyi & Dokumenter",
            "content_labels": ["Solo"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#000000", "#FFFFFF", "#3A3A3A"],
            "aesthetic_tags": ["black-white", "night-bench", "graduation-night"],
            "sensory_details": {
                "visual_description": "Potret membelakangi wisudawan bertoga duduk sendirian di bangku kayu di taman gelap disinari lampu jalan.",
                "implied_sound": "Suara jangkrik malam dan angin sepoi-sepoi",
                "implied_season": "Tengah malam wisuda"
            },
            "story_prompt": "Malam terakhir di sudut taman ini sebelum esok pagi membawa kita ke kota yang berbeda."
        },
        86: {
            "new_name": "solo-lorong-pilar-simetris.jpg",
            "title": "Symmetry of Departure",
            "description": "Lulusan bertoga berjalan menyusuri koridor panjang dengan barisan pilar beton simetris yang megah, memproyeksikan perspektif yang luas.",
            "category_id": "into-the-unknown",
            "tone": "Sinematik & Tenang",
            "content_labels": ["Solo"],
            "technique_labels": ["Film"],
            "dominant_colors": ["#D5C5B5", "#2C3E50", "#ECEFF1"],
            "aesthetic_tags": ["symmetry", "columns", "corridor"],
            "sensory_details": {
                "visual_description": "Mahasiswa bertoga berjalan menjauhi kamera di lorong bangunan pilar bergaya kolonial yang simetris.",
                "implied_sound": "Langkah kaki tunggal bergema di lorong pilar",
                "implied_season": "Sore hari hangat"
            },
            "story_prompt": "Lorong simetris ini membentang panjang, menggambarkan jalan masa depan yang harus kutempuh."
        },
        87: {
            "new_name": "solo-menatap-langit-senja.jpg",
            "title": "Membaca Langit Senja",
            "description": "Potret syahdu seorang wisudawan menatap langit senja berawan yang berwarna jingga keunguan di atas balkon gedung kampus.",
            "category_id": "silent-reflection",
            "tone": "Syahdu & Nostalgik",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#8E44AD", "#D35400", "#2C3E50"],
            "aesthetic_tags": ["sunset-clouds", "silhouette", "balcony"],
            "sensory_details": {
                "visual_description": "Wisudawan membelakangi kamera berdiri menatap warna jingga keunguan langit berawan di atas balkon.",
                "implied_sound": "Alunan musik syahdu dan desau angin senja",
                "implied_season": "Senja musim kemarau"
            },
            "story_prompt": "Langit sore ini adalah lukisan terindah untuk menutup lembaran cerita kampus kita."
        },
        88: {
            "new_name": "detail-kelas-kuliah-sore.jpg",
            "title": "Sore di Kelas yang Kosong",
            "description": "Cahaya matahari sore yang hangat menerobos jendela menyinari deretan meja dan kursi kosong di ruang kelas kuliah yang sunyi.",
            "category_id": "silent-reflection",
            "tone": "Kesunyian Indah",
            "content_labels": ["Objek"],
            "technique_labels": ["Dark"],
            "dominant_colors": ["#8A6D56", "#E5D4C0", "#2C2C2C"],
            "aesthetic_tags": ["empty-classroom", "sunset-glow", "nostalgic"],
            "sensory_details": {
                "visual_description": "Ruang kelas kuliah kosong disinari berkas cahaya sore yang hangat dari samping.",
                "implied_sound": "Gema debu-debu beterbangan ditiup angin sepoi",
                "implied_season": "Akhir semester sore hari"
            },
            "story_prompt": "Di bangku inilah semua id, kecemasan, dan persahabatan pernah lahir."
        },
        89: {
            "new_name": "solo-charizard-refleksi-air.jpg",
            "title": "Mimpi Naga di Senja Hari",
            "description": "Edit foto surealis menampilkan wisudawan duduk berdampingan dengan seekor naga jingga (Charizard) di tepi genangan air yang merefleksikan langit senja dan lampu gedung kota.",
            "category_id": "daily-struggle",
            "tone": "Surealis & Fantasi",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#D35400", "#1E3A8A", "#FFFFFF"],
            "aesthetic_tags": ["charizard", "reflection", "surreal-sunset"],
            "sensory_details": {
                "visual_description": "Mahasiswa bertoga duduk membelakangi kamera di samping naga bersayap di atas genangan air pemantul cahaya gedung pencakar langit malam.",
                "implied_sound": "Suara kepakan sayap samar dan deru kota malam",
                "implied_season": "Senja musim hujan"
            },
            "story_prompt": "Kita melangkah keluar membawa naga impian masa kecil kita ke dunia nyata."
        },
        90: {
            "new_name": "solo-sunrise-road-forward.jpg",
            "title": "Bab Selesai, Cerita Berlanjut",
            "description": "Seorang wisudawan memunggungi kamera berjalan menuju gerbang cahaya keemasan matahari terbit, membawa ijazah di tangannya.",
            "category_id": "into-the-unknown",
            "tone": "Optimistis & Syahdu",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#E67E22", "#34495E", "#FFFFFF"],
            "aesthetic_tags": ["sunrise", "finish", "new-chapter"],
            "sensory_details": {
                "visual_description": "Wisudawan membelakangi kamera berjalan di aspal basah menuju matahari terbit yang megah.",
                "implied_sound": "Musik orkestra instrumental yang megah dan tenang",
                "implied_season": "Fajar musim kemarau"
            },
            "story_prompt": "Ini bukanlah akhir dari cerita, melainkan awal dari perjalanan yang sesungguhnya."
        },
        91: {
            "new_name": "solo-into-the-unknown-collage.jpg",
            "title": "Into The Unknown Collage",
            "description": "Kolase grafis bernuansa oranye keemasan bertuliskan 'Into the unknown' menampilkan lulusan berjalan melintasi kampus saat sunset indah.",
            "category_id": "into-the-unknown",
            "tone": "Syahdu & Harapan",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#D35400", "#1E2A38", "#F5EBE6"],
            "aesthetic_tags": ["collage", "orange-sunset", "text-graphic"],
            "sensory_details": {
                "visual_description": "Kolase menampilkan foto sunset jalan kampus dengan siluet lulusan dan teks bergaya majalah indie.",
                "implied_sound": "Petikan gitar akustik yang lambat",
                "implied_season": "Senja musim kemarau"
            },
            "story_prompt": "Melangkah ke dunia yang tidak kita ketahui, dengan harapan yang membimbing di dada."
        },
        92: {
            "new_name": "solo-senja-surat-korosensei.jpg",
            "title": "Pesan dari Guru Terakhir",
            "description": "Langkah kaki wisudawan di jalan beraspal senja hari dengan ilustrasi surat dari Koro-sensei berisi selamat dan nasehat hidup.",
            "category_id": "into-the-unknown",
            "tone": "Nostalgia Hangat",
            "content_labels": ["Solo"],
            "technique_labels": ["Sunset"],
            "dominant_colors": ["#D35400", "#2C3E50", "#F5EBE6"],
            "aesthetic_tags": ["message", "korosensei", "candid"],
            "sensory_details": {
                "visual_description": "Lulusan berjalan membelakangi di jalan kampus saat senja, dengan teks surat Koro-sensei bertulis tangan di sudut.",
                "implied_sound": "Bisikan angin sore membawa petuah hangat",
                "implied_season": "Senja kelulusan"
            },
            "story_prompt": "Selamat. Kamu telah belajar banyak. Sekarang ajarkan kebaikan itu kepada dunia."
        },
        93: {
            "new_name": "teman-candid-flash-night.jpg",
            "title": "Tawa Malam Kelulusan",
            "description": "Potret candid berkecepatan rendah menggunakan flash, menangkap ekspresi tawa lepas sekelompok sahabat berjalan bersama di kegelapan malam kelulusan.",
            "category_id": "found-family",
            "tone": "Kebebasan Jiwa & Tawa",
            "content_labels": ["Teman"],
            "technique_labels": ["Flash"],
            "dominant_colors": ["#000000", "#FFFFFF", "#3A3A3A"],
            "aesthetic_tags": ["candid-flash", "night-walk", "friends"],
            "sensory_details": {
                "visual_description": "Foto flash buram malam hari memperlihatkan sahabat merangkul pundak satu sama lain sambil tertawa lebar.",
                "implied_sound": "Tawa lepas yang menggema di jalan sepi tengah malam",
                "implied_season": "Tengah malam wisuda"
            },
            "story_prompt": "Biar dunia luar berisik, malam ini kita tertawa bersama seolah waktu telah berhenti."
        }
    }

    # Helper options for old generated filenames
    content_opts = ["Solo", "Keluarga", "Teman", "Pasangan", "Objek"]
    tech_opts = ["Sunset", "Blur", "Dark", "Flash", "Film"]

    # 1. Scan the directory and map MD5 of all files currently on disk
    disk_md5_to_paths = {}
    print("Memindai dan menghitung MD5 semua file di folder...")
    for fname in os.listdir(IMAGE_DIR):
        fpath = os.path.join(IMAGE_DIR, fname)
        if os.path.isfile(fpath):
            try:
                f_hash = calculate_md5(fpath).lower()
                if f_hash not in disk_md5_to_paths:
                    disk_md5_to_paths[f_hash] = []
                disk_md5_to_paths[f_hash].append(fpath)
            except Exception as e:
                pass

    renamed_images = []

    # 2. Match metadata IDs to files on disk by MD5
    for img_id in range(1, 94):
        img_detail = curated_data.get(img_id)
        sheet_info = sheet_mapping.get(str(img_id))
        
        if not img_detail or not sheet_info:
            print(f"[Warning] ID {img_id} tidak terdaftar!")
            continue

        target_md5 = sheet_info["id"].lower()
        new_filename = img_detail["new_name"]
        target_path = os.path.join(IMAGE_DIR, new_filename)

        # Check if the file is already renamed and exists at the target path
        if os.path.exists(target_path):
            # Perfect, already in place
            pass
        else:
            # We need to find a file on disk that has target_md5
            available_paths = disk_md5_to_paths.get(target_md5, [])
            if not available_paths:
                print(f"[Warning] ID {img_id} (MD5: {target_md5}) tidak ditemukan di disk.")
                continue
            
            # Pick the first available path
            src_path = available_paths[0]
            
            # If this is a duplicate MD5 shared by multiple IDs, we copy instead of rename
            # to make sure both files exist. We check if there are other IDs needing this MD5.
            is_shared = False
            for other_id in range(1, 94):
                if other_id != img_id:
                    other_info = sheet_mapping.get(str(other_id))
                    if other_info and other_info["id"].lower() == target_md5:
                        is_shared = True
                        break

            try:
                if is_shared:
                    shutil.copy2(src_path, target_path)
                    print(f"[Copy Duplikat] {src_path} -> {new_filename}")
                else:
                    os.rename(src_path, target_path)
                    print(f"[Rename] {src_path} -> {new_filename}")
                    # Update our scanned map to reflect the rename
                    available_paths[0] = target_path
            except Exception as e:
                print(f"[Error] Gagal memindahkan {src_path} ke {new_filename}: {e}")
                new_filename = os.path.basename(src_path)

        # Append to metadata JSON
        img_metadata = {
            "id": sheet_info["id"],
            "filename": new_filename,
            "title": img_detail["title"],
            "description": img_detail["description"],
            "category_id": img_detail["category_id"],
            "tone": img_detail["tone"],
            "content_labels": img_detail["content_labels"],
            "technique_labels": img_detail["technique_labels"],
            "dominant_colors": img_detail["dominant_colors"],
            "aesthetic_tags": img_detail["aesthetic_tags"],
            "sensory_details": img_detail["sensory_details"],
            "story_prompt": img_detail["story_prompt"]
        }
        renamed_images.append(img_metadata)

    # 3. Export final JSON
    final_json = {
        "collection_theme": "Transisi Sinematik & Nostalgia Sore Hari",
        "collection_summary": "Koleksi kurasi visual wisuda yang memadukan kehangatan kenangan kampus, persahabatan karib, dan ketidakpastian langkah menuju masa depan yang baru.",
        "collection_story": "Di antara sudut-sudut perpustakaan yang sunyi, lembaran buku yang kusam, dan canda tawa hangat di bawah sinar matahari sore, lembaran moodboard ini adalah saksi dari sebuah akhir.\n\nKita memulai perjalanan ini sebagai orang asing yang membawa mimpi masing-masing, berjuang dalam revisi skripsi yang tak berujung, hingga akhirnya berdiri di gerbang kelulusan dengan jubah toga hitam yang berat.\n\nMatahari terbenam menandai babak yang ditutup, kereta api menanti di peron stasiun untuk membawa kita ke kota masing-masing, namun kenangan tentang tawa malam hari dan dukungan hangat keluarga akan menetap selamanya.",
        "categories": categories,
        "images": renamed_images
    }

    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)

    print(f"\n[Sukses] Fisik file berhasil diubah dan data kurasi rapi diekspor ke {METADATA_FILE}!")

if __name__ == "__main__":
    main()
