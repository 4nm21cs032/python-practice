import numpy as np
''' numpy universal functions (Ufunctions) '''
#mathematical Ufunctions
# ang1=np.array([0,30,45,60,90])
# radians=np.deg2rad(ang1)
# print(radians)

# #compute
# sin_val=np.sin(radians)
# cos_val=np.cos(radians)
# print(sin_val)
# print(cos_val)


''' logical and comarisons  Ufns '''
# A=np.array([True, False, True])
# B=np.array([False, False, True])
# l_and=np.logical_and(A,B)
# print(l_and)

# #element wise comparison
# a1=np.array([1,2,3])
# a2=np.array([3,2,1])
# gt=np.greater(a1,a2)
# print(gt)

# #create own functions using frompyfunc
# def add_one(x):
#     return x+1
# # create ufunc
# add_ufunc=np.frompyfunc(add_one,1,1)        # param: no of ips, no of ops
# a1=np.array([1,2,3,4,5])
# res=add_ufunc(a1)
# print(res)

'''
    1.Create a random array
        - find the elements greater than 50 and compute their logarithm
# '''
# rand_array=np.random.randint(1,100,50)      # start,end,size
# gt_50=rand_array[rand_array>50]
# log_Val=np.log(gt_50)
# print(f'{gt_50}\n{log_Val}')

# def split_no(x):
#     return x//2,x%2

# split_res=np.frompyfunc(split_no,1,2)
# a=np.array([10,15,30,25,30])
# res1,res2=split_res(a)
# print(f'{res1}\n{res2}')
# # [5 7 15 12 15]
# # [0 1 0 1 0]


'''
    Create a numpy array of 50 random nos between 1 and 100 
        - find all prime nos in array
        - for the prime nos, compute their square root using ufunc (universal fn)

'''
# arr=np.random.randint(1,100,50)
# print(arr)
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(np.sqrt(num))+1):
#         if num%i==0:
#             return False
#     return True
# prime_fn=np.frompyfunc(is_prime,1,1)
# prime_m=prime_fn(arr).astype(bool)
# prime_no=arr[prime_m]
# print('\nPrime nos: ',prime_no)
# sqrt_prime=np.sqrt(prime_no)
# print(f'square roots:\n{sqrt_prime}')


'''
    Write a custom function that takes a string and returns:
        > The string reversed.
        > The length of the string.
    Convert this function into a universal function (ufunc) 
    and apply it to an array of strings like ["hello", "python"].
'''

def rev_str(str):
    rev=str[::-1]
    str_len=len(str)
    return rev,str_len
rev_ufn=np.frompyfunc(rev_str,1,2)
strs=np.array(['Hello','World!!'])
revstr,str_len=rev_ufn(strs)
print(f'reversed str: {revstr}\nStrlem: {str_len}')