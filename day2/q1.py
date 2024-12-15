'''
1.  pgm to check given string is palindromwe.
    ignoring space ,case  and punctuatuion


4.  given a nested tuple ((1,2) , (3,(4,5)) , (6,7)).
    write a pgm to flatten it into single tuple.

5.  given a tuple of integers. find the following:
        -> max and min val
        -> sum of all ele
        -> tuple after removing duplicates (convert into tuple aggregate)
    
6. sum of subsets, target sum:5
    list=[1,2,3,4,5]
    output -> (1,4) (2,3)

'''

# -------1-------

def palindrome(str):
    s1=str.lower();
    s1=''.join(char for char in s1 if char.isalnum())
    print(s1==s1[::-1]) 
str=input("Enter the string:\n")
palindrome(str)
