import requests
import json

FIND_BY_INGREDIENTS = "https://api.spoonacular.com/recipes/findByIngredients"
RECIPES_BULK = "https://api.spoonacular.com/recipes/informationBulk"
RECIPES_FILE = "recipes.json"
FULL_RECIPES_FILE = "full_recipes.json"

API_KEY = ""


def get_request(url, params, api_key):
    params["apiKey"] = api_key
    response = requests.get(url=url, params=params)
    if response.status_code == 400 or response.status_code == 401:
        raise Exception("Received server error")
    return response.text


def read_file(filename):
    f = open(filename, "r")
    ret = f.read()
    f.close()
    return ret


def write_file(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()


def run():
    recipes_json = read_file(RECIPES_FILE)

    if not recipes_json:
        print("Sending server request...")
        parameters = {"ingredients": "onions,tomatoes,garlic,parsley,beef",
                      "number": 10,
                      "ranking": 2}

        recipes_json = get_request(FIND_BY_INGREDIENTS, parameters, API_KEY)
        write_file(RECIPES_FILE, recipes_json)

    print(recipes_json)
    recipes_array = json.loads(recipes_json)
    print(recipes_array)
    recipe_ids_strings = list(map(lambda recipe: str(recipe["id"]), recipes_array))
    print(recipe_ids_strings)
    recipe_ids_string = ",".join(recipe_ids_strings)
    print(recipe_ids_string)

    full_recipes_json = read_file(FULL_RECIPES_FILE)

    if not full_recipes_json:
        print("Sending server request...")
        parameters = {"ids": recipe_ids_string,
                      "includeNutrition": "true"}
        full_recipes_json = get_request(RECIPES_BULK, parameters, API_KEY)
        write_file(FULL_RECIPES_FILE, full_recipes_json)

    print(full_recipes_json)
    full_recipes_list = json.loads(full_recipes_json)
    print(full_recipes_list)


if __name__ == '__main__':
    run()
