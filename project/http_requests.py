import requests
import json

FIND_BY_INGREDIENTS = "https://api.spoonacular.com/recipes/findByIngredients"
RECIPES_BULK = "https://api.spoonacular.com/recipes/informationBulk"
QUERIES_FILE = "queries.json"
API_KEY = "91c872bcb84c442f8599092ea7b1affb"


def get_request(url, params, api_key):
    """
    A query is:
    {"arguments":{"url":String, "params":Object},
     "result":String}
    The queries file contains a list of queries.
    """
    past_queries_raw = read_file(QUERIES_FILE)
    past_queries = []
    if past_queries_raw:
        past_queries = json.loads(past_queries_raw)
        matching_queries = list(filter(matches_args(url, params), past_queries))
        if matching_queries:
            return matching_queries[0]["result"]

    print("Sending server request...")
    params["apiKey"] = api_key
    response = requests.get(url=url, params=params)
    if response.status_code == 400 or response.status_code == 401:
        raise Exception("Received server error")
    params.pop("apiKey")
    query = {"arguments": {"url": url, "params": params}, "result": json.loads(response.text)}
    past_queries.append(query)
    write_file(QUERIES_FILE, json.dumps(past_queries))

    return json.loads(response.text)


def matches_args(url, params):
    def query_matches_args(query):
        return query["arguments"]["url"] == url and query["arguments"]["params"] == params
    return query_matches_args


def read_file(filename):
    f = open(filename, "r")
    ret = f.read()
    f.close()
    return ret


def write_file(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()


def run(api_key):
    parameters = {"ingredients": "onions,tomatoes,garlic,parsley,beef",
                  "number": 10,
                  "ranking": 2}

    recipes_array = get_request(FIND_BY_INGREDIENTS, parameters, api_key)
    recipe_ids_strings = list(map(lambda recipe: str(recipe["id"]), recipes_array))
    recipe_ids_string = ",".join(recipe_ids_strings)

    parameters = {"ids": recipe_ids_string,
                  "includeNutrition": "true"}
    full_recipes_list = get_request(RECIPES_BULK, parameters, api_key)
    print(full_recipes_list)


class Recipe:
    def __init__(self, full_recipe_json):
        self.title = full_recipe_json["title"]
        self.source_url = full_recipe_json["sourceUrl"]
        self.image_url = full_recipe_json["image"]
        self.required_time = full_recipe_json["readyInMinutes"]
        self.ext_ingredients = full_recipe_json["extendedIngredients"]
        self.servings = full_recipe_json["servings"]
        self.nutrition = full_recipe_json["nutrition"]



if __name__ == '__main__':
    run(API_KEY)
