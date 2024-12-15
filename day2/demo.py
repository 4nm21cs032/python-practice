# s1='helooW World'
# print(s1[0])    # h
# print(s1[-1])   # d

# # slice
# print(s1[0:5])  # heloo

# print(s1[::-1]) # dlroW Wooleh

# print(s1.upper())   #HELOOW WORLD

# # print(string_text.replace('old_word','new_word'))
# print(s1.replace('World','python')) # helooW python

# print('hel' in s1)  # True

# # ------------- List --------------
# # -> list is mutable ( can be changed )
# # -> support diff Data Type

# list1=[1,2,3,'python',[4,5]]
# #accessing the elements
# print(list1[3])
# print(list1[-1][0])
# print('-----')
# #modifying elements
# list1[1]='aaa'
# print(list1)
# print('-----')

# list1.append('java')
# print(list1)
# print('-----')

# list1.extend([4,5,6])
# print(list1)
# print('-----')

# list1.remove('python')
# print(list1)
# print('-----')

# list2 = [3,4,1,8,4,6,2]
# list2.sort()
# print(list2)

# # --------- Tuple ----------
# # -> tuple is an ordered collection
# # -> immutable
# # -> faster than list and used for fixed data
# tp=(1,2,3,'ram')
# print(tp[2])

# #tp[1]='hello #unable to perform

# a,b,c,d=tp
# print(a,d)
# print(tp.index('ram'))

'''
--------- Dictonary ----------
    -UNOREDED COLECTION of key value pairs
    -keys are unique and immutablr
    -values can be mutable
'''
d={'name':'Anil', "age":25,"skills":['python','C++','java']}
print(d['name'])
print(d.get('age'))
d["city"]="udupi"
print(d)
d['age']=27
print(d)

del d['city']
print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

for key,value in d.items():
    print(key,value)