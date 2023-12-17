
fruits={"apple","banana","grapes"}
vegetable={"patato","tamato","lauki","grapes"}


similar =fruits.union(vegetable);
print(similar)

all = fruits.intersection(vegetable)
print(all)


numbers = len(fruits)
print(numbers)

for  i in fruits:
    print(i)
    
    
# Immutable set are called frozen set

number=frozenset({"1","2"})
# number[0]="sachin"
print(number)