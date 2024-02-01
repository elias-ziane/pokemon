import json
import random

class Pok:
    def __init__(self) -> None:
        self.nom = self.get_infos('nom')
        self.num = self.get_infos('numero')
        self.pv = self.get_infos('pv')
        self.atk = self.get_infos('atk')
        self.defense = self.get_infos('defense')
        self.types = self.get_infos('types')
    
    def get_infos(self, name):
        with open('pokedex_user.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Génère un index aléatoire entre 0 et len(data['pokemons']) - 1 inclus
            random_index = random.randint(0, len(data['pokemons']) - 1)
            random_pokemon = data['pokemons'][random_index]
            return random_pokemon[name]

if __name__ == "__main__":
    pok1 = Pok()
    print(f"{pok1.nom}")
