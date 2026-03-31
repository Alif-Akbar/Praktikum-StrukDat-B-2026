class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    class AntrianLinkedList:
        def __init__(self):
            self.head = None

        def insert_at_position (self, nama_pasien, posisi):
            new_node = Node(nama_pasien)

            if posisi < 0:
                print("Posisi sisip tidak valid.")
                return

            if posisi == 0:
                new_node.next = self.head
                self.head = new_node
                return

            current = self.head
            count = 0

            while current is not None and count < posisi - 1:
                current = current.next
                count += 1

            if current is None:
                print("Posisi sisip melebihi panjang daftar.")
                return

            new_node.next = current.next
            current.next = new_node

    def tampilkan_antrian(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

