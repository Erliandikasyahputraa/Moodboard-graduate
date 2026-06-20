// State Aplikasi
let appState = {
    theme: "",
    summary: "",
    story: "",
    categories: [],
    images: [],
    activeCategory: "all",
    searchQuery: ""
};

// DOM Elements
const loaderScreen = document.getElementById("loader-screen");
const themeEl = document.getElementById("collection-theme");
const summaryEl = document.getElementById("collection-summary");
const storyEl = document.getElementById("collection-story");
const categoriesNav = document.getElementById("categories-nav");
const masonryGrid = document.getElementById("masonry-grid");
const emptyState = document.getElementById("empty-state");
const searchInput = document.getElementById("search-input");

// Drawer Elements
const detailDrawer = document.getElementById("detail-drawer");
const drawerOverlay = document.getElementById("drawer-overlay");
const closeDrawerBtn = document.getElementById("close-drawer");
const drawerImg = document.getElementById("drawer-img");
const drawerCategory = document.getElementById("drawer-category");
const drawerTone = document.getElementById("drawer-tone");
const drawerTitle = document.getElementById("drawer-title");
const drawerDesc = document.getElementById("drawer-desc");
const drawerVisualDesc = document.getElementById("drawer-visual-desc");
const drawerSound = document.getElementById("drawer-sound");
const drawerSeason = document.getElementById("drawer-season");
const drawerColors = document.getElementById("drawer-colors");
const drawerTags = document.getElementById("drawer-tags");
const drawerStoryPrompt = document.getElementById("drawer-story-prompt");

// Path gambar relatif ke workspace
const IMAGE_BASE_PATH = "pict Moodboard wisuda/";

// Inisialisasi Galeri
async function initGallery() {
    try {
        const response = await fetch("metadata.json");
        if (!response.ok) {
            throw new Error("File metadata.json tidak ditemukan. Silakan jalankan `python analyze.py` terlebih dahulu.");
        }
        
        const data = await response.json();
        
        // Simpan ke state
        appState.theme = data.collection_theme || "Koleksi Moodboard";
        appState.summary = data.collection_summary || "Silakan jalankan analyze.py untuk kurasi.";
        appState.story = data.collection_story || "";
        appState.categories = data.categories || [];
        appState.images = data.images || [];

        // Render UI
        renderHeader();
        renderCategoryButtons();
        renderGrid();
        setupEventListeners();

        // Sembunyikan loader
        loaderScreen.classList.add("hidden");
    } catch (error) {
        console.error(error);
        showErrorState(error.message);
    }
}

// Menampilkan Error State di Halaman utama
function showErrorState(message) {
    loaderScreen.classList.add("hidden");
    themeEl.textContent = "Galeri Belum Siap";
    summaryEl.innerHTML = `<span style="color: #d9534f; font-weight: 500;">${message}</span>`;
    storyEl.textContent = "Langkah-langkah:\n1. Buka terminal Anda\n2. Set environment variable: GEMINI_API_KEY\n3. Jalankan perintah: python analyze.py";
    document.querySelector(".story-details").open = true;
    masonryGrid.innerHTML = "";
    emptyState.classList.remove("hidden");
    emptyState.innerHTML = `<p>${message}</p>`;
}

// Render Header
function renderHeader() {
    themeEl.textContent = appState.theme;
    summaryEl.textContent = appState.summary;
    storyEl.textContent = appState.story;
}

// Render Tombol Kategori
function renderCategoryButtons() {
    // Bersihkan kecuali tombol "Semua"
    categoriesNav.innerHTML = `<button class="cat-btn active" data-category="all">00. Semua Koleksi</button>`;
    
    appState.categories.forEach((cat, index) => {
        const btn = document.createElement("button");
        btn.className = "cat-btn";
        btn.setAttribute("data-category", cat.id);
        
        // Format nomor kategori editorial (01, 02, dst)
        const num = String(index + 1).padStart(2, '0');
        btn.textContent = `${num}. ${cat.name}`;
        categoriesNav.appendChild(btn);
    });
}

