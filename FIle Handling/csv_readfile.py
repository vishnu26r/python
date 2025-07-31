import csv

file_path = "C:/Users/vishn/OneDrive/Desktop/csvfile.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
        print(line)
        #if we want specific column of csv file use index
        print(line[1])