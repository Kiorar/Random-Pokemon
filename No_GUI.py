
import requests
import random


def get_pokemon():
    poke_id = random.randint(1, 1118) 
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        img_url = data['sprites']['front_default']
        weight = data['weight']
        height = data['height']
        print("Name:",name)
        print("Image URL:",img_url)
        print("Weight(hg):",weight)
        print("Height(dm)",height)
    else:
        print("error")

get_pokemon()
