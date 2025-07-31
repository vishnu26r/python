# "x"=  used to create file and write ,if already created file try with x it shows error 

import os

text_data = "i like pizza!!"

#file_path = "File Handling/output.txt"
file_path = "C:/Users/vishn/OneDrive/Desktop/output.txt"

with open(file_path, "w") as file:
    file.write(text_data)
    print(f"txt file'{file_path}' was created")

try:
    with open(file_path, "w") as file:
         file.write(text_data)
         print(f"txt file'{file_path}' was created")
except FileExistsError:
    print("FIle Already exists")