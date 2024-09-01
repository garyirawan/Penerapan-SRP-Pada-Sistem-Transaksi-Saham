<h1>Penerapan SRP Pada Sistem Transaksi Saham</h1>

<h3>Deskripsi Proyek</h3>
Proyek ini merupakan implementasi dari Single Responsibility Principle (SRP) pada sistem transaksi saham sederhana. SRP adalah salah satu prinsip dari SOLID yang menyatakan bahwa sebuah kelas harus memiliki satu tanggung jawab atau alasan untuk berubah. Dalam proyek ini, sistem transaksi saham dibangun dengan memisahkan tanggung jawab masing-masing komponen agar lebih modular, mudah dipelihara, dan dapat dikembangkan di masa depan.

<br>Dalam penerapan SRP yang sudah dilakukan, saya memisahkan sistem transaksi saham sederhana ke dalam 4 *class*, yaitu:</br>

1. `StockTransaction`: Bertugas untuk menyimpan informasi dasar tentang transaksi saham, seperti simbol saham, jumlah saham, dan harga. </br>
2. `TransactionValidator`: Bertanggung jawab untuk melakukan validasi terhadap transaksi saham, memastikan bahwa transaksi tersebut sah dan dapat dilanjutkan. </br>
3. `TransactionExecutor`: Mengurus pelaksanaan transaksi, seperti memperbarui jumlah saham yang dimiliki setelah transaksi terjadi. </br>
4. `TransactionReportGenerator`: Berfungsi untuk membuat laporan yang merinci detail transaksi saham tersebut.
