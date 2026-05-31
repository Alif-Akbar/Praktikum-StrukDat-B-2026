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


def tampilkan_pasien():
    for pasien in pasien_hari_ini:
        print(pasien)

def filter_belum_bayar(nama, bayar):
    pasien_belum_bayar = []
    for pasien in pasien_hari_ini:
        if bayar in pasien is False :
            pasien_belum_bayar.append(nama in pasien)
    print(f"Pasien yang belum melunasi pembayaran : {pasien_belum_bayar}")        

tampilkan_pasien()
filter_belum_bayar(pasien_hari_ini, bayar="bayar" in pasien_hari_ini)
