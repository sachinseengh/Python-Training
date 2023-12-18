# similar to switch case
# introduced in python 3.10
# when some pattern matches block the match case get executed

# we can match list in case
# list can check list with number



# match(marks):
#     case 80:
#         print("distinction")
        
#     case 60:
#         print("first")
#     case 40:
#         print("second")
#     case 20:
#         print("Third")
#     case _:
#         print("fail")
        
        
        
        # using if in case
        
marks=55   
match(marks):
    case marks if marks>80:
        print("distinction")
        
    case marks if marks>60 :
        print("first")
    case marks if marks>40:
        print("second")
    case marks if marks>20:
        print("Third")
    case _:
        print("fail")
        
        
        
# case [greet,ram]--- it matches with the list having two element 
# greet,ram is just a representation