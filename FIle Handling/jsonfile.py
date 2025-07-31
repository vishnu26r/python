#dump() = used in dict to convert our dict to a JSON String

import json

employee = {
    "name" : "SpiderMan",
    "age" : 21,
    "job" : "Rescuve People"
}

file_path = "C:/Users/vishn/OneDrive/Desktop/jsonfile.json"

with open(file_path, "w") as file:
    json.dump(employee,file,indent=4)
    print(f"json file '{file_path}' was created")
