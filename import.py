import json

with open("UserData.json", "r") as f:
    data = json.load(f)

imported = data

print(imported)