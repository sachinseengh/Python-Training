def printing(name,**kwargs):
    print("Name : ",name)
    
    for i,v in kwargs.items():
        print(f"{i} : {v}")
        
    

printing(name="Sachin",age=78,address="Gaushala",education="bca",mobile="9818755885")