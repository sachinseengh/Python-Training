def perform_math_operation(n1,n2,oper):
    
    if(oper== "+"):
        print(f"The sum of {n1} and {n2} is {n1+n2}")
    elif(oper== "-"):
        print(f"The sub of {n1} and {n2} is {n1-n2}")
    elif(oper== "/"):
        print(f"The div of {n1} and {n2} is {n1/n2}")
    elif(oper== "*"):
        print(f"The mul of {n1} and {n2} is {n1-n2}")
    else:
        print("Invalid operation")
        
        
        
n1=int(input("Enter your first number : "))
n2=int(input("Enter your second number : "))
oper=input("Enter your  operation : ")


perform_math_operation(n1=n1,n2=n2,oper=oper)


