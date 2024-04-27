# SOAL
Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar.

syarat UTS :
1. Kerjakan dengan menggunakan bahasa pemrograman python.
2. Menggunakan protokol UDP.
3. Code untuk server dan client dikumpulkan di github repostory masing masing. 
4. Pada readme.md silahkan beri penjelasan how code works.
5. Pada readme.md silahkan berikan screenshot cara penggunaan serta contoh ketika program berjalan. 
6. Test case : 1 server 10 client. 
7. Pastikan memahami soal.
8. Silahkan kumpulkan link respostory di assignment ini.
 --- JANGAN TELAT ! ---

# APA ITU PROTOKOL UDP
UDP adalah singkatan dari User Datagram Protocol. Ini adalah salah satu protokol komunikasi dalam jaringan komputer yang beroperasi di lapisan transport dalam model referensi OSI (Open Systems Interconnection). UDP adalah protokol yang berorientasi pada koneksi, yang berarti tidak ada koneksi langsung yang ditetapkan sebelum data dikirimkan, dan tidak ada konfirmasi penerimaan yang dijamin.

Berikut beberapa karakteristik utama dari UDP:
1. **Tanpa Koneksi (Connectionless)**: UDP tidak memerlukan pembangunan koneksi sebelum mengirim data. Setiap pesan dikirimkan secara independen, tanpa memperhatikan pesan sebelumnya atau sesudahnya.
2. **Tidak Handal (Unreliable)**: UDP tidak menjamin pengiriman paket yang sukses atau pengiriman yang terurut. Ini berarti bahwa data yang dikirim melalui UDP dapat hilang, duplikat, atau tiba di urutan yang salah.
3. **Ringan (Lightweight)**: Karena tidak memiliki overhead yang terkait dengan pembangunan koneksi atau mekanisme pemulihan kesalahan, UDP seringkali lebih cepat daripada protokol lain seperti TCP.
4. **Tidak Terjamin (Unacknowledged)**: UDP tidak memiliki mekanisme pengiriman ulang paket atau konfirmasi penerimaan. Ini membuatnya lebih cepat, tetapi juga berarti bahwa tidak ada jaminan bahwa data akan tiba di tujuan.

UDP sering digunakan untuk aplikasi yang memerlukan komunikasi yang cepat dan efisien, seperti video streaming, VoIP (Voice over IP), dan permainan daring (online games). Meskipun kurang handal daripada protokol lain seperti TCP, UDP tetap menjadi pilihan yang baik dalam beberapa kasus ketika kecepatan dan efisiensi lebih penting daripada keandalan.

# PENJELASAN CODINGAN
# 1. Server

Pertama, mengimpor modul *socket* yang memungkinkan kita untuk menggunakan fungsi-fungsi yang diperlukan untuk membuat dan mengelola socket di Python. Disini saya juga mengimpor modul *random* dan *time*. Modul *random* digunakan untuk memilih kata warna secara acak, sedangkan modul *time* digunakan untuk mengatur waktu antara pengiriman kata warna kepada klien.

Selanjutnya ada *COLOR_TRANSLATION* ini adalah kamus yang berisi daftar kata warna dalam bahasa Inggris dan terjemahannya dalam bahasa Indonesia. Kamus ini akan digunakan oleh server untuk memeriksa jawaban yang diberikan oleh klien.

Fungsi dari codingan diatas adalah untuk mengirim pesan kepada semua klien yang terhubung ke server. Fungsi ini menerima socket server, pesan yang akan dikirim, dan daftar alamat klien yang terhubung.

codingan berikutnya yang ada diatas digunakan untuk menerima pesan dari klien. Fungsi ini menerima socket server dan mengembalikan pesan yang diterima beserta alamat klien yang mengirim pesan.

Berikutnya dan yang terakhir untuk server, ada Fungsi utama yang menjalankan logika permainan server. Ini menciptakan socket UDP, mengikatnya ke alamat localhost pada port 12345, dan kemudian mulai menunggu koneksi dari klien. Setelah klien terhubung, server mengirimkan kata warna dalam bahasa Inggris kepada semua klien, menerima jawaban dari klien, memeriksa jawaban yang diberikan, dan memberikan umpan balik kepada klien. Selain itu, server juga memeriksa apakah ada klien baru yang ingin terhubung dan menambahkannya ke dalam daftar klien yang terhubung. Proses ini berlangsung secara berulang dengan interval waktu tertentu menggunakan fungsi *time.sleep(10)*.

