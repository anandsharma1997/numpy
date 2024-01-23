# class Myclass :
#     x = 5


# p1 = Myclass()

# print(p1.x)

# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

# p2 = Person("Anand", 27)

# #print(p2.name, p2.age)
# print(p2, "withot str method")


# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age


#     def __str__(self) -> str:
#         return f"{self.name}({self.age})"

# p2 = Person("Anand", 27)


# print(p2, "with str method")


# class Person:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def myfunc(self):
#       print("Hello my name is " + self.name)
      
# p1 = Person("Anand Sharma", 27)

# p1.myfunc()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# x = Person("Vinay", "Sharma")

# x.printname()

# class Student(Person):
#     pass


# x = Student("Mike", "olsen")
# x.printname()


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail")
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly")


# car1 = Car("ford", "mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1 , boat1, plane1):
#     x.move()


import json

# some JSON:
# x = '{ "name":"anand", "age":30, "city":"New York"}'

# y = json.loads(x)

# print(type(y))

# print(y["name"])


# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# y = json.dumps(x)

# print(type(y))

# print(y)


# price = 100
# text= "The price of vegetable is {:.2f} rupees"

# print(text.format(price))

# quantity = 3
# itemno = 567
# price = 49

# myorder = "i want {} pieces of item number{} for {:.2f} dollers"

# print(myorder.format(quantity, itemno, price))

# age = 27
# name = "Anand Sharma"

# intro = "My name is {0} , and age {1}, my name is {0}"

# print(intro.format(name,age))


# class Dog:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname


#     def bark(self):
#         print("dogs bark!", self.firstname + " " + self.lastname)


# dog1 = Dog("Abhishek", "Sharma")

# print(dog1.firstname + " " + dog1.lastname)
# dog1.bark()


# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance      #Protected attribute

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             print("withdraw")
#         else:
#             print("Insufficient funds.")

# account = BankAccount(balance=1000)


# class Animal:
#     def __init__(self, name):
#         self.animal_name = name

#     def make_sound(self):
#         print(self.animal_name)


# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# dog1 = Dog(name="Dog")
# dog1.make_sound()

# cat1 = Cat(name="Cat")
# cat1.make_sound()


# class School:
#     def __init__(self, name, schoolcode):
#         self.student_name = name
#         self.roll_number = schoolcode

#     def study(self):
#         print("students are studing...")

# class MathsStudent:
#     def __init__(self, name, roll_number):
#         self.student_name = name
#         self.roll_number = roll_number

#     def study(self):
#         print("students are studing...")

# class CommerceStudent:
#     def __init__(self, name, roll_number):
#         self.student_name = name
#         self.roll_number = roll_number

#     def study(self):
#         print("students are studing...")


# student = School("Avadh academy", 13300)
# mathstudent = MathsStudent("Anand sharma", 32)
# commerceStudent = CommerceStudent("Vinay sharma", 65)

# for x in (student, mathstudent, commerceStudent):
#     x.study()


#without context manager

# file = open('demo.txt', 'r')
# content = file.read()
# print(content)
# file.close()

#with context manager

# with open('demo.txt', 'r') as file :
#     content = file.read()
#     print(content)

# class Anand:
#     def __init__(self, work):
#         self.work = work

#     def __str__(self):
#         return f"Work is {self.work}"
    

# man = Anand("Software engineer")

# print(man)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return f"Point(x ={self.x}, y= {self.y})"
    

# point = Point(5,6)
# print(repr(point))


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def __len__(self):
#         return len(self.items)

# stack = Stack()
# stack.push(5)
# stack.push(10)
# stack.push(55)

# print(len(stack))


# class ItemList:
#     def __init__(self):
#         self.items = []

#     def addItem(self, item):
#         self.items.append(item)

#     def __getitem__(self, index):
#         return self.items[index]
    

# itemlist = ItemList()

# itemlist.addItem(45)
# itemlist.addItem(456)
# itemlist.addItem(47)

