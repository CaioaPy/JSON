import json

lista = [
    {
    "name": "Francis",
    "ID": 59283122,
    "Work": "Unemployed",
    "Employed": False,
    "Likes": ["games", "Series"]
    },
    {
    "name": "Marcus",
    "ID": 1231262,
    "Work": "Dev",
    "Employed": True,
    "Likes": ["learning", "teaching"]
    }
]

with open("UserData.json", "w") as f:
    json.dump(lista, f)