# test.py
# Contoh penggunaan colorama untuk mencetak teks berwarna di terminal

from colorama import init, Fore, Back, Style

init()  # Initialize colorama


print(Fore.RED + 'Teks Merah')
print(Fore.GREEN + 'Teks Hijau')
print(Fore.BLUE + Back.YELLOW + 'Teks Biru, Bg Kuning')
print(Style.RESET_ALL + 'Kembali Normal')