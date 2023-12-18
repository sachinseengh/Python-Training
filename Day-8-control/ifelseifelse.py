price=8000
discount=0

if(price>8000):
    discount = price*0.15
elif(price>6000 ):
    discount= price*0.10
else:
    discount = price*0.05
    
    
print("Total amount",price-discount);
print("Discount",discount)