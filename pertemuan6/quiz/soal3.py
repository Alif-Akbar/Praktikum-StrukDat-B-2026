from soal2 import katalog
import soal3

riwayat_transaksi = {}

def proses_transaksi(katalog, nama_buku, jumlah_beli, stok):
    beli_buku = input("Masukkan buku yang ingin dibeli:")
    if stok in katalog < 0:
        print("Maaf, Stok Habis.")
    if nama_buku not in katalog:{'nama':beli_buku}:
        print("Maaf, Buku yang kamu cari tidak ada.")
        return None
    if nama_buku in katalog:{'nama':beli_buku}:
        return katalog 

proses_transaksi()