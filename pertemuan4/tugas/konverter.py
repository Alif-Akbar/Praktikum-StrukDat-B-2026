# konversi mata uang

from kurs import kurs

def konversi_mata_uang(jumlah, mata_uang_asal, mata_uang_tujuan):
    if mata_uang_asal not in kurs or mata_uang_tujuan not in kurs:
        raise ValueError("Mata uang tidak valid.")

    jumlah_tujuan = jumlah * (kurs[mata_uang_asal] / kurs[mata_uang_tujuan])
    
    return jumlah_tujuan

