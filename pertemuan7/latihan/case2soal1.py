data_awal = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]
nama_pasien_darurat = "Pasien D (Darurat)"
posisi_sisip = 2


def sisipkan_pasien_darurat_array(data_awal, nama_pasien, posisi):
    if posisi < 0 or posisi > len(data_awal):
        print("Posisi sisip tidak valid.")
        return data_awal

    data_baru = [None] * (len(data_awal) + 1)

    for i in range(posisi):
        data_baru[i] = data_awal[i]

    data_baru[posisi] = nama_pasien

    for i in range(posisi, len(data_awal)):
        data_baru[i + 1] = data_awal[i]

    return data_baru


data_awal = sisipkan_pasien_darurat_array(data_awal, nama_pasien_darurat, posisi_sisip)

print("Data awal pasien:")
for pasien in data_awal:
    print(pasien)