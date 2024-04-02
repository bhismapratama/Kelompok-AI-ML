# Studi Kasus: Penjadwalan Pengiriman Barang

## Deskripsi
Studi kasus ini membahas penggunaan algoritma pencarian untuk meningkatkan efisiensi pengiriman barang antar kota dalam suatu perusahaan logistik. Dalam implementasi ini, digunakan pendekatan A*, Weighted A*, dan Greedy untuk menemukan rute terbaik dari titik awal ke titik tujuan, dengan mempertimbangkan estimasi waktu atau biaya.

## Langkah-langkah Penyelesaian
1. **Pemodelan Data:** Setiap kota diwakili sebagai simpul dalam graf, dengan jalur pengiriman antar kota sebagai sisi-sisi graf. Struktur data graf dibangun menggunakan representasi adjacency list.
2. **Heuristik:** Heuristik digunakan untuk memperkirakan biaya dari setiap simpul ke tujuan akhir, membantu meningkatkan efisiensi pencarian.
3. **Pencarian Rute:** Algoritma pencarian A*, Weighted A*, dan Greedy digunakan untuk menemukan rute terpendek atau tercepat dari titik awal ke titik tujuan.
4. **Evaluasi dan Analisis:** Kinerja setiap algoritma dievaluasi berdasarkan jumlah simpul yang dieksplorasi dan dipilih untuk solusi, membantu dalam pemilihan algoritma yang sesuai dengan kebutuhan.

## Implementasi Kode
- Implementasi kode Python disediakan dalam file `main.py`.
- Pengguna dapat menjalankan skrip dan memilih algoritma yang ingin digunakan serta memberikan bobot jika menggunakan Weighted A*.
- Data graf dan heuristik dihasilkan secara acak untuk mencerminkan situasi nyata dalam jaringan distribusi barang.

## Penggunaan
1. Pastikan Python telah terpasang di komputer Anda.
2. Jalankan `main.py` dan ikuti instruksi yang diberikan untuk memilih algoritma dan memberikan bobot jika diperlukan.

## Kontribusi
Kontribusi terhadap perbaikan kode atau peningkatan fitur selalu dipersilakan. Silakan buka pull request untuk saran atau perubahan yang diinginkan.

## Lisensi
Tidak ada lisensi khusus yang diberikan untuk implementasi ini. Namun, silakan merujuk atau memberikan kredit jika Anda menggunakan kode atau konsep dari sini.

