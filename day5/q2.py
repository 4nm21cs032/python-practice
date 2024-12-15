'''
    create a random array of 100 elementts between 0 and 1
    find 
        > mean
        > Standard deviation
        > median
        > elemnets greater than 0.8
'''

import numpy as np
# arr_random = np.random.random(100)
# print('Elements: \n',arr_random)

# mean=np.mean(arr_random)
# median=np.median(arr_random)
# sd=np.std(arr_random)
# gt=arr_random[arr_random>0.8]

# print('\nMean: ',mean,'\nmedian: ',median,'\nStandard Deviation: ',sd,'\nValues > 0.8:\n',gt)



'''
    4.Create the following 4*4 array
    Extract:
    - the diagonal elements
    - all elements greater than 10
    - A sub array with middle 2*2 block
'''
# array1=np.array([[2,3,1,4],[2,5,88,4],[1,4,6,7],[11,4,3,6]])
# print(np.diag(array1))      # [2 5 6 6]
# print(array1[array1>10])    # [88 11]
# print(array1[1:3,1:3])      # [[ 5 88] [ 4  6]]


''' Fibonacci Series '''
# n=int(input('Enter the range: '))
# fib=np.zeros(n,dtype='int64')
# fib[0]=0
# fib[1]=1
# for i in range(2,n):
#     fib[i]=fib[i-1]+fib[i-2]
# print(fib)


'''
    Create 1D numoy array 10-60
    perform tasks :
        > find index of elemnet 40
        > check if 25 exists in array
        > get all indices whr val>35
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

ele = int(input('Enter the element whose index to be found: '))
indices = np.where(arr == ele)[0]
if indices.size > 0:
    print(f'Index of {ele} is: {indices[0]}')
else:
    print(f'Element {ele} does not exist in the array.')

search_ele = int(input('Check existence of element: '))
if search_ele in arr:
    print(f'Element {search_ele} exists in the array.')
else:
    print(f'Element {search_ele} does not exist in the array.')

greater_indices = np.where(arr > 35)[0]
print(f'Indices where values are greater than 35: {greater_indices}')
