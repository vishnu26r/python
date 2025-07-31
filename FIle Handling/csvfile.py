# writer = is an object. it provides for writing data to a CSV file

import csv

employees = [["Name" ,"Age", "Job"],
             ["SpiderMan",21, "Rescue people"],
             ["ironMan",22,"Ironing"],
             ["Hulk", 23,"unemployement"]]

file_path = "C:/Users/vishn/OneDrive/Desktop/csvfile.csv"

with open(file_path, "w", newline='') as file:
    writer = csv.writer(file)
    for employee in employees:
        writer.writerow(employee)
    print(f"csv file '{file_path}' was created")
