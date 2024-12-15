#   replace all occurence of substring
def replace_str(str,old,new):
    return str.replace(old,new)

str=input('Enter the string:\n')
substring=input('Enter the substring:\n')
new_str=input('Enter the newstring to replace:\n')

print(replace_str(str,substring,new_str))