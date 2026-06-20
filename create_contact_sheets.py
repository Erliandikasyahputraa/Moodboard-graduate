import os
import hashlib
import json
from PIL import Image, ImageDraw, ImageFont

IMAGE_DIR = "pict Moodboard wisuda"
OUTPUT_DIR = "docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Grid parameters
THUMB_SIZE = 300
COLS = 5
ROWS = 4
IMAGES_PER_SHEET = COLS * ROWS

def calculate_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def create_sheets():
    # Scan images
    all_files = os.listdir(IMAGE_DIR)
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    image_files = sorted([f for f in all_files if f.lower().endswith(image_extensions)])
    
    print(f"Total images found: {len(image_files)}")
    
    mapping = {}
    sheet_num = 1
    current_images = []
    
    for idx, filename in enumerate(image_files):
        img_id = idx + 1
        filepath = os.path.join(IMAGE_DIR, filename)
        file_hash = calculate_md5(filepath)
        
        mapping[img_id] = {
            "filename": filename,
            "id": file_hash
        }
        
        current_images.append((img_id, filepath))
        
        # If we reached limit or end of list, create sheet
        if len(current_images) == IMAGES_PER_SHEET or idx == len(image_files) - 1:
            # Create blank image
            sheet_w = COLS * THUMB_SIZE
            sheet_h = ROWS * THUMB_SIZE
            sheet_img = Image.new('RGB', (sheet_w, sheet_h), color='#111111')
            draw = ImageDraw.Draw(sheet_img)
            
            for cell_idx, (num, path) in enumerate(current_images):
                row = cell_idx // COLS
                col = cell_idx % COLS
                
                try:
                    with Image.open(path) as img:
                        # Resize and crop to square preserving aspect ratio
                        img_ratio = img.width / img.height
                        if img_ratio > 1:
                            new_w = int(THUMB_SIZE * img_ratio)
                            img_resized = img.resize((new_w, THUMB_SIZE), Image.Resampling.LANCZOS)
                            left = (new_w - THUMB_SIZE) // 2
                            img_cropped = img_resized.crop((left, 0, left + THUMB_SIZE, THUMB_SIZE))
                        else:
                            new_h = int(THUMB_SIZE / img_ratio)
                            img_resized = img.resize((THUMB_SIZE, new_h), Image.Resampling.LANCZOS)
                            top = (new_h - THUMB_SIZE) // 2
                            img_cropped = img_resized.crop((0, top, THUMB_SIZE, top + THUMB_SIZE))
                            
                        # Paste into grid
                        x = col * THUMB_SIZE
                        y = row * THUMB_SIZE
                        sheet_img.paste(img_cropped, (x, y))
                        
                        # Draw number label with background rectangle
                        draw.rectangle([x + 10, y + 10, x + 65, y + 45], fill='#000000')
                        draw.text((x + 18, y + 15), f"#{num}", fill='#FFFFFF', font_size=20)
                except Exception as e:
                    print(f"Error loading {path}: {e}")
            
            output_path = os.path.join(OUTPUT_DIR, f"sheet_{sheet_num}.jpg")
            sheet_img.save(output_path, 'JPEG', quality=85)
            print(f"Saved: {output_path} with {len(current_images)} images")
            
            sheet_num += 1
            current_images = []
            
    with open(os.path.join(OUTPUT_DIR, "sheet_mapping.json"), 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print("Mapping saved to docs/sheet_mapping.json")

if __name__ == "__main__":
    create_sheets()
