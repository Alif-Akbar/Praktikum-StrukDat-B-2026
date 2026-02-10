angka = [10, 20, 30, 40, 50]


angka.append(60) # Menambahkan 60 ke dalam list
angka.remove(20) # Menghapus 20 dari list
print(angka) # Menampilkan isi list setelah operasi append dan remove


total = sum(angka) # Menghitung jumlah semua elemen dalam list
jumlah_elemen = len(angka) # Menghitung jumlah elemen dalam list
rata_rata = total / jumlah_elemen if jumlah_elemen > 0 else 0 # Menghitung rata-rata
print(f"Rata-rata: {rata_rata}")


print(angka)

