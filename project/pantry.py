import json
import os
import requests

API_KEY = "89cc44a62bab4f498f7afb7257f799dc"
BASE_URL = "https://api.spoonacular.com/recipes/parseIngredients?apiKey=" + API_KEY


def read_category(name):
    name = name.lower()
    if os.path.exists('pantry.json'):
        try:
            with open('pantry.json') as f:
                food = json.load(f)
        except ValueError:
            food = {}
    else:
        food = {}

    data = {'ingredientList': "broccoli",
            'servings': 0,
            'includeNutrition': False}
    r = requests.post(url=BASE_URL, data=data)

    if "aisle" not in r.json()[0]:
        return

    category = r.json()[0]["aisle"].lower()

    if category in food:
        if name not in food[category]:
            food[category].append(name)
    else:
        food[category] = [name]

    with open('pantry.json', 'w') as outfile:
        json.dump(food, outfile)


def read_pantry():
    if os.path.exists('pantry.json'):
        try:
            with open('pantry.json') as f:
                food = json.load(f)
        except ValueError:
            food = {}
    else:
        food = {}

    lst = []
    for category in food:
        for item in food[category]:
            lst.append(item)
    print(lst)


if __name__ == '__main__':
    read_pantry()
