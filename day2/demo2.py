'''
    Module 
        The standard libaray: includes the collection of modules
        and perfroms the different tasks
        the os module: function to interact with operating system
'''
# import os
# print(os.getcwd())
# # os.mkdir("test")
# print('-------------------------------')

# # sys module: provide the functions and varaibles to interact with python interpretor

# # import sys
# # print(sys.version)
# # sys.exit()
# # print('-------------------------------')

# # random module: generate the random nos
# import random 
# print(random.randint(0,20))
# print(random.choice([1,2,'a','b','d','c']))
# print('-------------------------------')


# # math module
# import math
# print(math.pi)
# print(math.factorial(5))
# print(math.cos(60))
# print('-------------------------------')

# # datetime module:date and time
# import datetime
# now=datetime.datetime.now()
# print(now)
# print(now.strftime("%d-%m-%y %H:%M:%S"))
# print(now.strftime("%d-%m-%Y %H:%M:%S"))
# print('-------------------------------')

# # dir() function
# import math
# print(dir(math))  #lists all the functions in math
# print('-------------------------------')

# import myModule
# print(myModule.add(4,6))
# print(myModule.sub(5,1))

#EXCEPTION HANDLING
'''
error: done by progammer or developer
sytax error: if you do not follow rule of the programming language
logical error:

Exception: mistake done by user
'''

# x=10/0   #Runtime error

#try....except
'''
try:
    num=int(input("enter a no."))
    result=10/num
except ZeroDivisionError:
    print('error: cannot divide by zero')
else:
    print(f'The result is {result}')

'''

#----------------------------------------------
try:
    file=open("a1.txt","r")
    content=file.read()
    print(content)       
    file.close()
except FileNotFoundError:
    print("Error: file doesnt exist")
except IOError:
    print('Eror: I/O error occured')
#-----------------------------------------------

# #  -> raise
# def check_age(Age):
#     if Age<0:
#         raise ValueError('Age cannot be -ve')
#     print(f'age is: {Age}')

# try:
#     check_age(-10)
# except ValueError as e:
#     print(f"Error: {e}")


# ->> assert statement: used for debugging process
def divide(a,b):
    assert b!=0, "Division not allowed"
    return a/b
try:
    res=divide(10,0)
except AssertionError as e:
    print(f'Error: {e}')