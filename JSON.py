import json

#dict
banco ={
    "name": "Francis",
    "ID": 59283122,
    "Work": "Unemployed",
    "Employed": False,
    "Likes": ["games", "Series"]
    }

data = json.dumps(banco,separators=(": ","-"))

print(data)