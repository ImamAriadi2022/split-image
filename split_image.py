"""
Program Split Image
Memotong gambar menjadi bagian-bagian yang lebih kecil berdasarkan dimensi yang ditentukan.

Cara penggunaan:
1. Letakkan gambar yang ingin dipotong di folder 'images'
2. Jalankan program ini
3. Masukkan dimensi potongan yang diinginkan (height dan width dalam pixel)
4. Hasil potongan akan disimpan di folder 'output'
"""

import os
import sys
from PIL import Image
import math

def get_available_images():
    """Mendapatkan daftar gambar yang tersedia di folder images"""
    images_dir = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(images_dir):
        print("❌ Folder 'images' tidak ditemukan!")
        return []
    
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')
    images = []
    
    for file in os.listdir(images_dir):
        if file.lower().endswith(supported_formats):
            images.append(file)
    
    return images

def display_images(images):
    """Menampilkan daftar gambar yang tersedia"""
    print("\n📁 Gambar yang tersedia:")
    print("-" * 40)
    for i, image in enumerate(images, 1):
        image_path = os.path.join('images', image)
        try:
            with Image.open(image_path) as img:
                print(f"{i}. {image} ({img.width}x{img.height}px)")
        except Exception as e:
            print(f"{i}. {image} (tidak dapat membaca dimensi)")

