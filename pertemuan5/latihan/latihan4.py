transaksi = [{"produk":"Buku", "harga":10000, "jumlah":3},
              {"produk":"Pena", "harga":5000, "jumlah":10},
              {"produk":"Penghapus", "harga":2000, "jumlah":2}]

transaksi[0]["jumlah"] = 8

transaksi.append({"produk":"Pensil", "harga":1500, "jumlah":5})
transaksi.append({"produk":"Penggaris", "harga":3000, "jumlah":7})

for item in transaksi:
    total_harga = item["harga"] * item["jumlah"]
    print(f"Produk: {item['produk']} | Total: {total_harga}")



