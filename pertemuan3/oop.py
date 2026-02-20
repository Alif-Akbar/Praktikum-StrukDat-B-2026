'''
self itu adalah parameter pertama dalam metode kelas di Python,
yang merujuk pada instance objek itu sendiri. Ketika Anda membuat metode dalam sebuah kelas,
Anda harus menyertakan self sebagai parameter pertama, 
agar metode tersebut dapat mengakses atribut dan metode lain.

OOP (Object-Oriented Programming) adalah paradigma pemrograman yang berfokus pada objek dan kelas.
OOP memungkinkan kita untuk membuat objek yang memiliki atribut (data) dan metode (fungsi) yang terkait dengan objek tersebut. OOP membantu dalam mengorganisir kode, meningkatkan modularitas, dan memudahkan pemeliharaan.
OOP memiliki beberapa konsep utama, termasuk:
1. Kelas (Class): Blueprint atau template untuk membuat objek. Kelas mendefinisikan atribut dan metode yang dimiliki oleh objek.
2. Objek (Object): Instance dari kelas. Objek memiliki atribut dan metode yang definisikan kelasnya.
3. Enkapsulasi (Encapsulation): Konsep menyembunyikan data dan metode dalam sebuah kelas, sehingga hanya dapat diakses melalui metode yang disediakan oleh kelas tersebut.
4. Pewarisan (Inheritance): Konsep di mana sebuah kelas dapat mewarisi atribut dan metode dari kelas lain, memungkinkan untuk membuat hierarki kelas.
5. Polimorfisme (Polymorphism): Konsep di mana objek dari kelas yang berbeda dapat digunakan secara interchangeably, asalkan mereka memiliki metode yang sama.
6. Abstraksi (Abstraction): Konsep menyembunyikan detail implementasi dan menyediakan antarmuka yang sederhana untuk berinteraksi dengan objek.
'''
# Object-Oriented Programming (OOP) Example in Python

class Car:
    def __init__(self, make, model, year): # Constructor method to initialize the car's attributes
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment
        print(f"The car has accelerated. Current speed: {self.speed} km/h") # Method to increase the car's speed

    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"The car has braked. Current speed: {self.speed} km/h") # Method to decrease the car's speed

    def honk(self):
        print("Beep beep!") # Method to honk the car's horn

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
my_car.accelerate(30)
my_car.brake(10)
my_car.honk()
