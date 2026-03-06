from soal2 import katalog

def tambah_buku (nama, harga, stok):
    nama = input("Masukkan Barang yang Dicari:")
    if stok < 0 :
        print("Error...")
        return None
    if stok >= 0 :
        tambah_stok = int(input("Masukkan Stok tambahan:"))
        stok in katalog
        {'nama':nama} += tambah_stok
        return {'nama', 'harga', 'stok'}

tambah_buku()