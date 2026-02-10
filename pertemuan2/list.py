'''
Docstring for pertemuan2.list
'''








'''List adalah kumpulan data yang terurut dan dapat diubah (mutable).
List digunakan untuk menyimpan beberapa item dalam satu variabel.'''




thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # menampilkan seluruh item dalam list
print(thislist.count("cherry"))  # menghitung berapa kali item "cherry" muncul dalam list
print(len(thislist))  # menghitung jumlah item dalam list
print(thislist[-1])  # menampilkan item terakhir dalam list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")  # memeriksa apakah "apple" ada dalam list


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
print(list1)  # menampilkan list dengan tipe data campuran


mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # menampilkan tipe data list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)  # menampilkan list yang dibuat dengan constructor list()
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # menampilkan item dari index 2 sampai index 4


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # mengganti item pada index 1 dan 2 dengan "blackcurrant" dan "watermelon"


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # menghapus item "banana" dari list (hanya yang pertama ditemukan)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # menghapus item pada index 1 (yaitu "banana")


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # menghapus item terakhir dalam list


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # menghapus item pada index 0 (yaitu "apple")


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # menghapus semua item dalam list sehingga list menjadi kosong


thislist = ["apple", "banana", "cherry"]
del thislist # menghapus seluruh list
# print(thislist)  # ini akan menimbulkan error karena list telah dihapus


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  # menampilkan semua item dalam list menggunakan loop while


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  # membuat list baru yang hanya berisi item yang mengandung huruf "a"


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello ' + x for x in fruits]

print(newlist)  # membuat list baru dengan menambahkan kata "hello " di depan setiap item dalam list fruits


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # mengurutkan item dalam list secara ascending (A-Z)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # mengurutkan item dalam list angka secara ascending (dari kecil ke besar)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)  # mengurutkan item dalam list angka secara descending (dari besar ke kecil)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)  # mengurutkan item dalam list berdasarkan jarak dari angka 50









'''Set adalah kumpulan data yang tidak berurutan dan tidak dapat diubah (immutable).
Set digunakan untuk menyimpan beberapa item dalam satu variabel.'''





thisset = {"apple", "banana", "cherry", False, True, 0, 1}

print(thisset) # menampilkan seluruh item dalam set (urutan tidak terjamin)

# false dan 0 dianggap item yang sama dalam set
# true dan 1 dianggap item yang sama dalam set

print(len(thisset))  # menghitung jumlah item dalam set



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)  # menambahkan item dari set tropical ke dalam thisset








'''Dictionary adalah kumpulan data yang tidak berurutan, dapat diubah (mutable), dan berpasangan (key-value).
Dictionary digunakan untuk menyimpan data dalam format key-value.'''




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])  # menampilkan nilai dari key "brand" dalam dictionary
print(len(thisdict))  # menghitung jumlah item dalam dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  # menampilkan dictionary (key "year" akan memiliki nilai terakhir yaitu 2020)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)  # menampilkan dictionary yang berisi dictionary lain sebagai nilai
print(myfamily["child2"]["name"])  # menampilkan nilai dari key "name" dalam dictionary child2 yang ada di dalam myfamily


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) # menampilkan keys dalam dictionary

car["color"] = "white"

print(x) # menampilkan keys dalam dictionary, setelah menambahkan item baru keys akan terupdate

