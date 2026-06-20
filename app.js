// State Aplikasi
let appState = {
    theme: "",
    summary: "",
    story: "",
    categories: [],
    images: [],
    activeSubject: "all",
    activeVibe: "all",
    searchQuery: "",
    gridSize: "md",
    layout: "masonry"
};

// DOM Elements
const loaderScreen = document.getElementById("loader-screen");
const themeEl = document.getElementById("collection-theme");
const summaryEl = document.getElementById("collection-summary");
const storyEl = document.getElementById("collection-story");
const masonryGrid = document.getElementById("masonry-grid");
const emptyState = document.getElementById("empty-state");
const searchInput = document.getElementById("search-input");

// Filter & Grid Elements
const subjectFilters = document.getElementById("subject-filters");
const vibeFilters = document.getElementById("vibe-filters");
const gridBtnGroup = document.querySelector(".grid-btn-group");
const layoutBtnGroup = document.querySelector(".layout-btn-group");

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
        // Gunakan cache buster untuk memotong caching browser
        const response = await fetch(`metadata.json?v=${Date.now()}`);
        if (!response.ok) {
            throw new Error("File metadata.json tidak ditemukan. Silakan jalankan `python write_final_metadata.py` terlebih dahulu.");
        }
        
        const data = await response.json();
        
        // Simpan ke state
        appState.theme = data.collection_theme || "Koleksi Moodboard";
        appState.summary = data.collection_summary || "Silakan jalankan write_final_metadata.py untuk kurasi.";
        appState.story = data.collection_story || "";
        appState.categories = data.categories || [];
        appState.images = data.images || [];

        // Render UI
        renderHeader();
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
    storyEl.textContent = "Langkah-langkah:\n1. Buka terminal Anda\n2. Jalankan perintah: python write_final_metadata.py";
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

// Render Grid Masonry
function renderGrid() {
    masonryGrid.innerHTML = "";
    
    // Terapkan kelas ukuran grid ke elemen masonry
    masonryGrid.className = "masonry-grid";
    
    // Terapkan tata letak (masonry atau flat)
    if (appState.layout === "flat") {
        masonryGrid.classList.add("layout-flat");
    }
    
    if (appState.gridSize === "sm") {
        masonryGrid.classList.add("grid-sm");
    } else if (appState.gridSize === "lg") {
        masonryGrid.classList.add("grid-lg");
    }

    // Filter gambar berdasarkan Subject, Vibe, dan Search Query
    const filteredImages = appState.images.filter(img => {
        // 1. Filter Subjek
        const matchesSubject = appState.activeSubject === "all" || 
            (img.content_labels && img.content_labels.includes(appState.activeSubject));
            
        // 2. Filter Vibe/Teknik
        const matchesVibe = appState.activeVibe === "all" || 
            (img.technique_labels && img.technique_labels.includes(appState.activeVibe));
        
        // 3. Pencarian Teks
        const searchLower = appState.searchQuery.toLowerCase();
        const matchesSearch = !appState.searchQuery || 
            (img.title && img.title.toLowerCase().includes(searchLower)) ||
            (img.description && img.description.toLowerCase().includes(searchLower)) ||
            (img.tone && img.tone.toLowerCase().includes(searchLower)) ||
            (img.aesthetic_tags && img.aesthetic_tags.some(tag => tag.toLowerCase().includes(searchLower)));
            
        return matchesSubject && matchesVibe && matchesSearch;
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
                <div class="img-wrapper">
                    <img src="${IMAGE_BASE_PATH}${img.filename}" alt="${img.title || 'Moodboard item'}" loading="lazy">
                </div>
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

    // Photography Details
    const photo = img.photography_details || {};
    document.getElementById("drawer-camera-technique").textContent = photo.technique_and_angle || "Tidak tersedia";
    document.getElementById("drawer-camera-settings").textContent = photo.suggested_settings || "Tidak tersedia";
    document.getElementById("drawer-color-grading").textContent = photo.color_grading || "Tidak tersedia";
    
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
    // 1. Filter Subjek
    subjectFilters.addEventListener("click", (e) => {
        const btn = e.target.closest(".filter-btn");
        if (!btn) return;
        
        subjectFilters.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        appState.activeSubject = btn.getAttribute("data-value");
        renderGrid();
    });

    // 2. Filter Vibe/Teknik
    vibeFilters.addEventListener("click", (e) => {
        const btn = e.target.closest(".filter-btn");
        if (!btn) return;
        
        vibeFilters.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        appState.activeVibe = btn.getAttribute("data-value");
        renderGrid();
    });

    // 3. Grid Size Controls
    gridBtnGroup.addEventListener("click", (e) => {
        const btn = e.target.closest(".grid-btn");
        if (!btn) return;
        
        gridBtnGroup.querySelectorAll(".grid-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        appState.gridSize = btn.getAttribute("data-size");
        renderGrid();
    });

    // 3.5. Layout Controls
    layoutBtnGroup.addEventListener("click", (e) => {
        const btn = e.target.closest(".layout-btn");
        if (!btn) return;
        
        layoutBtnGroup.querySelectorAll(".layout-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        appState.layout = btn.getAttribute("data-layout");
        renderGrid();
    });
    
    // 4. Input Pencarian (Debounce Sederhana)
    let searchTimeout;
    searchInput.addEventListener("input", (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            appState.searchQuery = e.target.value;
            renderGrid();
        }, 250);
    });
    
    // 5. Tombol Tutup Drawer
    closeDrawerBtn.addEventListener("click", closeDrawer);
    drawerOverlay.addEventListener("click", closeDrawer);
    
    // 6. Keyboard Esc untuk menutup Drawer
    window.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && detailDrawer.classList.contains("open")) {
            closeDrawer();
        }
    });
}

// Jalankan saat dokumen siap
document.addEventListener("DOMContentLoaded", initGallery);
