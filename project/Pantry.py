import json


def read_category(name, category, amount):
    ingredient = {name: {{'category': category}, {'amount': amount}}}
    ingredient_json = json.dumps(ingredient)  # string form of JSON
    with open('pantry.json', 'a') as outfile:
        json.dump(ingredient_json, outfile)
