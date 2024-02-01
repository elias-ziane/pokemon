import json
import tkinter as tk
from tkinter import ttk
from random import randint

class Pokemon:
    def __init__(self, nom, numero, pv, atk, defense, types, niveau, evolution=None, evolution_niveau=None):
        self.nom = nom
        self.numero = numero
        self.pv = pv
        self.atk = atk
        self.defense = defense
        self.types = types
        self.niveau = niveau
        self.evolution = evolution
        self.evolution_niveau = evolution_niveau
        
def check_duplicate(pokedex_data, new_pokemon):
    for pokemon_data in pokedex_data["pokemons"]:
        if new_pokemon["numero"] == pokemon_data["numero"] or new_pokemon["nom"] == pokemon_data["nom"]:
            return True  # Doublon trouvé
    return False  # Pas de doublon
        
types_pokemon = [
    "Normal", "Feu", "Eau", "Plante", "Electrique", "Glace", "Combat", "Poison", "Sol",
    "Vol", "Psy", "Insecte", "Roche", "Spectre", "Dragon", "Ténèbres", "Acier", "Fée"
]

pokemon_liste = [
    Pokemon(nom="Bulbizarre", numero="001", pv=45, atk=49, defense=49, types=["Plante", "Poison"], niveau=1, evolution="Herbizarre", evolution_niveau=10),
    Pokemon(nom="Herbizarre", numero="002", pv=60, atk=62, defense=63, types=["Plante", "Poison"], niveau=10, evolution="Florizarre", evolution_niveau=15),
    Pokemon(nom="Florizarre", numero="003", pv=80, atk=82, defense=83, types=["Plante", "Poison"], niveau=15),

    Pokemon(nom="Salamèche", numero="004", pv=39, atk=52, defense=43, types=["Feu"], niveau=1, evolution="Reptincel", evolution_niveau=10),
    Pokemon(nom="Reptincel", numero="005", pv=58, atk=64, defense=58, types=["Feu"], niveau=10, evolution="Dracaufeu", evolution_niveau=15),
    Pokemon(nom="Dracaufeu", numero="006", pv=78, atk=84, defense=78, types=["Feu", "Vol"], niveau=15),

    Pokemon(nom="Carapuce", numero="007", pv=44, atk=48, defense=65, types=["Eau"], niveau=1, evolution="Carabaffe", evolution_niveau=10),
    Pokemon(nom="Carabaffe", numero="008", pv=59, atk=63, defense=80, types=["Eau"], niveau=10, evolution="Tortank", evolution_niveau=15),
    Pokemon(nom="Tortank", numero="009", pv=79, atk=83, defense=100, types=["Eau"], niveau=15),

    Pokemon(nom="Chenipan", numero="010", pv=45, atk=30, defense=35, types=["Insecte"], niveau=1, evolution="Chrysacier", evolution_niveau=10),
    Pokemon(nom="Chrysacier", numero="011", pv=50, atk=20, defense=55, types=["Insecte"], niveau=10, evolution="Papilusion", evolution_niveau=15),
    Pokemon(nom="Papilusion", numero="012", pv=60, atk=45, defense=50, types=["Insecte", "Vol"], niveau=15),

    Pokemon(nom="Aspicot", numero="013", pv=40, atk=35, defense=30, types=["Insecte", "Poison"], niveau=1, evolution="Coconfort", evolution_niveau=10),
    Pokemon(nom="Coconfort", numero="014", pv=45, atk=25, defense=50, types=["Insecte", "Poison"], niveau=10, evolution="Dardagnan", evolution_niveau=15),
    Pokemon(nom="Dardagnan", numero="015", pv=65, atk=90, defense=40, types=["Insecte", "Poison"], niveau=15),

    Pokemon(nom="Roucool", numero="016", pv=40, atk=45, defense=40, types=["Normal", "Vol"], niveau=1, evolution="Roucoups", evolution_niveau=10),
    Pokemon(nom="Roucoups", numero="017", pv=55, atk=60, defense=55, types=["Normal", "Vol"], niveau=10, evolution="Roucarnage", evolution_niveau=15),
    Pokemon(nom="Roucarnage", numero="018", pv=80, atk=80, defense=75, types=["Normal", "Vol"], niveau=15),

    Pokemon(nom="Rattata", numero="019", pv=30, atk=56, defense=35, types=["Normal"], niveau=1, evolution="Rattatac", evolution_niveau=10),
    Pokemon(nom="Rattatac", numero="020", pv=55, atk=81, defense=60, types=["Normal"], niveau=10),

    Pokemon(nom="Piafabec", numero="021", pv=40, atk=60, defense=30, types=["Normal", "Vol"], niveau=1, evolution="Rapasdepic", evolution_niveau=10),
    Pokemon(nom="Rapasdepic", numero="022", pv=65, atk=90, defense=65, types=["Normal", "Vol"], niveau=10),

    Pokemon(nom="Abo", numero="023", pv=35, atk=60, defense=44, types=["Poison"], niveau=1, evolution="Arbok", evolution_niveau=10),
    Pokemon(nom="Arbok", numero="024", pv=60, atk=85, defense=69, types=["Poison"], niveau=10),

    Pokemon(nom="Pikachu", numero="025", pv=35, atk=55, defense=40, types=["Electrique"], niveau=1, evolution="Raichu", evolution_niveau=10),
    Pokemon(nom="Raichu", numero="026", pv=60, atk=90, defense=55, types=["Electrique"], niveau=10),

    Pokemon(nom="Sabelette", numero="027", pv=50, atk=75, defense=85, types=["Sol"], niveau=1, evolution="Sablaireau", evolution_niveau=10),
    Pokemon(nom="Sablaireau", numero="028", pv=75, atk=100, defense=110, types=["Sol"], niveau=10),

    Pokemon(nom="Nidoran.F", numero="029", pv=55, atk=47, defense=52, types=["Poison"], niveau=1, evolution="Nidorina", evolution_niveau=10),
    Pokemon(nom="Nidorina", numero="030", pv=70, atk=62, defense=67, types=["Poison"], niveau=10, evolution="Nidoqueen", evolution_niveau=15),
    Pokemon(nom="Nidoqueen", numero="031", pv=90, atk=92, defense=87, types=["Poison", "Sol"], niveau=15),

    Pokemon(nom="Nidoran.M", numero="032", pv=46, atk=57, defense=40, types=["Poison"], niveau=1, evolution="Nidorino", evolution_niveau=10),
    Pokemon(nom="Nidorino", numero="033", pv=61, atk=72, defense=57, types=["Poison"], niveau=10, evolution="Nidoking", evolution_niveau=15),
    Pokemon(nom="Nidoking", numero="034", pv=81, atk=102, defense=77, types=["Poison", "Sol"], niveau=15),

    Pokemon(nom="Mélofée", numero="035", pv=70, atk=45, defense=48, types=["Fée"], niveau=1, evolution="Mélodefle", evolution_niveau=10),
    Pokemon(nom="Mélodefle", numero="036", pv=95, atk=70, defense=73, types=["Fée"], niveau=10),

    Pokemon(nom="Goupix", numero="037", pv=38, atk=41, defense=40, types=["Feu"], niveau=1, evolution="Feunard", evolution_niveau=10),
    Pokemon(nom="Feunard", numero="038", pv=73, atk=76, defense=75, types=["Feu"], niveau=10),

    Pokemon(nom="Rondoudou", numero="039", pv=115, atk=45, defense=20, types=["Normal", "Fée"], niveau=1, evolution="Grodoudou", evolution_niveau=10),
    Pokemon(nom="Grodoudou", numero="040", pv=140, atk=70, defense=45, types=["Normal", "Fée"], niveau=10),

    Pokemon(nom="Nosferapti", numero="041", pv=40, atk=45, defense=35, types=["Poison", "Vol"], niveau=1, evolution="Nosferalto", evolution_niveau=10),
    Pokemon(nom="Nosferalto", numero="042", pv=75, atk=80, defense=70, types=["Poison", "Vol"], niveau=10),

    Pokemon(nom="Mystherbe", numero="043", pv=45, atk=50, defense=55, types=["Plante", "Poison"], niveau=1, evolution="Ortide", evolution_niveau=10),
    Pokemon(nom="Ortide", numero="044", pv=60, atk=65, defense=70, types=["Plante", "Poison"], niveau=10, evolution="Rafflesia", evolution_niveau=15),
    Pokemon(nom="Rafflesia", numero="045", pv=75, atk=80, defense=85, types=["Plante", "Poison"], niveau=15),

    Pokemon(nom="Paras", numero="046", pv=35, atk=70, defense=55, types=["Insecte", "Plante"], niveau=1, evolution="Parasect", evolution_niveau=10),
    Pokemon(nom="Parasect", numero="047", pv=60, atk=95, defense=80, types=["Insecte", "Plante"], niveau=10),

    Pokemon(nom="Mimitoss", numero="048", pv=60, atk=55, defense=50, types=["Insecte", "Poison"], niveau=1, evolution="Aéromite", evolution_niveau=10),
    Pokemon(nom="Aéromite", numero="049", pv=70, atk=65, defense=60, types=["Insecte", "Poison"], niveau=10),

    Pokemon(nom="Taupiqueur", numero="050", pv=10, atk=55, defense=25, types=["Sol"], niveau=1, evolution="Triopikeur", evolution_niveau=10),
    Pokemon(nom="Triopikeur", numero="051", pv=35, atk=80, defense=50, types=["Sol"], niveau=10),

    Pokemon(nom="Miaouss", numero="052", pv=40, atk=45, defense=35, types=["Normal"], niveau=1, evolution="Persian", evolution_niveau=10),
    Pokemon(nom="Persian", numero="053", pv=65, atk=70, defense=60, types=["Normal"], niveau=10),

    Pokemon(nom="Psykokwak", numero="054", pv=50, atk=52, defense=48, types=["Eau"], niveau=1, evolution="Akwakwak", evolution_niveau=10),
    Pokemon(nom="Akwakwak", numero="055", pv=80, atk=82, defense=78, types=["Eau"], niveau=10),

    Pokemon(nom="Férosinge", numero="056", pv=40, atk=80, defense=35, types=["Combat"], niveau=1, evolution="Colossinge", evolution_niveau=10),
    Pokemon(nom="Colossinge", numero="057", pv=65, atk=105, defense=60, types=["Combat"], niveau=10),

    Pokemon(nom="Caninos", numero="058", pv=55, atk=70, defense=45, types=["Feu"], niveau=1, evolution="Arcanin", evolution_niveau=10),
    Pokemon(nom="Arcanin", numero="059", pv=90, atk=110, defense=80, types=["Feu"], niveau=10),

    Pokemon(nom="Ptitard", numero="060", pv=40, atk=50, defense=40, types=["Eau"], niveau=1, evolution="Têtarte", evolution_niveau=10),
    Pokemon(nom="Têtarte", numero="061", pv=65, atk=65, defense=65, types=["Eau"], niveau=10, evolution="Tartard", evolution_niveau=15),
    Pokemon(nom="Tartard", numero="062", pv=90, atk=95, defense=95, types=["Eau","Combat"], niveau=15),

    Pokemon(nom="Abra", numero="063", pv=25, atk=20, defense=15, types=["Psy"], niveau=1, evolution="Kadabra", evolution_niveau=10),
    Pokemon(nom="Kadabra", numero="064", pv=40, atk=35, defense=30, types=["Psy"], niveau=10, evolution="Alakazam", evolution_niveau=15),
    Pokemon(nom="Alakazam", numero="065", pv=55, atk=50, defense=45, types=["Psy"], niveau=15),

    Pokemon(nom="Machoc", numero="066", pv=70, atk=80, defense=50, types=["Combat"], niveau=1, evolution="Machopeur", evolution_niveau=10),
    Pokemon(nom="Machopeur", numero="067", pv=80, atk=100, defense=70, types=["Combat"], niveau=10, evolution="Mackogneur", evolution_niveau=15),
    Pokemon(nom="Mackogneur", numero="068", pv=90, atk=130, defense=80, types=["Combat"], niveau=15),

    Pokemon(nom="Chétiflor", numero="069", pv=50, atk=75, defense=35, types=["Plante","Poison"], niveau=1, evolution="Boustiflor", evolution_niveau=10),
    Pokemon(nom="Boustiflor", numero="070", pv=65, atk=90, defense=50, types=["Plante","Poison"], niveau=10, evolution="Empiflor", evolution_niveau=15),
    Pokemon(nom="Empiflor", numero="071", pv=80, atk=105, defense=85, types=["Plante","Poison"], niveau=15),
    
    Pokemon(nom="Tentacool", numero="072", pv=40, atk=40, defense=35, types=["Eau", "Poison"], niveau=1, evolution="Tentacruel", evolution_niveau=10),
    Pokemon(nom="Tentacruel", numero="073", pv=80, atk=70, defense=65, types=["Eau", "Poison"], niveau=10),

    Pokemon(nom="Racaillou", numero="074", pv=40, atk=80, defense=100, types=["Roche", "Sol"], niveau=1, evolution="Gravalanch", evolution_niveau=10),
    Pokemon(nom="Gravalanch", numero="075", pv=55, atk=95, defense=115, types=["Roche", "Sol"], niveau=10, evolution="Grolem", evolution_niveau=15),
    Pokemon(nom="Grolem", numero="076", pv=80, atk=110, defense=130, types=["Roche", "Sol"], niveau=15),

    Pokemon(nom="Ponyta", numero="077", pv=50, atk=85, defense=55, types=["Feu"], niveau=1, evolution="Galopa", evolution_niveau=10),
    Pokemon(nom="Galopa", numero="078", pv=65, atk=100, defense=70, types=["Feu"], niveau=10),

    Pokemon(nom="Ramoloss", numero="079", pv=90, atk=65, defense=65, types=["Eau", "Psy"], niveau=1, evolution="Flagadoss", evolution_niveau=10),
    Pokemon(nom="Flagadoss", numero="080", pv=95, atk=75, defense=110, types=["Eau", "Psy"], niveau=10),
    
    Pokemon(nom="Magnéti", numero="081", pv=25, atk=35, defense=70, types=["Electrique", "Acier"], niveau=1, evolution="Magnéton", evolution_niveau=10),
    Pokemon(nom="Magnéton", numero="082", pv=50, atk=60, defense=95, types=["Electrique", "Acier"], niveau=10),

    Pokemon(nom="Canarticho", numero="083", pv=52, atk=65, defense=55, types=["Normal", "Vol"], niveau=1),

    Pokemon(nom="Doduo", numero="084", pv=35, atk=85, defense=45, types=["Normal", "Vol"], niveau=1, evolution="Dodrio", evolution_niveau=10),
    Pokemon(nom="Dodrio", numero="085", pv=60, atk=110, defense=70, types=["Normal", "Vol"], niveau=10),

    Pokemon(nom="Otaria", numero="086", pv=65, atk=45, defense=55, types=["Eau", "Glace"], niveau=1, evolution="Lamantine", evolution_niveau=10),
    Pokemon(nom="Lamantine", numero="087", pv=90, atk=70, defense=80, types=["Eau", "Glace"], niveau=10),

    Pokemon(nom="Tadmorv", numero="088", pv=80, atk=80, defense=50, types=["Poison"], niveau=1, evolution="Grotadmorv", evolution_niveau=10),
    Pokemon(nom="Grotadmorv", numero="089", pv=105, atk=105, defense=75, types=["Poison"], niveau=10),

    Pokemon(nom="Kokiyas", numero="090", pv=30, atk=65, defense=100, types=["Eau"], niveau=1, evolution="Crustabri", evolution_niveau=10),
    Pokemon(nom="Crustabri", numero="091", pv=50, atk=95, defense=180, types=["Eau", "Glace"], niveau=10),

    Pokemon(nom="Fantominus", numero="092", pv=30, atk=35, defense=30, types=["Spectre", "Poison"], niveau=1, evolution="Spectrum", evolution_niveau=10),
    Pokemon(nom="Spectrum", numero="093", pv=45, atk=50, defense=45, types=["Spectre", "Poison"], niveau=10, evolution="Ectoplasma", evolution_niveau=15),
    Pokemon(nom="Ectoplasma", numero="094", pv=60, atk=65, defense=60, types=["Spectre", "Poison"], niveau=15),

    Pokemon(nom="Onix", numero="095", pv=35, atk=45, defense=160, types=["Roche", "Sol"], niveau=1),

    Pokemon(nom="Soporifik", numero="096", pv=60, atk=48, defense=45, types=["Psy"], niveau=1, evolution="Hypnomade", evolution_niveau=10),
    Pokemon(nom="Hypnomade", numero="097", pv=85, atk=73, defense=70, types=["Psy"], niveau=10),

    Pokemon(nom="Krabby", numero="098", pv=30, atk=105, defense=90, types=["Eau"], niveau=1, evolution="Krabboss", evolution_niveau=10),
    Pokemon(nom="Krabboss", numero="099", pv=55, atk=130, defense=115, types=["Eau"], niveau=10),
    
    Pokemon(nom="Voltorbe", numero="100", pv=40, atk=30, defense=50, types=["Electrique"], niveau=1, evolution="Électrode", evolution_niveau=10),
    Pokemon(nom="Électrode", numero="101", pv=60, atk=50, defense=70, types=["Electrique"], niveau=10),

    Pokemon(nom="Noeunoeuf", numero="102", pv=60, atk=40, defense=80, types=["Plante", "Psy"], niveau=1, evolution="Noadkoko", evolution_niveau=10),
    Pokemon(nom="Noadkoko", numero="103", pv=95, atk=85, defense=125, types=["Plante", "Psy"], niveau=10),

    Pokemon(nom="Osselait", numero="104", pv=50, atk=50, defense=95, types=["Sol"], niveau=1, evolution="Ossatueur", evolution_niveau=10),
    Pokemon(nom="Ossatueur", numero="105", pv=60, atk=80, defense=110, types=["Sol"], niveau=10),

    Pokemon(nom="Kicklee", numero="106", pv=50, atk=120, defense=53, types=["Combat"], niveau=1),

    Pokemon(nom="Tygnon", numero="107", pv=50, atk=105, defense=79, types=["Combat"], niveau=1),

    Pokemon(nom="Excelangue", numero="108", pv=90, atk=55, defense=75, types=["Normal"], niveau=1),

    Pokemon(nom="Smogo", numero="109", pv=40, atk=65, defense=95, types=["Poison"], niveau=1, evolution="Smogogo", evolution_niveau=10),
    Pokemon(nom="Smogogo", numero="110", pv=60, atk=90, defense=120, types=["Poison"], niveau=10),

    Pokemon(nom="Rhinocorne", numero="111", pv=80, atk=85, defense=95, types=["Sol", "Roche"], niveau=1, evolution="Rhinoféros", evolution_niveau=10),
    Pokemon(nom="Rhinoféros", numero="112", pv=105, atk=130, defense=120, types=["Sol", "Roche"], niveau=10),

    Pokemon(nom="Leveinard", numero="113", pv=250, atk=5, defense=5, types=["Normal"], niveau=1,),

    Pokemon(nom="Saquedeneu", numero="114", pv=65, atk=55, defense=115, types=["Plante"], niveau=1),

    Pokemon(nom="Kangourex", numero="115", pv=105, atk=95, defense=80, types=["Normal"], niveau=1),

    Pokemon(nom="Hypotrempe", numero="116", pv=30, atk=40, defense=70, types=["Eau"], niveau=1, evolution="Hypocéan", evolution_niveau=10),
    Pokemon(nom="Hypocéan", numero="117", pv=55, atk=65, defense=95, types=["Eau"], niveau=10),

    Pokemon(nom="Poissirène", numero="118", pv=45, atk=67, defense=60, types=["Eau"], niveau=1, evolution="Poissoroy", evolution_niveau=10),
    Pokemon(nom="Poissoroy", numero="119", pv=80, atk=92, defense=65, types=["Eau"], niveau=10),

    Pokemon(nom="Stari", numero="120", pv=30, atk=45, defense=55, types=["Eau"], niveau=1, evolution="Staross", evolution_niveau=10),
    Pokemon(nom="Staross", numero="121", pv=60, atk=75, defense=85, types=["Eau"], niveau=10),

    Pokemon(nom="M. Mime", numero="122", pv=40, atk=45, defense=65, types=["Psy", "Fée"], niveau=1),

    Pokemon(nom="Insécateur", numero="123", pv=70, atk=110, defense=80, types=["Insecte", "Vol"], niveau=1),

    Pokemon(nom="Lippoutou", numero="124", pv=65, atk=50, defense=35, types=["Glace", "Psy"], niveau=1,),
    
    Pokemon(nom="Élektek", numero="125", pv=65, atk=83, defense=57, types=["Électrique"], niveau=1),

    Pokemon(nom="Magmar", numero="126", pv=65, atk=95, defense=57, types=["Feu"], niveau=1,),
    
    Pokemon(nom="Scarabrute", numero="127", pv=65, atk=125, defense=100, types=["Insecte"], niveau=1),

    Pokemon(nom="Tauros", numero="128", pv=75, atk=100, defense=95, types=["Normal"], niveau=1),

    Pokemon(nom="Magicarpe", numero="129", pv=20, atk=10, defense=55, types=["Eau"], niveau=1, evolution="Léviator", evolution_niveau=10),
    Pokemon(nom="Léviator", numero="130", pv=95, atk=125, defense=79, types=["Eau", "Vol"], niveau=10),

    Pokemon(nom="Lokhlass", numero="131", pv=130, atk=85, defense=80, types=["Eau", "Glace"], niveau=1),

    Pokemon(nom="Métamorph", numero="132", pv=48, atk=48, defense=48, types=["Normal"], niveau=1),

# A MODIFIER CAR CE POKEMON PEUT CHOISIR SON STYLE ELEMENTAIRE
#-------------------------------------------------------------------------------------------------------------

    Pokemon(nom="Évoli", numero="133", pv=55, atk=55, defense=50, types=["Normal"], niveau=1, evolution="Aquali", evolution_niveau=10),
    Pokemon(nom="Aquali", numero="134", pv=130, atk=65, defense=60, types=["Eau"], niveau=10),
    Pokemon(nom="Pyroli", numero="135", pv=130, atk=60, defense=65, types=["Feu"], niveau=10),
    Pokemon(nom="Voltali", numero="136", pv=130, atk=65, defense=60, types=["Électrique"], niveau=10),
    
#-------------------------------------------------------------------------------------------------------------

    Pokemon(nom="Porygon", numero="137", pv=65, atk=60, defense=70, types=["Normal"], niveau=1),

    Pokemon(nom="Amonita", numero="138", pv=35, atk=40, defense=100, types=["Roche", "Eau"], niveau=1, evolution="Amonistar", evolution_niveau=10),
    Pokemon(nom="Amonistar", numero="139", pv=70, atk=60, defense=125, types=["Roche", "Eau"], niveau=10),

    Pokemon(nom="Kabuto", numero="140", pv=30, atk=80, defense=90, types=["Roche", "Eau"], niveau=1, evolution="Kabutops", evolution_niveau=10),
    Pokemon(nom="Kabutops", numero="141", pv=60, atk=115, defense=105, types=["Roche", "Eau"], niveau=10),

    Pokemon(nom="Ptéra", numero="142", pv=80, atk=105, defense=65, types=["Roche", "Vol"], niveau=1),

    Pokemon(nom="Ronflex", numero="143", pv=160, atk=110, defense=65, types=["Normal"], niveau=1),

# A MODIFIER EGALEMENT CAR POKEMON LEGENDAIRE

#--------------------------------------------------------------------------------------------------------

    Pokemon(nom="Artikodin", numero="144", pv=90, atk=85, defense=100, types=["Glace", "Vol"], niveau=1),


    Pokemon(nom="Électhor", numero="145", pv=90, atk=90, defense=85, types=["Électrique", "Vol"], niveau=1),


    Pokemon(nom="Sulfura", numero="146", pv=90, atk=100, defense=90, types=["Feu", "Vol"], niveau=1),

#--------------------------------------------------------------------------------------------------------
    Pokemon(nom="Minidraco", numero="147", pv=41, atk=64, defense=45, types=["Dragon"], niveau=1, evolution="Draco", evolution_niveau=10),
    Pokemon(nom="Draco", numero="148", pv=61, atk=84, defense=65, types=["Dragon"], niveau=10, evolution="Dracolosse", evolution_niveau=15),
    Pokemon(nom="Dracolosse", numero="149", pv=91, atk=134, defense=95, types=["Dragon", "Vol"], niveau=15),

    Pokemon(nom="Mewtwo", numero="150", pv=106, atk=110, defense=90, types=["Psy"], niveau=1),

    Pokemon(nom="Mew", numero="151", pv=100, atk=100, defense=100, types=["Psy"], niveau=1),
    
    Pokemon(nom="LORD-GENJOUX", numero="152", pv=1000, atk=1000, defense=1000, types=["Psy"], niveau=100),
]


