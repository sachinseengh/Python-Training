# write program that prints the numbers
# from 1 to 10 ,but stops if the number is greater than 5


a = range(1,10,1)



for i in a:
    if(i>5):
        break
    else:
        print(i)