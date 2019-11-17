import json
import os


def read_category(category, name):
    category = category.lower()
    name = name.lower()
    if os.path.exists('pantry.json'):
        try:
            with open('pantry.json') as f:
                data = json.load(f)
        except ValueError:
            data = {}
    else:
        data = {}

    if category in data:
        if name not in data[category]:
            data[category].append(name)
    else:
        data[category] = [name]

    with open('pantry.json', 'w') as outfile:
        json.dump(data, outfile)
