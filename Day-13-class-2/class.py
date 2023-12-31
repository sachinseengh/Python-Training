
# Access Modifier


class Bike:
    
    
    def __init__(self,name,cc):
        self.__name= name
        self.__cc= cc
    
    def print(self):
        print(f"The name is {self.__name} and cc is {self.__cc}")
        
        
bike = Bike("Yamaha",155)
bike.__name="Bajaj"
print(bike.__name)


bike.print()