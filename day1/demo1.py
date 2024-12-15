# import sys
# print('scrypt name: ',sys.argv[0])
# if len(sys.argv)>1:
#     print('arguments: ',sys.argv[1])
# else:
#     print('No args')

# implicit conv
# excplicit conv
# list() tuple() set() dict()

# types of literals

# # --> numeric literals
# x=4+5j
# print(x,type(x))
# True, False
# value=None
# print(value,type(value))

# # ->>collection literals
# list=[1,2.3,'abc']
# tuple=(1,2.3,'abc')
# set={1,2.3,'abc'}
# dic={'key':'value'}

# #Bytes: immutable
# b=b'python'
# print(b, type(b))

# #ByteAray: mutable
# ba=bytearray(b'python')
# print(ba, type(ba))

# #memoryview: used to view and manipulate data withut copying
# mv=memoryview(b'python')
# print(mv,type(mv))


# Anonymous function
# # lambda args : expr
# square=lambda x:x**2
# print(square(3))

# def outer():
#     x=5 # non-local var
#     def inner():
#         nonlocal x
#         x+=1
#         print(x)
#     inner()
# outer()


# # -----------Python Decortors------------
# # @staticmethod -> Defines static method
# # @classmethod -> defines method related 
# # @property -> converts method into property

# class myClass:
#     @staticmethod
#     def static_method():
#         return 'i am static'
#     @classmethod
#     def class_method(cls):
#         return f'i am related ti {cls}'
# print(myClass.static_method())
# print(myClass.class_method())


# # ------- Closure function -----
# def outer_fn(x):
#     def inner_fn(y):
#         return x+y
#     return inner_fn
# add1=outer_fn(5)    # x=3 y=5
# print(add1(3))
## When you call outer_fn(5), it executes and returns the inner_fn function.
## The value of x is remembered by the returned function (inner_fn) as part of the closure.

# ---------- filter map reduce enumerate --------
#  -> filter(function,iterable)
n1=[1,2,3,4,5]
res=filter(lambda x:x%2==0,n1)
print(list(res))