sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

PagiDanSiang = sesi_pagi & sesi_siang
print(PagiDanSiang)

sesi_hari_ini = sesi_pagi | sesi_siang
print(sesi_hari_ini)

print(len(sesi_hari_ini))