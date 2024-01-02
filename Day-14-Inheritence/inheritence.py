
# # Classes without inheritence

# class Designer:
#     def __init__(self,name,address,salary,tool):
#         self.name=name
#         self.address=address
#         self.salary=salary
#         self.tool=tool
        
#     def print_detail(self):
#         print(f"{self.name},{self.address},{self.salary},{self.tool}")
    
        
# class Developer:
#     def __init__(self,name,address,salary,programming_language):
#         self.name=name
#         self.address=address
#         self.salary=salary
#         self.programming_language=programming_language
        
#     def print_detail(self):
#         print(f"{self.name},{self.address},{self.salary},{self.programming_language}")
        
        
        
# Designer_1 = Designer("Sachin","Bafal",5000,"Adobe")
# Developer_1= Developer("Surya","Bafal",8000,"Python")

# Designer_1.print_detail()
# Developer_1.print_detail()




# -------------------------------------After inheritence---------------------

# Classes without inheritence



class Employee:
    
    def __init__(self,name,address,salary):
        self.name= name
        self.address=address
        self.salary=salary
        
    def print_detail(self):
        print(f"{self.name},{self.address},{self.salary}")

class Designer(Employee):
    def __init__(self,name,address,salary,tool):
       super().__init__(name,address,salary)
       self.tool=tool
    def print_detail(self):
        super().print_detail()
        print("Tool",self.tool)
   
    
        
class Developer(Employee):
    def __init__(self,name,address,salary,programming_language):
        super().__init__(name,address,salary)
        self.programming_language=programming_language
        
    def print_detail(self):
        super().print_detail()
        print("Programming",self.programming_language)
        
        
Designer_1 = Designer("Sachin","Bafal",5000,"Adobe")
Developer_1= Developer("Surya","Bafal",8000,"Python")

Designer_1.print_detail()
Developer_1.print_detail()