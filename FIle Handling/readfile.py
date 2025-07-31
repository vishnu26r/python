
file_path="C:/Users/vishn/OneDrive/Desktop/output.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
# use exception for better use
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("You do not have permission to read that file")