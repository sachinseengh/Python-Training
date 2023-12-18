marks =100

grade="no grade"

if(marks>=80):
    grade="Distinction"
elif(marks>=60):
    grade="First"
elif(marks>=40):
    grade="Second"
elif(marks>=30):
    grade="Third"
else:
    grade="fail"
    
print("Grade : ",grade)