// Render Grid Masonry
function renderGrid() {
    masonryGrid.innerHTML = "";
    
    // Filter gambar berdasarkan kategori dan pencarian
    const filteredImages = appState.images.filter(img => {
        const matchesCategory = appState.activeCategory === "all" || img.category_id === appState.activeCategory;
        
        const searchLower = appState.searchQuery.toLowerCase();
        const matchesSearch = !appState.searchQuery || 
            (img.title && img.title.toLowerCase().includes(searchLower)) ||
            (img.description && img.description.toLowerCase().includes(searchLower)) ||
            (img.tone && img.tone.toLowerCase().includes(searchLower)) ||
            (img.aesthetic_tags && img.aesthetic_tags.some(tag => tag.toLowerCase().includes(searchLower)));
            
        return matchesCategory && matchesSearch;
    });

    if (filteredImages.length === 0) {
        emptyState.classList.remove("hidden");
    } else {
        emptyState.classList.add("hidden");
        
        filteredImages.forEach(img => {
            const item = document.createElement("div");
            item.className = "gallery-item";
            item.setAttribute("data-id", img.id);
            
            // Dapatkan nama kategori
            const categoryObj = appState.categories.find(c => c.id === img.category_id);
            const categoryName = categoryObj ? categoryObj.name : "Uncategorized";

            item.innerHTML = `
                <img src="${IMAGE_BASE_PATH}${img.filename}" alt="${img.title || 'Moodboard item'}" loading="lazy">
                <div class="item-info-overlay">
                    <h3 class="item-title">${img.title || 'Tanpa Judul'}</h3>
                    <span class="item-category">${categoryName}</span>
                </div>
            `;
            
            item.addEventListener("click", () => openDrawer(img));
            masonryGrid.appendChild(item);
        });
    }
}

// Buka Drawer Detail
function openDrawer(img) {
    const categoryObj = appState.categories.find(c => c.id === img.category_id);
    const categoryName = categoryObj ? categoryObj.name : "Uncategorized";
    
    drawerImg.src = `${IMAGE_BASE_PATH}${img.filename}`;
    drawerImg.alt = img.title || "Detail Gambar";
    
    drawerCategory.textContent = categoryName;
    drawerTone.textContent = img.tone || "Suasana";
    drawerTitle.textContent = img.title || "Tanpa Judul";
    drawerDesc.textContent = img.description || "";
    
    // Sensory Details
    const sensory = img.sensory_details || {};
    drawerVisualDesc.textContent = sensory.visual_description || "Tidak tersedia";
    drawerSound.textContent = sensory.implied_sound || "Tidak tersedia";
    drawerSeason.textContent = sensory.implied_season || "Tidak tersedia";
    
    // Dominant Colors
    drawerColors.innerHTML = "";
    if (img.dominant_colors && img.dominant_colors.length > 0) {
        img.dominant_colors.forEach(color => {
            const swatch = document.createElement("div");
            swatch.className = "color-swatch";
            swatch.style.backgroundColor = color;
            swatch.setAttribute("data-hex", color);
            drawerColors.appendChild(swatch);
        });
    } else {
        drawerColors.innerHTML = "<p style='font-size:0.85rem;color:var(--text-muted);'>Tidak ada data warna.</p>";
    }
    
    // Aesthetic Tags
    drawerTags.innerHTML = "";
    if (img.aesthetic_tags && img.aesthetic_tags.length > 0) {
        img.aesthetic_tags.forEach(tag => {
            const span = document.createElement("span");
            span.className = "tag";
            span.textContent = `#${tag}`;
            drawerTags.appendChild(span);
        });
    }
    
    // Story Prompt
    drawerStoryPrompt.textContent = img.story_prompt ? `"${img.story_prompt}"` : '"..."';
    
    // Tampilkan Drawer
    detailDrawer.classList.add("open");
    detailDrawer.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden"; // Disable body scroll
}

// Tutup Drawer Detail
function closeDrawer() {
    detailDrawer.classList.remove("open");
    detailDrawer.setAttribute("aria-hidden", "true");
    document.body.style.overflow = ""; // Enable body scroll
    
    // Bersihkan src agar hemat memori setelah ditutup
    setTimeout(() => {
        if (!detailDrawer.classList.contains("open")) {
            drawerImg.src = "";
        }
    }, 400);
}

// Event Listeners
function setupEventListeners() {
    // Navigasi Kategori
    categoriesNav.addEventListener("click", (e) => {
        const btn = e.target.closest(".cat-btn");
        if (!btn) return;
        
        // Ganti kelas aktif
        document.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        appState.activeCategory = btn.getAttribute("data-category");
        renderGrid();
    });
    
    // Input Pencarian (Debounce Sederhana)
    let searchTimeout;
    searchInput.addEventListener("input", (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            appState.searchQuery = e.target.value;
            renderGrid();
        }, 250);
    });
    
    // Tombol Tutup Drawer
    closeDrawerBtn.addEventListener("click", closeDrawer);
    drawerOverlay.addEventListener("click", closeDrawer);
    
    // Keyboard Esc untuk menutup Drawer
    window.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && detailDrawer.classList.contains("open")) {
            closeDrawer();
        }
    });
}

// Jalankan saat dokumen siap
document.addEventListener("DOMContentLoaded", initGallery);
