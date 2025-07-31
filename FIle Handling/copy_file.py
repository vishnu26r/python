import shutil

file_path = "C:/Users/vishn/OneDrive/Desktop/output.txt"
dest_path = "C:/Users/vishn/OneDrive/Desktop/dest.txt"

shutil.copyfile(file_path,dest_path)
print(f"✅ File copied successfully from:\n{file_path} \nto\n{dest_path}")