pokedex_data = {"pokemons": []}
for pokemon in pokemon_liste:
        pokemon_data = {
            "nom": pokemon.nom,
            "numero": pokemon.numero,
            "pv": pokemon.pv,
            "atk": pokemon.atk,
            "defense": pokemon.defense,
            "types": pokemon.types,
            "niveau": pokemon.niveau,
            "evolution": pokemon.evolution,
            "evolution_niveau": pokemon.evolution_niveau
        }
        if not check_duplicate(pokedex_data, pokemon_data):
            pokedex_data["pokemons"].append(pokemon_data)
        else:
            print(f"Vous possédez déjà le Pokémon {pokemon_data['nom']} (n° {pokemon_data['numero']}).")

with open('pokedex.json', 'a') as file:
    json.dump(pokedex_data, file, indent=2)

pokedex_user = {"pokemons": []}
for _ in range(5):
    pokemon = pokemon_liste[randint(1, 151)]
    pokemon_data = {
        "nom": pokemon.nom,
        "numero": pokemon.numero,
        "pv": pokemon.pv,
        "atk": pokemon.atk,
        "defense": pokemon.defense,
        "types": pokemon.types,
        "niveau": pokemon.niveau,
        "evolution": pokemon.evolution,
        "evolution_niveau": pokemon.evolution_niveau
    }
    if not check_duplicate(pokedex_user, pokemon_data):
        pokedex_user["pokemons"].append(pokemon_data)
    else:
        print(f"Vous possédez déjà le Pokémon {pokemon_data['nom']} (n° {pokemon_data['numero']}).")
with open('pokedex_user.json', 'w') as f:
    json.dump(pokedex_user, f, indent= 2)


print("Le fichier JSON du Pokédex a été créé avec succès.")


