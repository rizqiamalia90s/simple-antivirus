# simple-antivirus
Terbantu dengan kode buatanku? tag aku atau cantumkan sumber ya!

Kode Program antivirus sederhana dengan bahasa Pemrograman Python dan databases Microsoft Access 2013, bagaimana membuat antivirus sederhana? ayo masuk ke skenario buatanku!

Dalam repositori ini terdiri dari beberapa file seakan berada didalam sebuah pc, mari aku jelaskan :
1. folder app berisi aplikasi bernama CSP.exe aplikasi ini akan menjadi virus
2. folder code berisi file kode yaitu hello world.py dan yang akan menjadi virus adalah fake_virus1.py
3. folder picture berisi file gambar bernama fake_virus2.png
4. file db.dat adalah database Microsoft Access 2013
5. untuk file database nama disamarkan menjadi .dat dalam skenario ini agar file database tidak dicurigai sebagai database guna meningkatkan keamanan
6. terakhir file scanner.py adalah sebagai aplikasi antivirus

Antivirus sederhana ini memerlukan modul pyodbc dan psutils jangan lupa untuk diinstall, antivirus ini juga dilengkapi fitur pindai file (apakah file ini adalah virus), tampilkan proses berjalan, ganti folder, listing folder, baca file, kill proses, dan hapus file (beberapa ada di repo sebelumnya).

Bagaimana cara eksekusi nya?
Kalian bisa jalankan salah satu virus dan mulai run scanner.py lalu melakukan baca proses yang ada di task manager, kemudian kill dan hapus. Mulailah membuat program!

Disclaimer !
- virus hanyalah sebagai contoh, tidak membahayakan sistem sama sekali
- ketiga virus buatan sudah berada dalam list antivirus sehingga virus dapat dideteksi sebagai file atau proses yang mencurigakan
- jangan asal eksekusi virus jika belum memahami betul instruksi
- virus yang tidak membahayakan ini harus tetap dimatikan (agar tidak memberatkan proses) dengan cara di kill dengan menu kill kemudian di hapus
- jangan langsung menghapus file sebelum di kill
