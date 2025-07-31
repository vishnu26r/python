employees = ["vishnu", "raghul", "gowtham", "gokul"]

file_path = "C:/Users/vishn/OneDrive/Desktop/output.txt"

with open(file_path ,"w") as file:
    for employee in employees:
        file.write("\n" + employee)
