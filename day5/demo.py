'''
    NumPy => numerical python
        > used for numerical computing
        > support for multi-dimensional arrays
        > data analysis , ML ,  AI
'''

import numpy as np

# # creaating 1D array
# arr1=np.array([1,2,3,4])
# print(arr1)

# # creating 2D array
# arr2=np.array([[1,2],[3,4]])
# print(arr2)

# # Array of zeroes
# zeros=np.zeros((2,3))
# print(zeros)    # [[0. 0. 0.] [0. 0. 0.]]

# # Array of ones
# ones=np.ones((3,2))
# print(ones)
# #  [ [1. 1.]
# #    [1. 1.]
# #    [1. 1.] ]

# range_array = np.arange(0,10,2)
# print(range_array)      # [0 2 4 6 8]
# range_array1 = np.arange(0,100,3)
# print(range_array1)
''' [ 0  3  6  9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69
72 75 78 81 84 87 90 93 96 99] '''
# #5 values between 0 and 1
# line_space=np.linspace(0,1,5)
# print(line_space)   # [0.   0.25 0.5  0.75 1.  ]
'''
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1.ndim)    # no of dimension -> 2
print(arr1.shape)   # no of rows and colms -> (2, 3)
print(arr1.size)    # total ele -> 6
print(arr1.dtype)   # data type of ele -> int64

'''


# # ---- indexinng & Slicing ----

# arr1=np.array([10,20,30,40,50,60])
# print(arr1[2])     # 30
# print(arr1[1:4])    # [20 30 40]

# arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_2d[1,2])      # 1st row 2 col -> 6
# print(arr_2d[:,1])      # all row 1st colmn -> [2 5]

# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(a+b)      # [5 7 9]
# print(a*b)      # [ 4 10 18]
# print(a**2)     # [1 4 9]

# a1=np.arange(12)
# print(a1)       # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# reshape1=a1.reshape(2,6)
# print(reshape1) # [[ 0  1  2  3  4  5] [ 6  7  8  9 10 11]]


'''
ndarray(n-dimnsioanl array):
    - operations on large datasets
    - vectorized operations
    - support for the int, float and complex nos
    - add, sub, mul, div direclty between arrays
'''

# arr=np.array([[1,2],[3,4]])
# res=arr+4
# print(res)      
# ''' [[5 6] [7 8]] '''

# b=np.array([1], dtype='int8')
# print(b, b.dtype)       # [1] int8
# f_array=np.array([1,2,3], dtype='float32')
# print(f_array, f_array.dtype)   # [1. 2. 3.] float32
# comp_array=np.array([1,2,3], dtype='complex64')
# print(comp_array)       # [1.+0.j 2.+0.j 3.+0.j]

# arr1=np.array([1,2,3,4])
# float_array=arr1.astype('float64')
# print(float_array)      # [1. 2. 3. 4.]
# print(float_array.dtype)    # float64

# a123=np.array([1.2,3.4,5.7,8.8])
# int_array = a123.astype('int32')
# print(int_array, int_array.dtype)     # [1 3 5 8] int32


# -------- Matrix --------
'''
    1.Create 2 3*3 matrices
        compute the folowwing 
            - element wise addition and subtraction
            - matrix multiplication
            - the determinant of matrix A
            - inverse of matrix B
'''

# A = np.array([[3,2,3],[4,5,6],[7,8,9]])
# B = np.array([[9,8,7],[6,5,4],[3,1,2]])

# print(A+B)
# print(A-B)
# print(np.dot(A,B))

# print(np.linalg.det(A))

# print(np.linalg.inv(B))



