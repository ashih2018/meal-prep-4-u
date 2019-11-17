import os
import requests

# Imports the Google Cloud client library
from google.cloud import vision
from google.oauth2 import service_account

from project.pantry import read_category


def pantry_vision():
    credentials = service_account.Credentials.from_service_account_file(
        "C:\\Users\\Stella\\Documents\\BostonHacks-56a57960ca1e.json")

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

    for object_ in objects:
        read_category(str(object_.name))


if __name__ == '__main__':
    pantry_vision()
