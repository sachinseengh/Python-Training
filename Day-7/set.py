# Set 
# Duplicate not allow
# set are unordered

a={1,2,3,4,5,6}
b={5,6,7,8,9,10}

c = a.intersection(b)
print(c)

d= a.union(b)
print(d)

tr= a.isdisjoint(b)
print(tr)

a.remove(5)
print(a)

a.add(588)
print(a)

# union
e= a|b
print(e)


# for intersection
ee= a&b
print(ee)



# converting list into set
a2=[1,2,3,4,5,5]
print(set(a2))



a3 =(1,5,8)
print(type(set(a3)))