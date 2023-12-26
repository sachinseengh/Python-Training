class Calculator:
    def __init__(self,n1,n2):
        self.n1= n1
        self.n2= n2
        
    def sum(self):
        # print(f"The sum is {self.n1+self.n2}")
        return self.n1+self.n2
        
    def sub(self):
        print(f"The sub is {self.n1-self.n2}")
        
    def div(self):
        print(f"The div is {self.n1/self.n2}")
        
    def mul(self):
        print(f"The mul is {self.n1*self.n2}")
        
    
c1= Calculator(5,5)
res=c1.sum()
print(res)
c1.sub()
c1.div()
c1.mul()