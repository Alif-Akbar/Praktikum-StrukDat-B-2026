kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]


for datamahasiswa in kumpulan_nilai:
    nama = datamahasiswa[0]
    nilai = datamahasiswa[1]
    if nilai >= 75:
        print(f"Selamat {nama}, Anda Lulus!")
    else:
        print(f"Maaf {nama}, Anda harus remidi.")

