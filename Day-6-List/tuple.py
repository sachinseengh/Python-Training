# under parenthesis

import sys
num_2=(4,5,7,85,75)
print(num_2.index(75))

num_1=[4,5,7,85,75]

# tuple cannot be changed or manipulated
# manipulation methods are unavailable
# num_2[0]=8



print("list size :",sys.getsizeof(num_1))
print("tuple size :",sys.getsizeof(num_2))

for i in num_2:
    print(i)
    