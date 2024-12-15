'''
program to ask user to enter 2 nos
the pgm shd perform diva nd disp the result
handle the exceptions:
    i) ZerodivisionError
    ii) valueError: Enters non numeric inp
'''


try:
    n1=int(input("Enter 1st number:\n"))
    n2=int(input("Enter 2nd number:\n"))
    res=n1/n2
except ZeroDivisionError:
    print('Error : Cannot divide by zero')
except ValueError:
    print('Error : Invalid input')
else:
    print(f'result= {res}')