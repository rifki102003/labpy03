# labpy03
## latihan praktek modul ke 3
### Berikut untuk program dan hasil nya 
    NAMA    : MUHAMAD RIFKI
    KELAS   : TI.21.A.1
    NIM     : 312110205
    MATKUL  : BAHASA PEMROGRAMAN
Berikut untuk program nya menggunakan editor pycharm<p>
1. latihan1.py<P>
1.Tampilkan n bilangan acak yang lebih kecil dari 0.5.<p>
2.nilai n diisi pada saat runtime<P>
3.anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya<p>
4.gunakan fungsi random() yang dapat diimport terlebih dahulu
Berikut untuk gambar program nya:<P>
![gambar 1](screenshot/latian1.PNG)

dari hasil tersebut menghasilkan output seperti ini<P>
               
               C:\Users\sdnke\AppData\Local\Programs\Python\Python310\python.exe D:/latihan3ku/labpy03/latihan1.py
               ========================================
               Bilangan random yang lebih kecil dari 0,5
               ========================================
               Masukan nilai n : 5
               Data ke 1  =  0.15096984215079234
               Data ke 2  =  0.21356004612311147
               Data ke 3  =  0.22985332279850357
               Data ke 4  =  0.08450664248444828
               Data ke 5  =  0.4574985262911251

               Process finished with exit code 0
Berikut untuk Algoritma beserta program nya:

    import random

    print(40 * "=")
    print("Bilangan random yang lebih kecil dari 0,5")
    print(40 * "=")
    jum = int(input("Masukan nilai n : "))
    i = 0
    for i in range(jum):
    i += 1
    angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)
Algoritma nya:<p>

    "print" : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.

    "import" : fungsi lanjut yang dipanggil oleh statement import.

    "random" : untuk menentukan suatu pilihan.

    "range" : merupakan fungsi yang menghasilkan list. Fungsi ini akan menciptakan sebuah list baru dengan rentang nilai tertentu.

    "uniform": digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.
2.Algoritma,Program beserta hasil output dari latihan2:<p>
![gambar 2](screenshot/latian5.PNG)

    print("Tugas Pertemuan 7 - Praktikum 3 - Latihan 2")

    xangka=0
    while True:
        xbilangan = int(input("Masukkan Bilangan : "))
        if (xangka < xbilangan):
            xangka=xbilangan
        if (xbilangan == 0):
            break

    print("Bilangan terbesar adalah: ",xangka)
    print()
Berikut adalah Algoritma nya

    "while" : disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

    "int" : berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).

    "if" = Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu.

    "input" : masukan yang kita berikan ke program.

    "break" : fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.

    "print" : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.
Dan ini adalah output dari program di atas:

    C:\Users\sdnke\AppData\Local\Programs\Python\Python310\python.exe D:/latihan3ku/labpy03/latihan2.py
    Tugas Pertemuan 7 - Praktikum 3 - Latihan 2
    Masukkan Bilangan : 10
    Masukkan Bilangan : 9
    Masukkan Bilangan : 8
    Masukkan Bilangan : 7
    Masukkan Bilangan : 6
    Masukkan Bilangan : 5
    Masukkan Bilangan : 0
    Bilangan terbesar adalah:  10


    Process finished with exit code 0
3.program 1 berikut adalah algoritma program dan output nya
![gambar 5](screenshot/latianku.PNG)
program di pycharm<p>
![gambar 3](screenshot/latian3.PNG)
Berikut untuk Algoritma nya:<P>
program dalam bentuk script nya:<P>
    
    a = 100000000
    for i in range(1, 9):
    if (i >= 1 and i <= 2):
        b = a * 0
        print("Laba bulan ke -", i, " = ", b)
    if (i >= 3 and i <= 4):
        c = a * 0.1
        print("Laba bulan ke -", i, " = ", c)
    if (i >= 5 and i <= 7):
        d = a * 0.5
        print("Laba bulan ke -", i, " = ", d)
    if (i == 8):
        e = a * 0.2
        print("Laba bulan ke -", i, " = ", e)
        total = b + b + c + c + d + d + d + e
        print("\nTotal : ", total)
Dan ini adalah algoritma nya:<p>
    
    1.masukkan nilai a

    2.gunakan for untuk perulangan dari 1 sampai 8.Perulangan for disebut counted loop (perulangan yang terhitung)

    3.lalu gunakan if pertama untuk menentukan laba bulan ke 1 dan ke 2.masukan variabel (b) kalikan nilai (a) dengan data bulan 1 dan 2. cetak (x) dan (b)

    4.lalu gunakan if kedua untuk menentukan laba bulan ke 3 dan ke 4.masukan variabel (b) kalikan nilai (a) dengan data bulan 3 dan 4. cetak (x) dan (c)

    5.lalu gunakan if ketiga untuk menentukan laba bulan ke 5 sampai ke 7.masukan variabel (b) kalikan nilai (a) dengan data bulan 5 sampai 7. cetak (x) dan (d)

    6.lalu gunakan if keempat untuk menentukan laba bulan ke 8.masukan variabel (b) kalikan nilai (a) dengan data bulan 8. cetak (x) dan (e)

    7.lalu total keseluruhan.

    8.cetak total
berikut untuk output dari program di atas:<P>
    
    C:\Users\sdnke\AppData\Local\Programs\Python\Python310\python.exe D:/latihan3ku/labpy03/program1.py
    Laba bulan ke - 1  =  0
    Laba bulan ke - 2  =  0
    Laba bulan ke - 3  =  10000000.0
    Laba bulan ke - 4  =  10000000.0
    Laba bulan ke - 5  =  50000000.0
    Laba bulan ke - 6  =  50000000.0
    Laba bulan ke - 7  =  50000000.0
    Laba bulan ke - 8  =  20000000.0

    Total :  190000000.0

    Process finished with exit code 0
Terimakasih kurang lebih nya wassalamuaalikum wr wb.<P>