# 2. Client

Kode ini dimulai dengan mengimpor modul socket, yang akan digunakan untuk membuat dan mengelola koneksi jaringan.

__Receive from server__

Ini adalah fungsi yang digunakan untuk menerima pesan dari server. Fungsi ini mengambil socket klien sebagai argumen dan menerima pesan dari server menggunakan metode recvfrom(). Panjang maksimum pesan yang dapat diterima adalah 1024 byte.

__Send response to server__

Fungsi ini mengirimkan jawaban dari klien ke server. Ini menerima socket klien dan jawaban yang akan dikirim sebagai argumen, kemudian mengirimnya ke alamat server yang telah ditentukan.

__Inisialisasi Socket UDP__

Di sini, socket UDP untuk klien diinisialisasi menggunakan *socket.socket()*. Parameter *socket.AF_INET* menunjukkan bahwa klien akan menggunakan alamat IP versi 4 dan *socket.SOCK_DGRAM* menunjukkan bahwa klien akan menggunakan protokol UDP.

__Alamat Server__

Ini adalah alamat server yang akan dihubungi oleh klien. Dalam hal ini, server berjalan pada localhost (mesin yang sama dengan klien) dan port 12345.

__Membangun koneksi dengan server__

Klien mengirim pesan "connect" ke server menggunakan metode sendto() socket UDP.

Pada kode di atas, terdapat logika untuk mengirim pesan *"connect"* ke server saat klien pertama kali terhubung. Ini bertindak sebagai tanda bahwa klien telah terhubung ke server dan siap untuk bermain. Setelah itu, klien memasuki loop utama yang akan terus berjalan hingga klien dihentikan. Pada setiap iterasi loop, klien menerima kata warna dari server, meminta input dari pengguna untuk menebak warna dalam bahasa Indonesia, mengirimkan jawaban ke server, dan menerima umpan balik dari server.

Jika jawaban yang diberikan oleh klien benar, skor diatur menjadi 100. Namun, ketika jawaban salah maka akan diberikan skor 0 Jika ingin menjaga skor klien dan hanya mengatur ulang skor ketika klien baru mulai bermain.

__Penanganan Exception__

Bagian ini menangani penutupan koneksi dan membersihkan sumber daya saat klien dihentikan, baik karena pengguna menekan Ctrl+C atau ada kesalahan lain.

# 3. Output

Untuk outputnya jika server telah memilih kata warna "red" dan mengirimkannya ke klien, klien mungkin akan menerima pesan "Received color: red". Klien kemudian dapat memasukkan jawaban yang benar atau salah, dan server akan memberikan umpan balik sesuai dengan jawaban tersebut.

Namun, server tidak peduli apakah pesan sudah terkirim atau belum karena UDP merupakan protokol tanpa koneksi yang tidak menjamin pengiriman paket yang berhasil. Dalam konteks permainan ini, karena tidak ada koneksi langsung yang ditetapkan antara klien dan server sebelum pengiriman pesan, server tidak mengetahui apakah pesan yang dikirim berhasil atau tidak. Ini membuat implementasi yang sederhana dan efisien, tetapi kurang andal daripada protokol yang memerlukan koneksi seperti TCP.

Sebagai contoh, server mungkin akan terus berlanjut ke langkah berikutnya dalam permainan setelah mengirimkan pesan ke klien, tanpa menunggu konfirmasi bahwa pesan tersebut telah diterima. Dalam kasus jaringan yang stabil, pesan dapat dikirim dan diterima tanpa masalah. Namun, dalam kasus jaringan yang tidak stabil atau memiliki latensi tinggi, ada kemungkinan bahwa pesan tidak akan sampai ke klien atau sampai terlambat. Dalam situasi seperti itu, penggunaan UDP memungkinkan permainan untuk terus berjalan tanpa menghentikan atau mengganggu proses.
