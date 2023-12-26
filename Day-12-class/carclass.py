class Car:
    def __init__(self,name,color,fuel):
        self.name=name
        self.color=color
        self.fuel=fuel
        
    def start(self):
        print(f"The car name is {self.name},Color is {self.color} and Fuel type is {self.fuel}")
        
car1 = Car("bmw","color","petrol")
car1.start()