
# importing base class

# import Employee as emp
# or
# import Employee

# or
from Employee import Employee

# for 1st method
# class Designer(emp.Employee)

# for 2nd method
# class Designer(Employee.Employee):


# for 3rd method
class  Designer(Employee):
    def __init__(self,name,address,salary,tool):
       super().__init__(name,address,salary)
       self.tool=tool
    def print_detail(self):
        super().print_detail()
        print("Tool",self.tool)
   