"""
Demo script untuk menguji program split image
Membuat gambar test sederhana untuk testing
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image():
    """Membuat gambar test sederhana"""
    # Buat gambar dengan warna gradient
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Buat gradient background
    for y in range(height):
        r = int(255 * (y / height))
        g = int(128 * (1 - y / height))
        b = int(255 * (1 - y / height))
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
    
    # Tambahkan grid lines untuk memudahkan melihat hasil split
    grid_size = 100
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill='black', width=2)
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill='black', width=2)
    
    # Tambahkan teks
    try:
        font = ImageFont.load_default()
    except:
        font = None
    
    # Grid numbers
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            text = f"({x//grid_size},{y//grid_size})"
            draw.text((x+10, y+10), text, fill='white', font=font)
    
    # Judul
    draw.text((width//2-100, 50), "TEST IMAGE 800x600", fill='yellow', font=font)
    draw.text((width//2-120, height-100), "Split Image Demo", fill='cyan', font=font)
    
    return img

def main():
    print("🎨 Membuat gambar test untuk demo...")
    
    # Pastikan folder images ada
    os.makedirs('images', exist_ok=True)
    
    # Buat dan simpan gambar test
    test_img = create_test_image()
    test_path = os.path.join('images', 'test_demo.png')
    test_img.save(test_path, 'PNG')
    
    print(f"✅ Gambar test berhasil dibuat: {test_path}")
    print(f"   Ukuran: 800x600 pixel")
    print(f"   Format: PNG")
    print("\n📝 Saran untuk testing:")
    print("   - Coba split dengan 200x150 pixel (akan jadi 4x4 = 16 potongan)")
    print("   - Coba split dengan 100x100 pixel (akan jadi 8x6 = 48 potongan)")
    print("   - Atau dimensi lain sesuai keinginan")
    print("\n🚀 Sekarang jalankan: python split_image.py")

if __name__ == "__main__":
    main()