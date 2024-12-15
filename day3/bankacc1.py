'''
    create a savingacc as a subclass
        -> inherits from bankAccount
        -> addtional attr
            . interest_rate : rate of interst( defult 2% )
        -> calc_interest():calculate and return interest earned on 
            current bal
'''

class BankAccount:
    def __init__(self, acc_holder, acc_number, balance=0):
        self.acc_holder=acc_holder
        self.balance=balance
        self.acc_number=acc_number
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(f"deposited {amount}")
        else:
            print(f"Invalid amount {amount}!!! cannot be deposited")
    def withdraw(self, amount):
        if(amount>self.balance):
            print("Amount exceeds account balance")
        else:
            self.balance-=amount
            print(f"withdrawed {amount}")
    def display_balance(self):
        print(f"Current balance: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, acc_holder, acc_number,interst_rate=2, balance=0):
        super().__init__(acc_holder, acc_number, balance)
        self.interest_rate=interst_rate
    def calculate_interest(self):
        print(f"Interest earned {self.balance*self.interest_rate/100}")
    def __str__(self):
        return f"{super()._str_()}, interest rate: {self.interest_rate}"

account1=SavingAccount("Anil","123456789",5, 70000)
account1.display_balance()
account1.deposit(500)
account1.display_balance()
account1.calculate_interest()
