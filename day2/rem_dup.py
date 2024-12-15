def remove_duplicate(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(remove_duplicate([1, 2, 3, 3, 4, 4, 5]))
