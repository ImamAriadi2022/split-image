"""
Script untuk membuat gambar test dengan berbagai rasio
untuk menguji fitur split by ratio
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_ratio_test_images():
    """Membuat beberapa gambar test dengan rasio berbeda"""
    
    # Pastikan folder images ada
    os.makedirs('images', exist_ok=True)
    
    # Gambar 1: Rasio 1:3 (vertikal - tinggi 3x lebar)
    print("🎨 Membuat gambar test rasio 1:3 (vertikal)...")
    width, height = 400, 1200  # rasio 1:3
    img1 = Image.new('RGB', (width, height), color='lightblue')
    draw1 = ImageDraw.Draw(img1)
    
    # Bagi menjadi 3 bagian dengan warna berbeda
    section_height = height // 3
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # merah, cyan, biru
    
    for i in range(3):
        y_start = i * section_height
        y_end = (i + 1) * section_height
        draw1.rectangle([0, y_start, width, y_end], fill=colors[i])
        
        # Tambahkan teks
        try:
            font = ImageFont.load_default()
        except:
            font = None
        
        text = f"BAGIAN {i+1}"
        text_y = y_start + section_height // 2
        draw1.text((width//2-40, text_y), text, fill='white', font=font)
    
    # Tambahkan info rasio
    draw1.text((10, 10), "RASIO 1:3", fill='white', font=font)
    draw1.text((10, 30), f"{width}x{height}px", fill='white', font=font)
    
    img1.save('images/test_rasio_1-3_vertikal.png')
    print(f"   ✅ Tersimpan: test_rasio_1-3_vertikal.png ({width}x{height}px)")
    
    
    # Gambar 2: Rasio 3:1 (horizontal - lebar 3x tinggi)
    print("🎨 Membuat gambar test rasio 3:1 (horizontal)...")
    width, height = 1200, 400  # rasio 3:1
    img2 = Image.new('RGB', (width, height), color='lightgray')
    draw2 = ImageDraw.Draw(img2)
    
    # Bagi menjadi 3 bagian dengan warna berbeda
    section_width = width // 3
    colors = ['#FF9FF3', '#54A0FF', '#5F27CD']  # pink, biru muda, ungu
    
    for i in range(3):
        x_start = i * section_width
        x_end = (i + 1) * section_width
        draw2.rectangle([x_start, 0, x_end, height], fill=colors[i])
        
        # Tambahkan teks
        text = f"BAGIAN {i+1}"
        text_x = x_start + section_width // 2 - 40
        draw2.text((text_x, height//2), text, fill='white', font=font)
    
    # Tambahkan info rasio
    draw2.text((10, 10), "RASIO 3:1", fill='white', font=font)
    draw2.text((10, 30), f"{width}x{height}px", fill='white', font=font)
    
    img2.save('images/test_rasio_3-1_horizontal.png')
    print(f"   ✅ Tersimpan: test_rasio_3-1_horizontal.png ({width}x{height}px)")
    
    
    # Gambar 3: Rasio 16:9 (landscape umum)
    print("🎨 Membuat gambar test rasio 16:9...")
    width, height = 1600, 900  # rasio 16:9
    img3 = Image.new('RGB', (width, height), color='black')
    draw3 = ImageDraw.Draw(img3)
    
    # Gradient background
    for y in range(height):
        r = int(255 * (y / height))
        g = int(100)
        b = int(255 * (1 - y / height))
        color = (r, g, b)
        draw3.line([(0, y), (width, y)], fill=color)
    
    # Grid untuk memudahkan melihat hasil split
    grid_w = width // 4
    grid_h = height // 3
    
    for x in range(0, width, grid_w):
        draw3.line([(x, 0), (x, height)], fill='yellow', width=2)
    for y in range(0, height, grid_h):
        draw3.line([(0, y), (width, y)], fill='yellow', width=2)
    
    # Info text
    draw3.text((50, 50), "RASIO 16:9", fill='white', font=font)
    draw3.text((50, 80), f"{width}x{height}px", fill='white', font=font)
    draw3.text((50, height-100), "Test Split Ratio", fill='cyan', font=font)
    
    img3.save('images/test_rasio_16-9.png')
    print(f"   ✅ Tersimpan: test_rasio_16-9.png ({width}x{height}px)")

def main():
    print("🎯 MEMBUAT GAMBAR TEST UNTUK SPLIT BY RATIO")
    print("=" * 50)
    
    create_ratio_test_images()
    
    print("\n📋 SARAN TESTING:")
    print("-" * 30)
    print("1. Gambar rasio 1:3 vertikal → split dengan rasio 1:1")
    print("   Hasil: 3 potongan persegi")
    print()
    print("2. Gambar rasio 3:1 horizontal → split dengan rasio 1:1") 
    print("   Hasil: 3 potongan persegi")
    print()
    print("3. Gambar rasio 16:9 → split dengan rasio 16:9")
    print("   Hasil: 1 potongan (sama dengan asli)")
    print()
    print("4. Gambar rasio 16:9 → split dengan rasio 4:3")
    print("   Hasil: beberapa potongan dengan rasio 4:3")
    print()
    print("🚀 Sekarang jalankan: python split_image.py")

if __name__ == "__main__":
    main()