## CONTOH DALAM STUDY CASE

Di sebuah kawasan hutan yang lebat dan terpencil, seorang pendaki solo, bernama Alex, memutuskan untuk menjelajahi pegunungan yang belum pernah dia kunjungi sebelumnya. Namun, tanpa disadari, cuaca berubah drastis menjadi kabut tebal yang menyelimuti sekitar, membuat Alex tersesat di tengah hutan.

Setelah menyadari bahwa dia tersesat, Alex mencoba untuk memanggil bantuan dengan menggunakan sinyal darurat di telepon genggamnya. Tim penyelamat segera dipanggil untuk membantu menemukannya.

Ketika tim penyelamat tiba di lokasi terakhir sinyal Alex, mereka menyadari bahwa kondisi hutan sangat sulit untuk melakukan pencarian yang efektif. Karena kabut tebal, visibilitas sangat rendah, dan medan yang sulit membuat mereka kesulitan menentukan arah yang benar.

Mereka memutuskan untuk menggunakan metode pencarian dengan batasan kedalaman. Kedalaman maksimum yang dipilih adalah lima langkah. Ini berarti bahwa tim penyelamat akan mencari korban hingga jarak lima langkah dari titik awal mereka, tetapi tidak lebih jauh dari itu. Jika dalam jarak lima langkah tersebut mereka tidak menemukan Alex, mereka akan menghentikan pencarian di situ.

Tim penyelamat yang terdiri dari beberapa anggota membagi diri mereka ke dalam kelompok-kelompok kecil dan mulai menyusuri hutan dengan hati-hati. Mereka mencatat setiap langkah mereka dan memeriksa setiap titik yang mereka lewati dengan seksama.

Setelah beberapa jam pencarian yang intensif, salah satu kelompok menemukan jejak sepatu Alex yang terlihat segar di tanah lembab. Mereka mengikuti jejak tersebut dengan hati-hati, berharap dapat menemukan Alex dalam batas kedalaman pencarian yang telah ditetapkan.

Saat mereka mendekati jarak lima langkah terakhir, suara teriakan dari kejauhan terdengar. Tim penyelamat dengan cepat bergerak menuju sumber suara dan menemukan Alex yang telah lelah dan kehausan, tetapi selamat.

Dengan menggunakan metode pencarian dengan batasan kedalaman, tim penyelamat berhasil menemukan Alex dan menyelamatkannya dari keadaan darurat di hutan yang gelap dan berbahaya.


- Inisialisasi Graf:
Representasi hutan dengan graf dilakukan melalui inisialisasi graf menggunakan fungsi initializeGraph(). Setiap simpul dalam graf mewakili titik-titik yang dapat dijangkau dalam hutan, sementara setiap sisi mewakili jalur yang menghubungkan titik-titik tersebut.

- Pencarian dengan Batasan Kedalaman:
Tim penyelamat menggunakan metode pencarian dengan batasan kedalaman (depth-limited search) untuk mencari Alex di dalam hutan yang lebat. Mereka memulai pencarian dari titik awal dan menjelajahi hutan hingga jarak maksimum lima langkah dari titik awal tersebut, sesuai dengan yang diimplementasikan dalam fungsi depthLimitedSearch().

- Iterasi Pencarian:
Tim penyelamat membagi diri ke dalam kelompok-kelompok kecil dan melakukan pencarian secara intensif dengan setiap kelompok mencatat langkah-langkah mereka dan memeriksa setiap titik yang mereka lewati. Iterasi pencarian yang dilakukan oleh setiap kelompok ini mencerminkan proses iteratif dalam algoritma pencarian dengan batasan kedalaman.

- Menemukan Jejak Alex:
Salah satu kelompok penyelamat menemukan jejak sepatu Alex yang segar, yang menciptakan harapan baru untuk menemukan Alex. Hal ini dapat direpresentasikan sebagai penemuan jejak di dalam graf, yang akan menjadi petunjuk bagi tim penyelamat untuk melanjutkan pencarian mereka.

- Mencapai Batas Kedalaman Maksimum:
Saat tim penyelamat mendekati jarak lima langkah terakhir, mereka mendengar suara teriakan dari kejauhan. Hal ini mengindikasikan bahwa mereka telah mencapai batas kedalaman maksimum yang ditetapkan, dan kemudian mereka menemukan Alex dalam batas tersebut.


1. Simpul (Vertices): Merupakan titik-titik atau lokasi dalam hutan yang diwakili dalam struktur data graf. Setiap simpul mungkin memiliki sambungan ke simpul lain dalam graf melalui tepi (edge). Dalam kode ini, simpul direpresentasikan dengan bilangan bulat yang mewakili posisi dalam hutan.

2. Langkah (Steps): Dalam konteks pencarian jalur evakuasi atau penelusuran dalam hutan, "langkah" merujuk pada perpindahan dari satu simpul ke simpul lainnya. Misalnya, jika Alex bergerak dari simpul A ke simpul B, itu dihitung sebagai satu langkah. Dalam kode, setiap langkah dicetak dengan pernyataan printf("Menelusuri langkah: %d\n", currentVertex);.

3. Batas (Depth): Ini berkaitan dengan kedalaman maksimum pencarian dalam algoritma yang digunakan. Dalam pencarian depth-limited atau iterative deepening, batas kedalaman menunjukkan sejauh mana algoritma akan mencoba menemukan solusi sebelum dihentikan. Jika tidak ada jalur yang ditemukan dalam kedalaman ini, pencarian dihentikan. Dalam kode, kedalaman dibatasi oleh nilai maxDepth yang dipilih secara acak.