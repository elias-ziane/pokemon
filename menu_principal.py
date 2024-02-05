import pygame
import sys
import matplotlib.pyplot as plt

CHEMIN_MP3 = "C:/Users/rachi/Desktop/Git/pokemon/music/generic.mp3"
CHEMIN_IMAGE_FOND = "C:/Users/rachi/Desktop/Git/pokemon/Image/img1.jpg"
CHEMIN_ICONE_NOUVELLE_PARTIE = "C:/Users/rachi/Desktop/Git/pokemon/Image/logo1.png"

Noir = "black"
Marron = "brown"
Orange = "orange"

class Menu:
    def __init__(self, longeur, largeur):
        pygame.init()
        self.longeur = longeur
        self.largeur = largeur
        self.fenetre = pygame.display.set_mode((longeur, largeur))
        pygame.mixer.init()
        pygame.mixer.music.load(CHEMIN_MP3)
        pygame.mixer.music.play()
        self.image_fond = pygame.image.load(CHEMIN_IMAGE_FOND)
        self.rect_fond = self.image_fond.get_rect()
        self.icone_nouvelle_partie = pygame.image.load(CHEMIN_ICONE_NOUVELLE_PARTIE)
        self.icone_rect = self.icone_nouvelle_partie.get_rect()
        self.y_icone = 100
        self.y_option = self.y_icone + self.icone_rect.height + 80  # Ajout de 10 pixels entre l'icône et l'option
        self.clignotement_actif = True
        self.temps_clignotement = 500  # Temps en millisecondes
        self.temps_dernier_clignotement = pygame.time.get_ticks()
        self.font = pygame.font.Font("C:/Users/rachi/Desktop/Git/pokemon/Polices/Sancreek.ttf", 48)  # Remplacez "chemin_vers_votre_police.ttf" par le chemin de votre police
        self.couleur_texte = (255, 255, 255)  # Couleur blanche
        self.couleur_rectangle = Orange # Couleur bleue
        self.options = ["NOUVELLE PARTIE", "CHARGER UNE PARTIE", "LE POKEDEX", "QUITTER LE PROGRAMME"]

    def afficher_menu(self):
        en_cours = True
        horloge = pygame.time.Clock()

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    en_cours = False

            self.fenetre.blit(self.image_fond, (0, 0))

            temps_actuel = pygame.time.get_ticks()

            # Vérifier si le clignotement doit être inversé
            if temps_actuel - self.temps_dernier_clignotement > self.temps_clignotement:
                self.clignotement_actif = not self.clignotement_actif
                self.temps_dernier_clignotement = temps_actuel

            if self.clignotement_actif:
                x_icone = self.longeur // 2 - self.icone_rect.width // 2
                y_icone = self.y_icone
                self.fenetre.blit(self.icone_nouvelle_partie, (x_icone, y_icone))

            # Afficher les options du menu
            for option in self.options:
                option_surface = self.font.render(option, True, self.couleur_texte)
                largeur_option, hauteur_option = option_surface.get_size()

                x_option = self.longeur // 2 - largeur_option // 2
                y_option = self.y_option + (self.options.index(option) * 90)  # Ajustez l'espacement entre les options

                # Ajustez la taille du rectangle en fonction de la largeur du texte
                pygame.draw.rect(self.fenetre, self.couleur_rectangle, (x_option - 8, y_option - 3, largeur_option + 10, hauteur_option + 2), 0)
                pygame.draw.rect(self.fenetre, (255, 255, 255), (x_option - 8, y_option - 3, largeur_option + 10, hauteur_option + 2), 2)

                self.fenetre.blit(option_surface, (x_option, y_option))
            pygame.display.flip()
            horloge.tick(60)

# Ajouter une fonction pour gérer le menu dans le fichier "menu.py"
def lancer_menu():
    menu_principal = Menu(996, 664)
    menu_principal.afficher_menu()