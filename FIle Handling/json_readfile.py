#load() = is allow file to load in json

import json

file_path = "C:/Users/vishn/OneDrive/Desktop/jsonfile.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    #we can use key also
    print(content["name"])
    print(content["job"])

