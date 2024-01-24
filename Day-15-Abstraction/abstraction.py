# Abstraction

from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    
     def __init__(self,name) :
         self.name=name;
         
    
     def start(self):
        print(f"{self.name} is starting")
      
     def stop(self):
         print(f"{self.name} stopped")  
        
 
car = Car("BMZ")

car.start()
car.stop()
 
