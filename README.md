# Tubes-Jarkom

Program yang dibuat untuk memenuhi tugas besar mata kuliah Jaringan Komputer terkait *Web Server* dan *Web Client*

## Rincian tugas:
Yang harus dipenuhi dan dinilai:
1. Implementasi pembuatan TCP socket dan mengaitkannya ke alamat dan port tertentu (poin: 20)
2. Program web server dapat menerima dan memparsing HTTP request yang dikirimkan oleh browser (poin: 20)
3. Web server dapat mencari dan mengambil file (dari file system) yang diminta oleh client (poin: 15)
4. Web server dapat membuat HTTP response message yang terdiri dari header dan konten file yang diminta (poin: 20)
5. Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client (poin: 15)
6. Jika file yang diminta oleh client tidak tersedia, web server dapat mengirimkan pesan “404 Not Found” dan dapat ditampilkan dengan benar di sisi client. (poin: 10)

## Batasan:
Server hanya bisa memenuhi *request* file html yang isinya adalah teks (bukan gambar).

## Kebutuhan:
- Python

## Cara penggunaan:
1. Hidupkan web server dengan pergi ke terminal dan jalankan program server.py, dengan command: 
```
py server.py
```
2. Untuk melakukan *request* yang valid melalui *browser client*, masukkan URL berikut pada browser: https://localhost:23489/index.html 
3. Akan ditampilkan hasil berupa tampilan html “Selamat Datang”.
4. Untuk melakukan *request* yang tidak valid, ganti index pada URL di atas, contohnya:  https://localhost:23489/inde.html 
5. Akan ditampilkan hasil berupa tampilan html “404 Page Not Found”.
6. Untuk melakukan *request* melalui *terminal client*, jalankan kode client.py, dengan command:
```
py client.py
```
7. Akan ditampilkan hasil berupa teks respons "HTTP 200 OK" dan isi kodingan dari file HTML yang diminta.
