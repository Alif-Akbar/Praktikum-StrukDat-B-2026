nilai = [70, 85, 90, 65, 80]

nilai[3] = 75

nilai.append(95)
urutan_nilai = sorted(nilai, reverse=True)
print(urutan_nilai)

jumlah_nilai = sum(nilai)
print(jumlah_nilai)

if 100 in nilai is True:
    print("Ada nilai sempurna")
else:
    print("Tidak Ada")