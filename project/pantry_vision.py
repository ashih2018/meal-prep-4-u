import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("C:\\Users\\Stella\\Documents\\BostonHacks-56a57960ca1e.json")

client = vision.ImageAnnotatorClient(credentials=credentials)
# Instantiates a client

# The name of the image file to annotate
file_name = os.path.abspath('resources/fridge.jpg')

# Loads the image into memory

with open(file_name, 'rb') as image_file:
    content = image_file.read()
image = vision.types.Image(content=content)

objects = client.object_localization(
    image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
    print(object_.name)
