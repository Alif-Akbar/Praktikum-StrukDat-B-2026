'''
Binary Search Tree efisien menggunakan inorder traversal untuk mengurutkan data.
Namun, untuk menyisipkan data baru, kita perlu memastikan bahwa data tersebut ditempatkan
pada posisi yang benar agar tetap mempertahankan sifat BST. Berikut adalah implementasi
sederhana dari Binary Search Tree dengan metode insert dan inorder traversal:
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Langkah 1
        new = Node(data)

        # Langkah 2
        if self.root == None:
            self.root = new
            return
        
        # Jika tidak, Langkah 3
        p = self.root
        q = self.root

        # Langkah 4
        while q != None and new.data != p.data:

            # Langkah 5
            p = q

            # Langkah 6
            if new.data < p.data:
                q = p.left
            else:
                q = p.right

        # Langkah 7
        if new.data == p.data:
            print("Datanya duplikat!")
            return
        
        # Jika tidak, Langkah 8
        if new.data < p.data:
            # Jika iya
            p.left = new
        else:
            # Jika tidak
            p.right = new
        
        # Selesai


bst = BinarySearchTree()

bst.insert(34)
bst.insert(37)
bst.insert(56)
bst.insert(29)
bst.insert(41)

def in_order(node):
        if node is not None:
            in_order(node.left)
            print(node.data, end=" ")
            in_order(node.right)

in_order(bst.root)