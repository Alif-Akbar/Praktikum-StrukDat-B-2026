class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    data = ("Nama", "Keluhan")
    

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.front.data

  def isEmpty(self):
    return self.length == 0
  
  def clear(self):
    self.front = None
    self.rear = None
    self.length = 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data , end=" -> " )
      temp = temp.next
    print()

# Skenario Pagi Hari — Poli Umum Sehat Bersama

ListPasien = Queue()

print("==============================")
print("   SISTEM ANTRIAN POLI UMUM   ")
print("       RS Sehat Bersama       ")
print("==============================")




print("Apakah antrian masih kosong?", ListPasien.isEmpty())


ListPasien.enqueue(("Budi", "Demam Tinggi"))
ListPasien.enqueue(("Ani", "Batuk Kering"))
ListPasien.enqueue(("Citra", "Sakit Kepala"))


print("Jumlah Pasien di Poli Umum Sehat Bersama:", ListPasien.size(), "pasien")
print("Pasien pertama yang akan dilayani: ", ListPasien.peek())
print("Melayani pasien: ", ListPasien.dequeue())


ListPasien.enqueue(("Dodi", "Nyeri Perut"))
print("Daftar Pasien di Poli Umum Sehat Bersama: ")
ListPasien.printQueue()
print("Melayani pasien: ", ListPasien.dequeue())


print("Sesi poliklinik selesai — kosongkan antrian!")
ListPasien.clear()
print("Apakah antrian sudah kosong?", ListPasien.isEmpty())
