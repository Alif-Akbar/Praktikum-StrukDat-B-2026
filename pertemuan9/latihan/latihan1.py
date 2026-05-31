Literasi = ["Laskar Pelangi", "Bumi Manusia", "Sang Pemimpi"]

class Node :
    def __init__(self, judul):
        self.judul = judul
        self.next = None

    def insert_tail():
        judul_buku_baru = input(print(f"Masukkan nama buku yang ingin ditambahkan: "))
        buku_baru = Node(judul_buku_baru)
        Literasi.append(buku_baru)
        print(f"Buku baru {judul_buku_baru}, telah ditambahkan...")

    def print_forward():
        print(Literasi)

    def print_backward():
        print(Literasi[::-1])

    def delete_by_judul():
        judul_buku_dihapus = input(print(f"Masukkan nama buku yang ingin dihapus: "))
        Literasi.remove(judul_buku_dihapus)
        print(f"Buku {judul_buku_dihapus}, telah dihapus...")

while True:
    print(f"(Tambah)                : Menambah buku baru ke Toko Buku 'Literasi'")
    print(f"(Lihat Urutan)          : Melihat urutan Toko Buku 'Literasi'")
    print(f"(Lihat Urutan Terbalik) : Melihat urutan Toko Buku 'Literasi' secara terbalik")
    print(f"(Hapus)                 : Menghapus buku lama dari Toko Buku 'Literasi'")
    n = input(print(f"Selamat datang di Toko Buku 'Literasi'! Ada yang bisa kami bantu? (T/LU/LT/H): ")).upper()
    

    if n == "T" :
        print(Node.insert_tail())
    elif n == "LU" :
        print(Node.print_forward())
    elif n == "LT" :
        print(Node.print_backward())
    elif n == "H" :
        print(Node.delete_by_judul())
    else :
        print(f"Maaf, pilihan yang Anda masukkan tidak valid. Silakan coba lagi.")