def count_string(str):
    vow='aeiouAEIOU'
    vcount=sum(1 for char in str if char in vow)
    c_count=sum(1 for char in str if char not in vow and char.isalpha())
    s_count=sum(1 for char in str if char==' ')
    return vcount,c_count,s_count

str=input('Enter the string:\n')
vow,cons,space=count_string(str)
print('no of consonants: ',cons,
      '\nNo ofvowels: ',vow,'\nNo if spaces: ',space)