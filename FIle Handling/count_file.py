file_path = "C:/Users/vishn/OneDrive/Desktop/output.txt"

with open(file_path, "r") as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    chars = len(content)

    print(f"File analysis for: '{file_path}'")
    print(f"Total lines      : '{len(lines)}'")
    print(f"Total words      : '{len(words)}'")
    print(f"Total chars      : '{chars}'")