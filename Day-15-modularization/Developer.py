
from Employee import Employee

class Developer(Employee):
    def __init__(self,name,address,salary,programming_language):
        super().__init__(name,address,salary)
        self.programming_language=programming_language
        
    def print_detail(self):
        super().print_detail()
        print("Programming",self.programming_language)
        