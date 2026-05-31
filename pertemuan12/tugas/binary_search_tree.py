'''
Perpustakaan Digital "Ilmu Terang" ingin mengelola katalog buku mereka agar pencarian
buku menjadi lebih cepat. Saat ini, mereka memiliki ribuan data buku, namun sistem pencariannya
masih menggunakan metode linear yang lambat.
Pustakawan senior, Pak Andi, memutuskan untuk menggunakan struktur data Binary
Search Tree (BST). Dalam sistem ini, setiap buku akan memiliki ID Buku (angka unik). Buku
dengan ID yang lebih kecil dari root akan diletakkan di cabang kiri, dan ID yang lebih besar akan
diletakkan di cabang kanan.
Sari, mahasiswi magang kita, diminta kembali untuk membuat simulasi sistem katalog ini
menggunakan Linked List manual untuk membentuk struktur Tree.
'''

class Node:
    def __init__(self, judul, id_buku):
        self.judul = judul
        self.id_buku = id_buku
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, judul, id_buku):
        new_node = Node(judul, id_buku)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif id_buku > current.id_buku:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                print("ID Buku sudah ada!")
                return
    
    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"ID Buku: {node.id_buku}, Judul: {node.judul}")
            self.traversal_inorder(node.right)
    
    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def get_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

rak_buku = BinarySearchTree()

rak_buku.insert("Dasar Pemrograman", 50)
rak_buku.insert("Struktur Data", 30)
rak_buku.insert("Kecerdasan Buatan", 70)
rak_buku.insert("Matematika Diskrit", 20)
rak_buku.insert("Basis Data", 40)
rak_buku.insert("Jaringan Komputer", 60)
rak_buku.insert("Sistem Operasi", 80)

print("[INFO] Koleksi Buku (Inorder Traversal):")
rak_buku.traversal_inorder(rak_buku.root)

print("\n[INFO] Mencari Buku dengan ID 60:")
buku = rak_buku.search(60)
if buku:
    print(f"Buku ditemukan: {buku.judul}")
else:
    print("Buku tidak ditemukan.")

print("\n[INFO] Mencari Buku dengan ID 100:")
buku = rak_buku.search(100)
if buku:
    print(f"Buku ditemukan: {buku.judul}")
else:
    print("Buku tidak ditemukan.")

print("\n[INFO] ID terkecil:")
min_buku = rak_buku.get_min(rak_buku.root)
print(f"ID Buku: {min_buku.id_buku}, Judul: {min_buku.judul}")
print("\n[INFO] ID terbesar:")
max_buku = rak_buku.get_max(rak_buku.root)
print(f"ID Buku: {max_buku.id_buku}, Judul: {max_buku.judul}")

print("\n[INFO] Tinggi (Height) Tree:")
print(rak_buku.height(rak_buku.root))