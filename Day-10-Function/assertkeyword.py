
# Even we have defined that the name should
# be str and if we pass the int it will work 

def person(name:str ,age:int):
    
    
    # to avoid the above condition we can do this
    assert type(name) == str,"name must be string"
    assert type(age) == int,"age must be Integer"
    print(f"Name is {name} and age is {age}")
    
    
# person(55,"sachin")
person("SACHIN",58)
