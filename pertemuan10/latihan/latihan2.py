class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return len(self.StackLinkedList) == 0
    
    def push(self, url):
        new_node = Node(url)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.url

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.url

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size + 1


myStack = StackLinkedList()
myStack.push('www.google.com')
myStack.push('www.youtube.com')
myStack.push('www.tiktok.com')
myStack.push('www.instagram.com')


print("Histori browser terakhir: ", myStack.peek())
print("Histori browser yang dihapus setelah di Undo: ", myStack.pop())
print("Apakah stacknya kosong? ", myStack.isEmpty())
print("Panjang stacknya adalah: ", myStack.stackSize())














HistoryBrowser = StackLinkedList()