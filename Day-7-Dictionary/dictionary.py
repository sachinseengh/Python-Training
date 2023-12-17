# key value pair
# unordered
# mutable



# explict person = dict("name":"sachin")



person = {
    "name":"Ram",
    "Age":23
}


print(person['name'])
print(person.get("Age"))

for i,v in person.items():
    print(f"key is {i} and value is {v}")