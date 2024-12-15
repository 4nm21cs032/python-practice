'''
Class and Objects:
--------------------------------------------
Class: the structure and behaviour of the objects
object: instace of a class

'''
# class Car:
# #_init_ initilaize the attributes of the class
#     def _init_(self, make, model, year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display(self):
#         print(f"{self.make}{self.model}{self.year}")
        
# car=Car("kia","seltos","2024")
# car.display()

#_init_(self): Constructor, used to initalze the object
#_str_(self):str() to return a string representation of object

# class Book:
#     def __init__(self, title, author):
#         self.title=title
#         self.author = author
#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
# book=Book("python","Guido")
# print(book)

# ----------- inheritance -------------
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f'{self.name} make a sound')

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")

# dog=Dog("jimmy")
# dog.speak()
# animal=Animal('jimmy1')
# animal.speak()

# -----------------Data Hiding------------------
# class bankAcc:
#     def __init__(self,owner,balnce):
#         self.owner=owner
#         self. _balance=balnce     #protected attr
#         # self.__balnce=balnce  -> private var cannot be accesd outside class
#     def deposit(self,amt):
#         self. _balance+=amt
#     def get_balance(self):
#         return self. _balance
# account=bankAcc(u'Luffy',100)
# account.deposit(500)
# print(account.owner)
# print(account._balance) 
# print(account.get_balance())

