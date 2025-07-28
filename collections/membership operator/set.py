Student = {"vishnu", "akash","sabaree","jk"}

guess = input("enter a student name: ").lower()

if guess in Student:
    print(f"{guess} is a Student")
else:
    print(f"{guess} is not found")
