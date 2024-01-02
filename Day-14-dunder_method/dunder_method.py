class BankAccount:
    
    __balance=110
    
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
        
    def __str__(self):
        return (f"{self.__acname} {self.__acnum}")
    
    def __gt__(self,other):
        return (self.__balance < other.__balance)
    def __add__(self,other):
        return (self.__balance + other.__balance)
    
        


        
account_1 = BankAccount("Sachin",1588,"Bafal")
account_2 = BankAccount("Surya",458,"bafal")


# this show error because there is no balance
print(account_1>account_2)

