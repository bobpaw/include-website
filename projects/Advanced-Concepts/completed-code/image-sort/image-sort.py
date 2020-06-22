from clarifai.rest import ClarifaiApp
import json
import os
import shutil

DIRECTORIES = ["puppy", "tree", "city", "cream"]

app = ClarifaiApp(api_key="a72c7ea1edbf4888880e399ab3a6c288")

model = app.models.get(model_id="aaa03c23b3724a16a56b629203edc62c")

path = '<PATH_TO_FOLDER_OF_IMAGES>'

list_ = os.listdir(path)

for file_ in list_:
    response = model.predict_by_filename(path+'/'+file_)
    img_tags = []
    for x in response['outputs'][0]['data']['concepts']:
        img_tags.append(x["name"])

    img_folder = ''
    for tag in img_tags:
        if tag in DIRECTORIES:
            img_folder = tag

    if os.path.exists(path+'/'+img_folder):
        shutil.move(path+'/'+file_,path+'/'+img_folder+'/'+file_)
            #If the directory does not exist, it creates a new directory
    else:
        os.makedirs(path+'/'+img_folder)
        shutil.move(path+'/'+file_,path+'/'+img_folder+'/'+file_)
