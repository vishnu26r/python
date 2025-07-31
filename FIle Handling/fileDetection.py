import os

file_path = "C:/Users/vishn/OneDrive/Desktop/filehandling.txt"

if os.path.exists(file_path):
    print(f"File location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("that is a directory!")
else:
    print(f"File Location doesn't exist")