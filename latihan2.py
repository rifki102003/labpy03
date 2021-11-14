print("Tugas Pertemuan 7 - Praktikum 3 - Latihan 2")

angka=0
while True:
    bilangan = int(input("Masukkan Bilangan : "))
    if (angka < bilangan):
        angka=bilangan
    if (bilangan == 0):
        break

print("Bilangan terbesar adalah: ",angka)
print()