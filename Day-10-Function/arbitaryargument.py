# arbitary attribute
def multiply(*args):
    # print("Arguments : ", args)
    # print(type(args)) #it return tuple
    
    total_multiply=1
    for number in args:
        total_multiply= total_multiply*number
    return total_multiply






total=  multiply(5,5,2,5,8)
print(total)