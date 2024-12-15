'''
pgm to wrtie asks user for age . use asser stament to 
ensure that age entered is +ve
if -ve then riase assertion error wirh error msg
'''

def  agecheck(age):
    assert age>0 , "Enter valid positive integer"
try:
    age=int(input("enter ut  age: \n"))
    agecheck(age)
except AssertionError as e:
    print(f'Error: {e}')
except ValueError:
    print("INvalid input")
else:
    print(f'Age: {age}')