mahasiswa = {
"A001": {"nama": "Alif", "prodi": "Informatika","ipk": 3.45},
"A002": {"nama": "Pandi", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Alam", "prodi": "Informatika", "ipk": 3.75}
}

# Menampilkan nama mahasiswa dengan IPK >= 3.5
for nim, data in mahasiswa.items():
    if ipk := data.get("ipk"):
        if ipk >= 3.5:
            print(f"{data['nama']} (NIM: {nim})")

# Menghitung rata-rata IPK semua mahasiswa
total_ipk = sum(data["ipk"] for data in mahasiswa.values())
jumlah_mahasiswa = len(mahasiswa)
rata_rata_ipk = total_ipk / jumlah_mahasiswa if jumlah_mahasiswa > 0 else 0
print(f"Rata-rata IPK mahasiswa: {rata_rata_ipk:.2f}")

# Menambahkan mahasiswa baru
mahasiswa["A004"] = {"nama": "Dewi", "prodi": "Teknik Komputer", "ipk": 3.60}
print("Data mahasiswa setelah penambahan:")
for nim, data in mahasiswa.items():
    print(f"{nim}: {data}")

       