# print(itemlist[1])



# class ItemList:
#     def __init__(self):
#         self.items = []

#     def additem(self, item):
#         self.items.append(item)

#     def __setitem__(self, index, value):
#         self.items[index] = value

#     def __getitem__(self , index):
#         self.items[index]

# itemlist = ItemList()

# itemlist.additem(1)
# itemlist.additem(6)
# itemlist[0] = 45

# print(itemlist[0])

# class Acount:
#     def __init__(self, balance):
#         self._balance = balance

#     def deposit(self, amount):
#         if amount>0:
#             self._balance += amount
#             print(f"Deposited {amount} Rupees. New Balance is {self._balance}")

#         else:
#             print("Invalid deposit amount...")

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdraw successfully completed rupees of {amount}. New balance is {self._balance}")

#         else:
#             print("insufficient Balance....")


#     def get_balance(self):
#         return self._balance
    

# acount = Acount(1000)

# acount.deposit(1000)
# acount.withdraw(1500)
# acount.deposit(100000000)
# acount.withdraw(50000)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "superclass method"

# class Dog(Animal):
#     def make_sound(self):
#         return "Barks!"
        

# class Cat(Animal):
#     def make_sound(self):
#         return super().make_sound() + "Meow5nh 4gbrn t5gv"
    

# dog = Dog(name="pappi")
# cat = Cat(name="cittyyy")

# print(dog.name, dog.make_sound())
# print(cat.name, cat.make_sound())


# class A:
#     def show(self):
#         return "A"
    
# class B:
#     def show(self):
#         return "B"
    
# class C(A, B):
#     pass

# obj = C()

# print(obj.show())

# class A:
#     def show(self):
#         return "A"
    
# class B(A):
#     def show(self):
#         return "B"
    
# class C(A):
#     def show(self):
#         return "C"
    
# class D(B, C):
#     pass

# obj = D()

# print(obj.show())


# class Calculator:
#     def add(self, a, b=0):
#         return a + b
    

# cal = Calculator()

# print(cal.add(6))
# print(cal.add(10, 5))


# class A:
#     def show(self):
#         return "A"
    
# class B(A):
#     def show(self):
#         return super().show() + "B"
    
# class C(A):
#     def show(self):
#         return super().show() + "C"
    
# class D(B, C):
#     pass

# obj = D()
# print(obj.show())


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# dog = Dog(name="Doggi", breed="Labrador")
# print(dog.name, dog.breed)



# def addition(*args):
#     return sum(args)


# print(addition(45,45,48,95,233,12,156,659,898))

# try:
#     x = 10/0

# except ZeroDivisionError:
#     print("x can be not divided...")

# try:
#     num = int(input("Enter a one number"))

#     result = 10/num

# except ValueError:
#     print("Invalid input. pleasse enter a number")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# else:
#     print(f"Result : {result}")

# finally:
#     print("This block always executes, regardless of exceptions.")


# try:
#     with open("demo.txt", 'r') as file:
#         content = file.read()

# except FileNotFoundError:
#     print("File not found.")

# else:
#     print(f"File content:{content}")


# try:
#     x = 10/0
    
# except Exception as e :
#     print(f"error name is {e}")


# value = 10
# assert value > 0, "Value must be grater than 0"


# import threading

# def print_number():
#     for i in range(5):
#         print(i)


# thread = threading.Thread(target=print_number)

# thread.start()

# thread.join()

# import os

# def child_process():
#     print("child process")
#     print("child PID:", os.getpid())

# def parent_process():
#     print("Parent process")
#     print("Parent PID:", os.getpid())


#     child_pid = os.getpid()

#     if child_pid == 0:
#         child_process()

#     else:
#         print("child PID:", child_pid)
#         parent_process()

# if __name__=="__main__":
#     parent_process()

# import os
# def child():
#     print("this is child process")

# def parent():
#     print("this is parent proces..")
    
    