def get_user_input():
    """Mendapatkan input dari user untuk mode dan dimensi potongan"""
    print("\n⚙️  Pengaturan Split Image")
    print("-" * 40)
    print("Pilih mode pemotongan:")
    print("1. Berdasarkan PIXEL (contoh: 640x480 pixel)")
    print("2. Berdasarkan RASIO (contoh: 1:1, 16:9, 4:3) untuk feed 4:5")
    
    while True:
        try:
            mode = input("\nPilih mode (1 atau 2): ").strip()
            if mode in ['1', '2']:
                break
            else:
                print("❌ Pilih 1 atau 2!")
        except ValueError:
            print("❌ Masukkan pilihan yang valid!")
    
    if mode == '1':
        # Mode pixel (original)
        print("\n📏 Mode PIXEL - Masukkan dimensi dalam pixel:")
        
        while True:
            try:
                width = int(input("Masukkan lebar potongan (width) dalam pixel: "))
                if width <= 0:
                    print("❌ Lebar harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("❌ Mohon masukkan angka yang valid!")
        
        while True:
            try:
                height = int(input("Masukkan tinggi potongan (height) dalam pixel: "))
                if height <= 0:
                    print("❌ Tinggi harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("❌ Mohon masukkan angka yang valid!")
        
        return 'pixel', width, height
    
    else:
        # Mode rasio (new)
        print("\n📐 Mode RASIO - Masukkan rasio potongan:")
        print("Contoh input: 1:1, 16:9, 4:3, 3:2")
        
        while True:
            try:
                ratio_input = input("Masukkan rasio (format lebar:tinggi): ").strip()
                if ':' not in ratio_input:
                    print("❌ Format harus lebar:tinggi (contoh: 1:1)")
                    continue
                
                ratio_parts = ratio_input.split(':')
                if len(ratio_parts) != 2:
                    print("❌ Format harus lebar:tinggi (contoh: 1:1)")
                    continue
                
                ratio_w = float(ratio_parts[0])
                ratio_h = float(ratio_parts[1])
                
                if ratio_w <= 0 or ratio_h <= 0:
                    print("❌ Nilai rasio harus lebih dari 0!")
                    continue
                
                break
            except ValueError:
                print("❌ Mohon masukkan rasio yang valid!")
        
        return 'ratio', ratio_w, ratio_h

def split_image_by_pixel(image_path, output_dir, split_width, split_height):
    """Memotong gambar berdasarkan dimensi pixel yang ditentukan"""
    try:
        # Buka gambar
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            image_ext = os.path.splitext(os.path.basename(image_path))[1]
            
            print(f"\n🖼️  Memproses: {os.path.basename(image_path)}")
            print(f"   Ukuran asli: {img_width}x{img_height}px")
            
            # Hitung jumlah potongan
            cols = math.ceil(img_width / split_width)
            rows = math.ceil(img_height / split_height)
            total_pieces = cols * rows
            
            print(f"   Akan dipotong menjadi: {cols} kolom x {rows} baris = {total_pieces} potongan")
            
            # Buat folder output untuk gambar ini
            image_output_dir = os.path.join(output_dir, image_name)
            os.makedirs(image_output_dir, exist_ok=True)
            
            piece_count = 0
            
            # Potong gambar
            for row in range(rows):
                for col in range(cols):
                    # Hitung koordinat crop
                    left = col * split_width
                    top = row * split_height
                    right = min(left + split_width, img_width)
                    bottom = min(top + split_height, img_height)
                    
                    # Crop gambar
                    piece = img.crop((left, top, right, bottom))
                    
                    # Nama file potongan
                    piece_filename = f"{image_name}_row{row+1:02d}_col{col+1:02d}{image_ext}"
                    piece_path = os.path.join(image_output_dir, piece_filename)
                    
                    # Simpan potongan
                    piece.save(piece_path, quality=95, optimize=True)
                    piece_count += 1
                    
                    print(f"   ✅ Potongan {piece_count}/{total_pieces}: {piece_filename} ({piece.width}x{piece.height}px)")
            
            print(f"   🎉 Selesai! {piece_count} potongan disimpan di: {image_output_dir}")
            return True
            
    except Exception as e:
        print(f"   ❌ Error memproses gambar: {str(e)}")
        return False

def split_image_by_ratio(image_path, output_dir, ratio_w, ratio_h):
    """Memotong gambar berdasarkan rasio yang ditentukan"""
    try:
        # Buka gambar
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            image_ext = os.path.splitext(os.path.basename(image_path))[1]
            
            print(f"\n🖼️  Memproses: {os.path.basename(image_path)}")
            print(f"   Ukuran asli: {img_width}x{img_height}px")
            print(f"   Rasio asli: {img_width/img_height:.2f}:1")
            print(f"   Rasio target: {ratio_w}:{ratio_h} = {ratio_w/ratio_h:.2f}:1")
            
            # Hitung dimensi potongan berdasarkan rasio
            target_ratio = ratio_w / ratio_h
            
            # Tentukan cara terbaik memotong gambar
            if img_width / img_height > target_ratio:
                # Gambar lebih lebar, potong secara horizontal
                piece_height = img_height
                piece_width = int(piece_height * target_ratio)
                cols = img_width // piece_width
                rows = 1
                
                # Sesuaikan jika ada sisa
                if img_width % piece_width > piece_width * 0.5:
                    cols += 1
                    
            else:
                # Gambar lebih tinggi, potong secara vertikal
                piece_width = img_width
                piece_height = int(piece_width / target_ratio)
                rows = img_height // piece_height
                cols = 1
                
                # Sesuaikan jika ada sisa
                if img_height % piece_height > piece_height * 0.5:
                    rows += 1
            
            total_pieces = cols * rows
            
            print(f"   Dimensi potongan: {piece_width}x{piece_height}px")
            print(f"   Akan dipotong menjadi: {cols} kolom x {rows} baris = {total_pieces} potongan")
            
            # Buat folder output untuk gambar ini
            image_output_dir = os.path.join(output_dir, image_name)
            os.makedirs(image_output_dir, exist_ok=True)
            
            piece_count = 0
            
            # Potong gambar
            for row in range(rows):
                for col in range(cols):
                    # Hitung koordinat crop
                    left = col * piece_width
                    top = row * piece_height
                    right = min(left + piece_width, img_width)
                    bottom = min(top + piece_height, img_height)
                    
                    # Skip jika area terlalu kecil
                    if (right - left) < piece_width * 0.5 or (bottom - top) < piece_height * 0.5:
                        continue
                    
                    # Crop gambar
                    piece = img.crop((left, top, right, bottom))
                    
                    # Nama file potongan
                    actual_ratio = piece.width / piece.height
                    piece_filename = f"{image_name}_ratio{ratio_w}-{ratio_h}_{row+1:02d}_{col+1:02d}{image_ext}"
                    piece_path = os.path.join(image_output_dir, piece_filename)
                    
                    # Simpan potongan
                    piece.save(piece_path, quality=95, optimize=True)
                    piece_count += 1
                    
                    print(f"   ✅ Potongan {piece_count}: {piece_filename}")
                    print(f"      Ukuran: {piece.width}x{piece.height}px | Rasio: {actual_ratio:.2f}:1")
            
            print(f"   🎉 Selesai! {piece_count} potongan disimpan di: {image_output_dir}")
            return True
            
    except Exception as e:
        print(f"   ❌ Error memproses gambar: {str(e)}")
        return False

def split_image(image_path, output_dir, mode, param1, param2):
    """Wrapper function untuk memilih mode pemotongan"""
    if mode == 'pixel':
        return split_image_by_pixel(image_path, output_dir, param1, param2)
    else:  # mode == 'ratio'
        return split_image_by_ratio(image_path, output_dir, param1, param2)

def main():
    """Fungsi utama program"""
    print("🎨 PROGRAM SPLIT IMAGE")
    print("=" * 50)
    print("Program ini memotong gambar menjadi bagian-bagian kecil")
    print("berdasarkan dimensi yang Anda tentukan.")
    
    # Cek apakah folder images ada
    if not os.path.exists('images'):
        print("\n❌ Folder 'images' tidak ditemukan!")
        print("Membuat folder 'images'...")
        os.makedirs('images')
        print("✅ Folder 'images' telah dibuat.")
        print("📝 Silakan letakkan gambar yang ingin dipotong di folder 'images' terlebih dahulu.")
        input("\nTekan Enter untuk keluar...")
        return
    
    # Dapatkan daftar gambar
    images = get_available_images()
    
    if not images:
        print("\n❌ Tidak ada gambar yang ditemukan di folder 'images'!")
        print("📝 Silakan letakkan gambar (PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP) di folder 'images'.")
        input("\nTekan Enter untuk keluar...")
        return
    
    # Tampilkan daftar gambar
    display_images(images)
    
    # Pilih gambar
    print(f"\n🔍 Pilih gambar yang ingin dipotong:")
    while True:
        try:
            choice = input(f"Masukkan nomor gambar (1-{len(images)}) atau 'all' untuk semua gambar: ").strip().lower()
            
            if choice == 'all':
                selected_images = images
                break
            else:
                choice_num = int(choice)
                if 1 <= choice_num <= len(images):
                    selected_images = [images[choice_num - 1]]
                    break
                else:
                    print(f"❌ Pilih nomor antara 1-{len(images)}!")
        except ValueError:
            print("❌ Masukkan nomor yang valid atau 'all'!")
    
    # Dapatkan mode dan dimensi potongan
    mode, param1, param2 = get_user_input()
    
    if mode == 'pixel':
        print(f"\n📏 Mode terpilih: PIXEL ({param1}x{param2}px)")
    else:
        print(f"\n📐 Mode terpilih: RASIO ({param1}:{param2})")
    
    # Buat folder output
    output_dir = os.path.join(os.getcwd(), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Proses gambar
    print(f"\n🚀 Mulai memproses {len(selected_images)} gambar...")
    print("=" * 50)
    
    success_count = 0
    
    for image_name in selected_images:
        image_path = os.path.join('images', image_name)
        if split_image(image_path, output_dir, mode, param1, param2):
            success_count += 1
    
    # Ringkasan hasil
    print("\n" + "=" * 50)
    print("📊 RINGKASAN HASIL")
    print(f"✅ Berhasil: {success_count}/{len(selected_images)} gambar")
    if success_count > 0:
        print(f"📁 Hasil tersimpan di folder: {output_dir}")
    
    input("\nTekan Enter untuk keluar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Terjadi error yang tidak terduga: {str(e)}")
        input("\nTekan Enter untuk keluar...")