class BankAccount:
    
    __balance=0
    
    def __init__(self,acname,acnum,acadd):
        self.__acname=acname
        self.__acnum=acnum
        self.__acadd=acadd
        
        
    def deposit(self,amount):
        self.__balance = self.__balance+amount
        print(f"You have Deposited Rs {amount} successfully")
       
        
    def withdraw(self,amount):
        
        if(self.__balance>=amount):
            self.__balance =self.__balance- amount
            print(f"You have Withdrawl Rs {amount} successfully")
        else:
            print("Insufficient Balance")
        
        
    def balance(self):
        print(f"Your balance is {self.__balance}")
        


        
account_1 = BankAccount("Sachin",1588,"Bafal")

account_1.balance()
d = int(input("Enter the amount you want to deposit :"))

account_1.deposit(d)
print("------------------------------------------")
account_1.balance()

w = int(input("Enter the amount you want to withdrawl :"))

account_1.withdraw(w)

account_1.balance()

