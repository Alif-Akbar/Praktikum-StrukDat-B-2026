class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack) + 1

TumpukanBuku = Stack()

TumpukanBuku.push('Bumi')
TumpukanBuku.push('Bulan')
TumpukanBuku.push('Matahari')
TumpukanBuku.push('Bintang')


print("Tumpukan buku: ", TumpukanBuku.stack)
print("Ambil buku yang paling atas: ", TumpukanBuku.pop())
print("Tumpukan Buku setelah diambil: ", TumpukanBuku.stack)
print("Lihat buku yang palingatas: ", TumpukanBuku.peek())
print("Apakah Tumpukan Bukunya kosong? ", TumpukanBuku.isEmpty())
print("Panjang Tumpukan bukunya: ", TumpukanBuku.size())