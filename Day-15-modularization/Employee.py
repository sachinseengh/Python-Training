# module for employee class

class Employee:
    
    def __init__(self,name,address,salary):
        self.name= name
        self.address=address
        self.salary=salary
        
    def print_detail(self):
        print(f"{self.name},{self.address},{self.salary}")