def filter_no(numbers):
    even_nos = [num for num in numbers if num % 2 == 0]  
    sq_nos = [num**2 for num in even_nos]       
    return sum(sq_nos)                           

numbers = list(map(int, input("Enter numbers :\n").split()))
result =filter_no(numbers)
print(result)  
