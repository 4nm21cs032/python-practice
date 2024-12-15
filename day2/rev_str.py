#  Method-1
def rev_str(str):
    str = list(str)
    s=0
    e=len(str)-1
    while s<e:
        temp=str[s]
        str[s]=str[e]
        str[e]=temp
        s+=1
        e-=1
    print(''.join(str))
str='hello'
rev_str(str)

#  Method-2
def reverseString(str):
    reversed_str = ""
    for c in str:
        reversed_str = c + reversed_str 
    print(reversed_str)
str1='hello'
reverseString(str1)