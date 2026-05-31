'''
Sebuah perusahaan logistik bernama "Cepat Sampai" menggunakan sistem kode lokasi gudang
yang berbentuk pohon biner. Setiap gudang (Node) dapat memiliki maksimal dua cabang jalur
distribusi (Left Child dan Right Child).
Manajer operasional perlu melakukan audit rutin untuk memastikan semua gudang terkunjungi.
Ada tiga metode audit yang digunakan:
1. Audit Prioritas (Pre-Order): Mengecek gudang utama sebelum cabang-cabangnya.
2. Audit Berurutan (In-Order): Mengecek dari jalur kiri, lalu pusat, baru ke kanan.
3. Audit Akhir (Post-Order): Mengecek semua cabang terlebih dahulu sebelum kembali ke
gudang pusat.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
    
    def get_leaf_nodes(self, node, leaf_nodes):
        if node is not None:
            if node.left is None and node.right is None:
                leaf_nodes.append(node.data)
            self.get_leaf_nodes(node.left, leaf_nodes)
            self.get_leaf_nodes(node.right, leaf_nodes)

tree = BinaryTree()
tree.insert_root("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
tree.insert_right(tree.root.right, "F")

def in_order(node):
        if node is not None:
            in_order(node.left)
            print(node.data, end=" ")
            in_order(node.right)


def pre_order(node):
        if node is not None:
            print(node.data, end=" ")
            pre_order(node.left)
            pre_order(node.right)


def post_order(node):
        if node is not None:
            post_order(node.left)
            post_order(node.right)
            print(node.data, end=" ")

print("Hasil Audit: ")

print("\n1. Pre-Order: ", end="")
pre_order(tree.root)
print("\n2. In-Order: ", end="")
in_order(tree.root)
print("\n3. Post-Order: ", end="")
post_order(tree.root)

print("\n\nDaftar Gudang Akhir (Leaf Nodes): ", end="")
leaf_nodes = []
tree.get_leaf_nodes(tree.root, leaf_nodes)
print(leaf_nodes)

print("\nAudit Selesai!")