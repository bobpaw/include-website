import requests
import json

pokemon = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')

poke_list = []
poke_json = pokemon.json()

for n in poke_json["results"]:
    poke_details = requests.get(n['url'])
    detail_json = poke_details.json()
    ability = detail_json["abilities"][0]["ability"]["name"]
    poke_list.append({'name':n["name"], 'ability':ability})


for i in poke_list:
    print(f"{i['name']} has the ability {i['ability']}")
