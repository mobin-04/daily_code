class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"\nAmount ₹{amount} Withdrawn Sucessfully!")
            self.display_account_details()
        else:
            print(f"Insuffecient Blance!!!")
            self.display_account_details()
    def deposite(self,amount):
        self.balance+=amount
        print(f"\nAmount ₹{amount} deposited Sucessfully!")
        self.display_account_details()
    def display_account_details(self):
        print(self.balance)
        print(self.account_holder)
        print(self.account_number)
obj1=BankAccount(123,"bottu",0)
obj2=BankAccount(456,"deepak",500)
obj3=BankAccount(789,"adi",1000)
BankAccount.deposite(obj1,5000)
BankAccount.withdraw(obj2,200)
BankAccount.display_account_details(obj3)


        