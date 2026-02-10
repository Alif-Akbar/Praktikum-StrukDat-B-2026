kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

# Mata kuliah yang diambil kedua kelas
mata_kuliah_kedua_kelas = kelas_A.intersection(kelas_B)
print("Mata kuliah yang diambil kedua kelas:", mata_kuliah_kedua_kelas)

# Mata kuliah yang hanya diambil kelas A
mata_kuliah_hanya_kelas_A = kelas_A.difference(kelas_B)
print("Mata kuliah hanya diambil kelas A:", mata_kuliah_hanya_kelas_A)

# Mata kuliah unik yang diambil oleh kelas A dan B
mata_kuliah_unik = kelas_A.union(kelas_B)
print("Mata kuliah unik yang diambil oleh kelas A dan B:", mata_kuliah_unik)