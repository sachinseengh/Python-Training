price =566
discount=0

if(price>500):
    discount = price*0.15
else:
    discount=price*0.05
    
print("Total amount",price-discount)
print("discount",discount)