fruits =["apple","orange","banana"]

print(fruits[0])

print(fruits[-1])
print(len(fruits))

for i in fruits:
    print (i)
    
fruits.append("guava")
fruits.remove("apple")

fruits.sort(reverse=True)

fruits.insert(1,"grapes")
fruits[0]="cherry"

print(fruits.count("apple"))

print(fruits) 
