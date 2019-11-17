import requests
import json

from project.recipe import Recipe

FIND_BY_INGREDIENTS = "https://api.spoonacular.com/recipes/findByIngredients"
ADVANCED_SEARCH = "https://api.spoonacular.com/recipes/complexSearch"
MEAL_PLAN = "https://api.spoonacular.com/recipes/mealplans/generate"
RECIPES_BULK = "https://api.spoonacular.com/recipes/informationBulk"
QUERIES_FILE = "queries.json"
NUM_ENTRIES = 5
RANKING = 2
DEFAULT_CALORIES = 2000


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
    return lambda query: query["arguments"]["url"] == url and query["arguments"]["params"] == params


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


def search_by_ingredients(ingredients, api_key, num_results=NUM_ENTRIES):
    """
    :param ingredients: a list of strings representing ingredient names
    :param api_key: the API key as a string
    :param num_results: the number of results to return
    :return: a list of Recipe objects
    """
    ingredients_string = ",".join(ingredients)
    parameters = {"ingredients": ingredients_string,
                  "number": num_results,
                  "ranking": RANKING}
    recipes_array = get_request(FIND_BY_INGREDIENTS, parameters, api_key)
    return get_full_recipes_list(recipes_array, lambda recipe: str(recipe["id"]), api_key)


def search_advanced(query, cuisines, diet, intolerances, include_ingredients, exclude_ingredients, dish_type,
                    max_ready_time, carb_range, protein_range, fat_range, calories_range, api_key,
                    num_results=NUM_ENTRIES):
    """
    :param num_results: the number of results
    :param api_key: the API key
    :param query: String (none if empty)
    :param cuisines: List (none if empty)
    :param diet: String (none if empty)
    :param intolerances: List (none if empty)
    :param include_ingredients: List (none if empty)
    :param exclude_ingredients: List (none if empty)
    :param dish_type: String (none if empty)
    :param max_ready_time: int (none if 0)
    :param carb_range: tuple (none if None)
    :param protein_range: tuple (none if None)
    :param fat_range: tuple (none if None)
    :param calories_range: tuple (none if None)
    :return: List of Recipes
    """
    parameters = {}
    if query:
        parameters["query"] = query
    if cuisines:
        parameters["cuisine"] = ",".join(cuisines)
    if diet:
        parameters["diet"] = diet
    if intolerances:
        parameters["intolerances"] = ",".join(intolerances)
    if include_ingredients:
        parameters["includeIngredients"] = ",".join(include_ingredients)
    if exclude_ingredients:
        parameters["excludeIngredients"] = ",".join(exclude_ingredients)
    if dish_type:
        parameters["type"] = dish_type
    if max_ready_time:
        parameters["maxReadyTime"] = max_ready_time
    if carb_range:
        parameters["minCarbs"] = carb_range[0]
        parameters["maxCarbs"] = carb_range[1]
    if protein_range:
        parameters["minProtein"] = protein_range[0]
        parameters["maxProtein"] = protein_range[1]
    if fat_range:
        parameters["minFat"] = fat_range[0]
        parameters["maxFat"] = fat_range[1]
    if calories_range:
        parameters["minCalories"] = calories_range[0]
        parameters["maxCalories"] = calories_range[1]
    parameters["number"] = num_results

    recipes_array = get_request(ADVANCED_SEARCH, parameters, api_key)["results"]
    return get_full_recipes_list(recipes_array, lambda recipe: str(recipe["id"]), api_key)


def meal_plan(time_frame, calories, diet, exclude, api_key):
    """
    :param api_key: the API key
    :param time_frame: String - day or week (week by default)
    :param calories: int (2000 if 0)
    :param diet: String (none if false)
    :param exclude: List of String - ingredients/allergens (none if false)
    :return: List of Recipes
    """
    parameters = {}
    if not time_frame:
        time_frame = "week"
    parameters["timeFrame"] = time_frame
    if not calories:
        calories = DEFAULT_CALORIES
    parameters["targetCalories"] = calories
    if diet:
        parameters["diet"] = diet
    if exclude:
        parameters["exclude"] = ",".join(exclude)
    recipes_array = get_request(ADVANCED_SEARCH, parameters, api_key)["items"]
    return get_full_recipes_list(recipes_array, lambda recipe: str(json.loads(recipe["value"])["id"]), api_key)


def get_full_recipes_list(recipes_list, recipe_to_id, api_key):
    """
    :param api_key: API key
    :param recipes_list: List of recipes in a different format
    :param recipe_to_id: function to convert a recipe in the input format to its ID
    :return: a list of Recipe objects
    """
    recipe_ids_strings = list(map(recipe_to_id, recipes_list))
    recipe_ids_string = ",".join(recipe_ids_strings)
    parameters = {"ids": recipe_ids_string,
                  "includeNutrition": "true"}
    full_recipes_list = get_request(RECIPES_BULK, parameters, api_key)
    return list(map(lambda recipe: Recipe(recipe), full_recipes_list))


if __name__ == '__main__':
    run("")  # replace with API key
