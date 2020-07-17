from clarifai.rest import ClarifaiApp
import json
import os
import shutil

# Access your application
clarifai_app = ClarifaiApp(api_key='INSERT_API_KEY_HERE')
# This is the General model id
clarifai_model = app.models.get(model_id='aaa03c23b3724a16a56b629203edc62c')

DIRECTORIES = ['puppy', 'tree', 'city', 'cream']
# Type out the full path to clarifai_images
clarifai_images_path = '<PATH_TO_FOLDER_OF_IMAGES>'

image_filenames = os.listdir(path)

# START CODING HERE

# 1. Loop through all the files in clarifai_images

    # 2. Use .predict_by_filename() on model to get the json response from Clarifai

    # 3. Create an empty list for the image tags

    # 4.  Loop through ['outputs'][0]['data']['concepts'] and append the items to the
    #     image tags list

    # 5. Move the files to the appropriate folder based on whether or not the image tag
    #    matches the name in DIRECTORIES
    #    Hint: Review your file organizer
