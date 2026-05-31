stack = []

# Push
stack.append("Buku A")
stack.append("Buku B")
stack.append("Buku C")

print("Stack:", stack)

# Peek
buku_teratas = stack[-1]
print("Buku teratas:", buku_teratas)

# Size
size = len(stack)
print("Jumlah buku dalam stack:", size)

# Search
buku_dicari = input("Masukkan nama buku yang ingin dicari: ")
if buku_dicari in stack:
    posisi = stack.index(buku_dicari)
    print(f"{buku_dicari} ditemukan di posisi {posisi} dalam stack.")



# Is Empty
is_empty = len(stack) == 0
print("Apakah stack kosong?", is_empty)


# Pop
buku_teratas = stack.pop()
print("Buku yang diambil:", buku_teratas)
print("Stack setelah pop:", stack)


# Clear
stack.clear()
print("Stack setelah clear:", stack)





# Class Stack:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack kosong"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack kosong"

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0 
    
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())   