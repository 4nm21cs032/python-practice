'''
    2.  count freq of each char on str and print
        3 most common chars
'''
def freq(str):
    s1=str.lower();
    s1=''.join(char for char in s1 if char.isalnum())
    cnt={}
    for char in s1:
        if char in cnt:
            cnt[char]+=1
        else:
            cnt[char]=1
    return sorted(cnt.items(),key=lambda item:item[1],reverse=True)[:3]

str=input('Enter the string:\n')
print(freq(str))