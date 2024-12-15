def concat_unq_list(l1,l2):
    new_lst=l1+l2
    print(len(new_lst)==len(set(new_lst)))

concat_unq_list([1,22,2,3,4],[1,2,4.1,1])