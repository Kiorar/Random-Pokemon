import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random


def get_pokemon():
    poke_id = random.randint(1, 1118) 
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        img_url = data['sprites']['front_default']
        name_label.config(text=name)
        weight = data['weight']
        height = data['height']
        weight_label.config(text=weight)
        height_label.config(text=height)
        img_response = requests.get(img_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data = img_data.resize((500, 500))  
        img_tk = ImageTk.PhotoImage(img_data)
        img_label.config(image=img_tk)
        img_label.image = img_tk  
    else:
        name_label.config(text="Error")

root = tk.Tk()
root.title("Pokémon thing")

root.geometry("1920x1080")


name_label = Label(root, text="Click button to get Pokémon",font=("Arial", 20, "bold"))
name_label.pack(pady=10)

weight1_label = Label(root, text="Weight:(hg)",font=("Arial",15))
weight1_label.pack(pady=10)


weight_label = Label(root, text="Weight will be displayed here",font=("Arial",15))
weight_label.pack(pady=10)

height1_label = Label(root, text="Height:(dm)",font=("Arial",15))
height1_label.pack(pady=10)
height_label = Label(root, text="Height will be displayed here",font=("Arial",15))
height_label.pack(pady=10)



img_label = Label(root)
img_label.pack(pady=10)


button = Button(root, text="Get Pokémon", command=get_pokemon,font=("Arial", 10, "bold"))
button.pack(pady=10)

root.mainloop()

