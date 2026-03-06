import soal3

level_diskon = (
 (500000, 15), 
 (300000, 10), 
 (100000, 5), 
 (0, 0), 
)

def hitung_diskon (harga, total_belanja, level_diskon, index=0):
    harga = input()
    if harga > index(2,0):
        if harga > index(1,0):
            if harga > index(0,0):
                level_diskon = index(0,1)
            else:
                level_diskon = index=(1,1)
        else:
            level_diskon = index=(2,1)
    else:
        level_diskon = index=(3,1)       

                        