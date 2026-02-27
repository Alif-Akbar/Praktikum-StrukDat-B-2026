# membuat aplikasi konversi mata uang sederhana menggunakan dictionary
# untuk menyimpan kurs mata uang dan fungsi untuk melakukan konversi.

from tabulate import tabulate

import kurs
from konverter import konversi_mata_uang

print(kurs.tampilkan_kurs())

mata_uang_asal = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
mata_uang_tujuan = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

konversi_mata_uang = konversi_mata_uang(jumlah, mata_uang_asal, mata_uang_tujuan)
print(f"{jumlah} {mata_uang_asal} = {konversi_mata_uang:.2f} {mata_uang_tujuan}")
