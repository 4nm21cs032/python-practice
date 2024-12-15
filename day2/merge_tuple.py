def merge_two_tuple(t1, t2):
    return tuple(x for y in zip(t1, t2) for x in y)
t1=(1,2,3)
t2=('a','b','c')
print(merge_two_tuple(t1,t2))