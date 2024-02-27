import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Charger les données du Pokédex depuis le fichier JSON
with open('pokemon/pokedex.json', 'r') as file:
    pokedex_data = json.load(file)

class PokedexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex")

        self.create_widgets()

    def create_widgets(self):
        # Créer la barre de recherche
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var, font=("Arial", 16), width=40)
        self.search_entry.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # Créer une frame pour la liste déroulante des suggestions
        self.suggestion_frame = ttk.Frame(self.root)
        self.suggestion_frame.grid(row=1, column=0, padx=20, pady=20, sticky='w', columnspan=2)

        self.suggestion_listbox = tk.Listbox(self.suggestion_frame, width=40, font=("Arial", 14), bg="White")
        self.suggestion_listbox.grid(row=0, column=0, sticky='w', columnspan=2)
        self.suggestion_listbox.grid_remove()  # Cacher la liste au début

        # Lier la fonction de suggestion à la frappe de touche
        self.search_var.trace_add('write', self.show_suggestions)

        # Lier la fonction de recherche au clic sur un élément de la liste
        self.suggestion_listbox.bind('<<ListboxSelect>>', self.on_suggestion_select)

        self.search_button = ttk.Button(self.root, text="Rechercher", command=self.search_pokemon, width=20)
        self.search_button.grid(row=0, column=2, padx=20, pady=20)

        # Créer la zone d'affichage des informations du Pokémon
        self.pokemon_info_frame = ttk.Frame(self.root)
        self.pokemon_info_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky='w')  # Alignement à gauche

        labels = [
            "Nom:", "Numéro:", "Types:", "PV:", "Attaque:", "Défense:",
            "Niveau:", "Évolution:", "Niveau d'évolution:"
        ]

        self.label_vars = [tk.StringVar() for _ in range(len(labels))]

        for i, label_text in enumerate(labels):
            label = ttk.Label(self.pokemon_info_frame, text=label_text, font=("Arial", 14), anchor='w')  # Alignement à gauche
            label.grid(row=i, column=0, sticky='w', padx=10, pady=10)
            value_label = ttk.Label(self.pokemon_info_frame, textvariable=self.label_vars[i], font=("Arial", 15), anchor='w')  # Alignement à gauche
            value_label.grid(row=i, column=1, sticky='w', padx=10, pady=10)

        # Créer la zone d'affichage de l'image du Pokémon avec une bordure
        self.pokemon_image_frame = ttk.Frame(self.root)
        self.pokemon_image_frame.grid(row=2, column=3, padx=20, pady=20)

        # Ajout de l'espace entre l'image et la bordure
        border_space = 10

        # Utiliser un Label standard pour la bordure
        self.pokemon_image_label = tk.Label(self.pokemon_image_frame, bd=5, relief="raised", bg="gray", border=5)
        self.pokemon_image_label.pack(padx=border_space, pady=border_space)

    def show_suggestions(self, *args):
        # Effacer les suggestions actuelles
        self.suggestion_listbox.delete(0, tk.END)

        # Récupérer le texte de la barre de recherche
        search_text = self.search_var.get().lower()

        # Afficher les suggestions basées sur le début des lettres
        for pokemon in pokedex_data["pokemons"]:
            if search_text and pokemon["nom"].lower().startswith(search_text):
                self.suggestion_listbox.insert(tk.END, pokemon["nom"])

        # Afficher la liste si elle a des éléments, sinon la cacher
        if self.suggestion_listbox.size() > 0:
            self.suggestion_listbox.grid()
            self.suggestion_frame.grid(row=1, column=0, padx=20, pady=20, sticky='w', columnspan=2)
        else:
            self.suggestion_listbox.grid_remove()
            self.suggestion_frame.grid_remove()

    def on_suggestion_select(self, event):
        # Cette fonction est appelée lorsqu'un élément de la liste est sélectionné
        selected_index = self.suggestion_listbox.curselection()
        if selected_index:
            selected_pokemon = self.suggestion_listbox.get(selected_index)
            self.search_var.set(selected_pokemon)
            self.search_pokemon()

    def search_pokemon(self, *args):
        # Réinitialiser les labels
        for var in self.label_vars:
            var.set("")

        # Cacher la liste de suggestions
        self.suggestion_listbox.grid_remove()
        self.suggestion_frame.grid_remove()

        # Récupérer le nom du Pokémon recherché en minuscules
        search_name = self.search_var.get().lower()

        # Chercher le Pokémon dans le Pokédex
        found_pokemon = None
        for pokemon in pokedex_data["pokemons"]:
            if pokemon["nom"].lower() == search_name:
                found_pokemon = pokemon
                break

        # Afficher les informations du Pokémon s'il est trouvé
        if found_pokemon:
            self.label_vars[0].set(f" {found_pokemon['nom']}")
            self.label_vars[1].set(f" {found_pokemon['numero']}")
            self.label_vars[2].set(f" {', '.join(found_pokemon['types'])}")
            self.label_vars[3].set(f" {found_pokemon['pv']}")
            self.label_vars[4].set(f" {found_pokemon['atk']}")
            self.label_vars[5].set(f" {found_pokemon['defense']}")
            self.label_vars[6].set(f" {found_pokemon['niveau']}")
            self.label_vars[7].set(f" {found_pokemon['evolution']}")
            self.label_vars[8].set(f" {found_pokemon['evolution_niveau']}")

            # Charger l'image du Pokémon avec une bordure
            self.load_pokemon_image(found_pokemon['numero'])

        else:
            # Afficher un message si le Pokémon n'est pas trouvé.
            self.label_vars[0].set("Pokémon non trouvé.")

    def load_pokemon_image(self, pokemon_number):
        # Construire le chemin de l'image en fonction du numéro du Pokémon
        image_filename = f"images/{pokemon_number}.png"  # Assurez-vous que le format de l'image est pris en charge

        # Charger l'image du Pokémon et l'afficher avec une bordure
        try:
            image_path = os.path.join(os.path.dirname(__file__), image_filename)
            image = Image.open(image_path)
            image = image.resize((300, 300), resample=Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.pokemon_image_label.config(image=photo)
            self.pokemon_image_label.image = photo

        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()
