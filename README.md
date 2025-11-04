# Split Image Program

Program Python untuk memotong gambar menjadi bagian-bagian yang lebih kecil berdasarkan dimensi yang ditentukan.

## Fitur

- ✅ Memotong gambar berdasarkan dimensi width dan height dalam pixel
- ✅ Mendukung berbagai format gambar (PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP)
- ✅ Interface CLI yang user-friendly
- ✅ Dapat memproses satu gambar atau semua gambar sekaligus
- ✅ Otomatis membuat folder output terorganisir
- ✅ Menampilkan progress dan informasi detail

## Cara Penggunaan

### 1. Persiapan
```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Letakkan Gambar
- Masukkan gambar yang ingin dipotong ke dalam folder `images/`
- Program mendukung format: PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP

### 3. Jalankan Program
```bash
python split_image.py
```

### 4. Ikuti Instruksi
- Pilih gambar yang ingin dipotong
- Masukkan dimensi potongan:
  - **Width** (lebar) dalam pixel
  - **Height** (tinggi) dalam pixel

### 5. Hasil
- Potongan gambar akan disimpan di folder `output/`
- Setiap gambar akan memiliki folder terpisah
- Nama file: `namafile_row01_col01.ext`

## Contoh Penggunaan

```
🎨 PROGRAM SPLIT IMAGE
==================================================

📁 Gambar yang tersedia:
----------------------------------------
1. foto.jpg (1920x1080px)
2. gambar.png (800x600px)

🔍 Pilih gambar yang ingin dipotong:
Masukkan nomor gambar (1-2) atau 'all' untuk semua gambar: 1

⚙️  Pengaturan Split Image
----------------------------------------
Masukkan lebar potongan (width) dalam pixel: 640
Masukkan tinggi potongan (height) dalam pixel: 360

🚀 Mulai memproses 1 gambar...
==================================================

🖼️  Memproses: foto.jpg
   Ukuran asli: 1920x1080px
   Akan dipotong menjadi: 3 kolom x 3 baris = 9 potongan
   ✅ Potongan 1/9: foto_row01_col01.jpg (640x360px)
   ✅ Potongan 2/9: foto_row01_col02.jpg (640x360px)
   ...
   🎉 Selesai! 9 potongan disimpan di: output/foto
```

## Struktur Folder

```
split-image/
├── images/          # Letakkan gambar sumber di sini
├── output/          # Hasil potongan akan tersimpan di sini
│   └── namafile/    # Folder terpisah untuk setiap gambar
├── split_image.py   # Program utama
├── requirements.txt # Dependencies
└── README.md       # Dokumentasi
```

## Persyaratan Sistem

- Python 3.6 atau lebih baru
- Pillow (PIL) library
- Windows/Linux/MacOS

## Troubleshooting

### Error "Folder 'images' tidak ditemukan"
- Pastikan folder `images` ada di direktori yang sama dengan `split_image.py`
- Atau jalankan program sekali, folder akan dibuat otomatis

### Error "Tidak ada gambar yang ditemukan"
- Pastikan file gambar ada di folder `images`
- Periksa format file (harus PNG, JPG, JPEG, GIF, BMP, TIFF, atau WEBP)

### Error memory untuk gambar besar
- Gunakan dimensi potongan yang lebih kecil
- Proses gambar satu per satu instead of 'all'

## Lisensi

Program ini free untuk digunakan dan dimodifikasi.