import json


class Recipe:
    def __init__(self, full_recipe_json):
        self.title = full_recipe_json["title"]
        self.source_url = full_recipe_json["sourceUrl"]
        self.image_url = full_recipe_json["image"]
        self.required_time = full_recipe_json["readyInMinutes"]
        self.ext_ingredients = full_recipe_json["extendedIngredients"]
        self.servings = full_recipe_json["servings"]
        self.nutrition = full_recipe_json["nutrition"]

    def to_json(self):
        dictionary = {"title": self.title,
                      "sourceUrl": self.source_url,
                      "imageUrl": self.image_url,
                      "requiredTime": self.required_time,
                      "ingredients": self.ext_ingredients,
                      "servings": self.servings,
                      "nutritionFacts": self.nutrition}
        return json.dumps(dictionary)
