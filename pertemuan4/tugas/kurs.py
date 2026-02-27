# kurs mata uang

import tabulate

kurs = {
    'IDR': 13875,
    'USD': 16875,
    'EUR': 19995,
    'SGD': 13360,
    'JPY': 109,
    }

def tampilkan_kurs():
    print(tabulate.tabulate(kurs.items(), headers=["Mata Uang", "Kurs"], tablefmt="grid"))
    