'''
    create BankAccount
    Attrbutes:account holder
        -balance
        -account number
    method:
        -deposit(amount):
        -withdraw(amount):
        -display_balance()
        -use the _str_() method to return a string representation of the account details
'''

class BankAccount:
    def __init__(self, acc_holder, acc_number, balance=0):
        self.acc_holder=acc_holder
        self.__balance=balance
        self.acc_number=acc_number
    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount
            print(f"deposited {amount}")
        else:
            print(f"Invalid amount {amount}!!! cannot be deposited")
    def withdraw(self, amount):
        if(amount>self.__balance):
            print("Amount exceeds account balance")
        else:
            self.__balance-=amount
            print(f"withdrawed {amount}")

    def display_balance(self):
        print(f"Current balance: {self.__balance}")
    def __str__(self):
        return f"accountholder: {self.acc_holder}, account number: {self.acc_number}"

account = BankAccount("Anil","12345678", 70000)
account.deposit(5000)
account.deposit(-1000)
account.display_balance()
account.withdraw(1000)
account.withdraw(300000)
print(account)

