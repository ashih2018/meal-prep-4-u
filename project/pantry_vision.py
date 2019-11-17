import io
import os
import requests

# Imports the Google Cloud client library
from google.cloud import vision

from google.oauth2 import service_account

def pantry_vision():
    credentials = service_account.Credentials.from_service_account_file(
        "C:\\Users\\Stella\\Documents\\BostonHacks-56a57960ca1e.json")

    API_KEY = "fa7c3e4e3bf74b55b573701f96e6c8cb"

    # defining the api-endpoint
    BASE_URL = "https://api.spoonacular.com/recipes/parseIngredients?apiKey=" + API_KEY


    client = vision.ImageAnnotatorClient(credentials=credentials)
    # client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath('resources/fridge.jpg')

    # Loads the image into memory

    with open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    for object in objects:
        data = {'ingredientList': object,
                'servings': 0,
                'includeNutrition': False}
        r = requests.post(url=BASE_URL, data=data)
        Pantry.


        # sending post request and saving response as response object
        r = requests.post(url=BASE_URL, data=data)
    #     print(object_.name)
    # your API key here
    API_KEY = "fa7c3e4e3bf74b55b573701f96e6c8cb"

    # defining the api-endpoint
    BASE_URL = "https://api.spoonacular.com/recipes/parseIngredients?apiKey=" + API_KEY



    # data to be sent to api
    data = {'ingredientList': 'broccoli',
            'servings': 2,
            'includeNutrition': False}

    # sending post request and saving response as response object
    r = requests.post(url=BASE_URL, data=data)
    print("the response text is '" + r.json()[0]["aisle"] + "'")

if __name__ == '__main__':
    pantry_vision()
