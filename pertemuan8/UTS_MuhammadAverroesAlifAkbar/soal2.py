'''
Sebuah klinik sederhana ingin membangun sistem untuk mencatat data pasien
yang datang berobat. Sistem ini harus mampu menyimpan data pasien,
mengelompokkan jenis penyakit, mencatat status pembayaran, dan mengatur
antrian pemeriksaan dokter.
'''

pasien_hari_ini = [
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit":
"Flu", "bayar": False},
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit":
"Tifus", "bayar": True},
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit":
"Flu", "bayar": False},
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit":
"Maag", "bayar": True},
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit":
"Tifus", "bayar": False},
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False},
]

def info_klinik():
    nama = "Klinik Sehat Bersama"
    alamat = "Jl. Merdeka No. 10, Pekanbaru"
    telp = "0761-12345"
    print("\n========INFO KLINIK========")
    print(f"Nama : {nama}")
    print(f"Alamat : {alamat}")
    print(f"Telp : {telp}")

def rekap_penyakit(pasien_hari_ini):
    print(f"Jenis Penyakit Unik: {''}")
    print(f"Jumlah jenis penyakit: {''}")
    print(f"Rekap per Penyakit: {''}")
    print(f"Penyakit terbanyak: {''}")

info_klinik()
rekap_penyakit(pasien_hari_ini)
