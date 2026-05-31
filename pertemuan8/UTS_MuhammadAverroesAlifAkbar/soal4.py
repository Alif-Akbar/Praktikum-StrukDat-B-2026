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

class Node():
    def __init__(self):
        pass

    def tambah(data):
        data.append()

    def tampilkan(data):
        return data
    
    def panggil_berikutnya():
        
        for i in pasien_hari_ini:
            print(pasien_hari_ini(i+1))

    def cari(data):
        print(data in pasien_hari_ini)
        
    def hapus_berdasarkan_id(id):
        data.remove(id)

    def hitung(data):
        print(len(data))
    
antrian = pasien_hari_ini()

antrian.tambah({"id": "P001", "nama": "Andi", "penyakit":
"Flu"})
antrian.tambah({"id": "P002", "nama": "Budi", "penyakit":
"Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici", "penyakit":
"Flu"})
antrian.tambah({"id": "P004", "nama": "Dani", "penyakit":
"Maag"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("P003")
antrian.tampilkan()
