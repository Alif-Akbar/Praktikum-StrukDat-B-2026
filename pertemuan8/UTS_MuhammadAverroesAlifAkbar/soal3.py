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

class Pasien():
    def __init__(self, __id, __nama, __penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit

    def tampilkan_info():
        for pasien in pasien_hari_ini:
            print(pasien)
    
    def hitung_pasien():
        for pasien in pasien_hari_ini:
            print(sum(pasien))

    class PasienPrioritas():
        def Prioritas(Darurat, Biasa):
            for pasien in pasien_hari_ini:
                for penyakit in pasien:
                    if penyakit is Tifus :
                        print("** Segera tangani! **")

Pasien.hitung_pasien()
Pasien.tampilkan_info()
Pasien.PasienPrioritas.Prioritas()
