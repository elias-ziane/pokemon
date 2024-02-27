from pokemon import Pokemon
from pok import Pok


class Combat:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.p1 = pokemon1
        self.p2 = pokemon2
        self.__p1_pv = self.p1.pv
        self.__p2_pv = self.p2.pv
        self.__p1_atk = self.calculer_dommages(self.p1, self.p2)
        self.__p2_atk = self.calculer_dommages(self.p2, self.p1)

    def attaquer1(self):
        self.__p2_pv -= self.__p1_atk
        print(f"{self.p1.nom} attaque {self.p2.nom} et lui inflige {self.__p1_atk} points de dégâts.")

        if self.__p2_pv <= 0:
            print(f"{self.p2.nom} a été vaincu!")

    def attaquer2(self):
        self.__p1_pv -= self.__p2_atk
        print(f"{self.p2.nom} attaque {self.p1.nom} et lui inflige {self.__p2_atk} points de dégâts.")

        if self.__p1_pv <= 0:
            print(f"{self.p1.nom} a été vaincu!")

    def calculer_dommages(self, attaquant, defenseur):
        types_attaquant = attaquant.types
        types_defenseur = defenseur.types
        
        table_type = {
                'Normal':   {'Normal':1.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':0.5, 'Spectre':0,   'Dragon':1.0, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':1.0},
                'Plante':   {'Normal':1.0, 'Plante': 1.0, 'Feu': 0.5, 'Eau':2.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':0.5, 'Sol':2.0, 'Vol':0.5, 'Psy':1.0, 'Insecte':0.5, 'Roche':2.0, 'Spectre':1.0, 'Dragon':0.5, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':1.0},
                'Feu':      {'Normal':1.0, 'Plante': 2.0, 'Feu': 1.0, 'Eau':0.5, 'Electrique':1.0, 'Glace':2.0, 'Combat':1.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':2.0, 'Roche':0.5, 'Spectre':1.0, 'Dragon':0.5, 'Ténèbres':1.0, 'Acier':2.0, 'Fée':1.0},
                'Eau':      {'Normal':1.0, 'Plante': 0.5, 'Feu': 2.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':2.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':2.0, 'Spectre':1.0, 'Dragon':0.5, 'Ténèbres':1.0, 'Acier':1.0, 'Fée':1.0},
                'Eletrique':{'Normal':1.0, 'Plante': 0.5, 'Feu': 1.0, 'Eau':2.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':0,   'Vol':2.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':0.5, 'Ténèbres':1.0, 'Acier':1.0, 'Fée':1.0},
                'Glace':    {'Normal':1.0, 'Plante': 1.0, 'Feu': 0.5, 'Eau':0.5, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':2.0, 'Vol':2.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':2.0, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':1.0},
                'Combat':   {'Normal':2.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':2.0, 'Combat':1.0, 'Poison':0.5, 'Sol':1.0, 'Vol':0.5, 'Psy':0.5, 'Insecte':0.5, 'Roche':2.0, 'Spectre':0,   'Dragon':1.0, 'Ténèbres':2.0, 'Acier':2.0, 'Fée':0.5},
                'Poison':   {'Normal':1.0, 'Plante': 2.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':0.5, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':0.5, 'Spectre':0.5, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':0,   'Fée':2.0},
                'Sol':      {'Normal':1.0, 'Plante': 0.5, 'Feu': 2.0, 'Eau':1.0, 'Electrique':2.0, 'Glace':1.0, 'Combat':1.0, 'Poison':2.0, 'Sol':1.0, 'Vol':0,   'Psy':1.0, 'Insecte':0.5, 'Roche':2.0, 'Spectre':1.0, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':2.0, 'Fée':1.0},
                'Vol':      {'Normal':1.0, 'Plante': 2.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':0.5, 'Glace':1.0, 'Combat':2.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':2.0, 'Roche':0.5, 'Spectre':1.0, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':1.0},
                'Psy':      {'Normal':1.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':2.0, 'Sol':2.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':1.0, 'Ténèbres':0,   'Acier':0.5, 'Fée':1.0},
                'Insecte':  {'Normal':1.0, 'Plante': 2.0, 'Feu': 0.5, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':0.5, 'Poison':0.5, 'Sol':1.0, 'Vol':0.5, 'Psy':2.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':0.5, 'Dragon':1.0, 'Ténèbres':2.0, 'Acier':0.5, 'Fée':0.5},
                'Roche':    {'Normal':1.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':2.0, 'Combat':0.5, 'Poison':1.0, 'Sol':0.5, 'Vol':2.0, 'Psy':1.0, 'Insecte':2.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':1.0},
                "Spectre":  {'Normal':0,   'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':2.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':2.0, 'Dragon':1.0, 'Ténèbres':0.5, 'Acier':1.0, 'Fée':1.0},
                'Dragon':   {'Normal':1.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':2.0, 'Ténèbres':1.0, 'Acier':0.5, 'Fée':0},
                'Ténèbres': {'Normal':1.0, 'Plante': 1.0, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':1.0, 'Poison':0.5, 'Sol':1.0, 'Vol':1.0, 'Psy':2.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':2.0, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':1.0, 'Fée':0.5},
                'Acier':    {'Normal':1.0, 'Plante': 0.5, 'Feu': 0.5, 'Eau':1.0, 'Electrique':0.5, 'Glace':2.0, 'Combat':1.0, 'Poison':1.0, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':2.0, 'Spectre':1.0, 'Dragon':1.0, 'Ténèbres':1.0, 'Acier':1.0, 'Fée':2.0},
                'Fée':      {'Normal':1.0, 'Plante': 0.5, 'Feu': 1.0, 'Eau':1.0, 'Electrique':1.0, 'Glace':1.0, 'Combat':2.0, 'Poison':0.5, 'Sol':1.0, 'Vol':1.0, 'Psy':1.0, 'Insecte':1.0, 'Roche':1.0, 'Spectre':1.0, 'Dragon':2.0, 'Ténèbres':2.0, 'Acier':0.5, 'Fée':1.0}
            }

        # Vérifie que les types des Pokémon sont correctement définis
        if not types_attaquant or not types_defenseur:
            raise ValueError("Les types des Pokémon doivent être définis.")

        coefficients_attaque = []
        for type_attaquant in types_attaquant:
            for type_defenseur in types_defenseur:
                # Obtenez le multiplicateur de dommages à partir de la table des types
                multiplicateur = table_type[type_attaquant][type_defenseur]
                coefficients_attaque.append(multiplicateur)

        # Calcul de la moyenne des coefficients
        coefficient_moyen = sum(coefficients_attaque) / len(coefficients_attaque)

        # Calcul les dégâts en fonction de l'attaque, de la défense et du multiplicateur de type
        degats = int(attaquant.atk * coefficient_moyen) - defenseur.defense

        # Assure que les dégâts sont au moins égaux à 0
        degats = max(0, degats)

        return degats

    def get_pv(self):
        return self.__p1_pv, self.__p2_pv

if __name__ == "__main__":
    pok1 = Pok()
    pok2 = Pok()
    
    combat = Combat(pok1, pok2)
    
    print(f"{combat.p1.atk}  {combat.calculer_dommages(combat.p1, combat.p2)}")
    print(f"{combat.p2.atk}  {combat.calculer_dommages(combat.p2, combat.p1)}")
    print(f"{combat.attaquer1()}")
    print(f"{combat.attaquer2()}")
    print(f"{combat.get_pv()}")
