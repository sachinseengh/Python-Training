def greet(**kwargs):
    print(kwargs) #it return dictionary

greet(name_1="Ram",name_2="shyam")




# use case
def total_marks(math,english, **kwargs):
    
    total=math+english;
    
    for sub,mark in kwargs.items():
        total += mark
    print(total)    
    
    
    
total_marks(math=58,english=85,opt=78)