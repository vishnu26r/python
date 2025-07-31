import os

txt_data = "Hellooooo Mr...!"
file_path = "C:/Users/vishn/OneDrive/Desktop/output.txt"

with open(file_path, "a") as file:
    file.write("\n" + txt_data)
    print(f"file append '{file_path}' sucessfully ")
