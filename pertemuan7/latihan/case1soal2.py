class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def tambah_pencarian_linked(node_baru, head):
        if head is None:
            head = node_baru
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = node_baru
        return head
    def tampilkan_history_linked(head):
        current = head
        while current is not None:
            print(current.data)
            current = current.next    

node1 = Node(1)
node2 = Node(4)
node3 = Node(9)
node4 = Node(16)
node5 = Node(25)

head = None
head = HistoryLinkedList.tambah_pencarian_linked(node1, head)
head = HistoryLinkedList.tambah_pencarian_linked(node2, head)
head = HistoryLinkedList.tambah_pencarian_linked(node3, head)
head = HistoryLinkedList.tambah_pencarian_linked(node4, head)
head = HistoryLinkedList.tambah_pencarian_linked(node5, head)
HistoryLinkedList.tampilkan_history_linked(head)

