def sec_large(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."
    large=arr[0]
    sec_large=float('-inf')
    for i in range(1,len(arr)):
        if arr[i]>large:
            sec_large=large
            large=arr[i]
        elif arr[i]>sec_large and arr[i]!=large:
            sec_large=arr[i]
    return large,sec_large

arr=list(map(int,input('Enter the elements:\n').split()))
l,sl=sec_large(arr)
print('Largest: ',l,'\nSecond largest: ',sl)