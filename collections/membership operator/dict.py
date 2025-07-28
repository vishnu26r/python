Grades = {"john": "A", "khan" :"B","Moan":"C"}

studennt=input("enter a name of the student:  ")

if studennt in Grades:
    print(f"{studennt}'s grade is {Grades[studennt]}")
else:
    print(f"{studennt} not found")
    