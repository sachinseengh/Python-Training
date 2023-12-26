class Student:
    id=8
    
    # Constructor in python
    # def __init__(self,id,name,address):
    #     self.id=id
    #     self.name=name
    #     self.address=address
    

# It is compulsory to pass self in method of a class
    def detail(self):
       print(f"your id is {self.id}")
    
    
    
# in case of Constructor 
# s1=Student(5,"sachin","gaushala")
# print(s1.address)


# modification in class
s1= Student()


s1.id=5
print(s1.id) #Answer is 5




s1.detail()





# to delete the object of class
del s1

# to delete the property of objec
del s1.id