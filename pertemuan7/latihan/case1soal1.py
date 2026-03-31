history_array = ["google.com", "python.org"]
keyword = "youtube.com"

def tambah_pencarian_array(keyword):
    history_array.append(keyword[:])  # Menambahkan keyword ke dalam history_array
    return history_array
 

tambah_pencarian_array(keyword)

print(history_array)


