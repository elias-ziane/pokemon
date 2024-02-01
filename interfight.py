import pygame
import sys
import os
import random

# Désactiver le mixer audio de Pygame
os.environ["SDL_AUDIODRIVER"] = "dummy"

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
largeur, hauteur = 1200, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pokemon Combat")

# Couleurs
GRIS = (192, 192, 192)  # Beau gris
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)  # Couleur verte

# Chargement des images de fond
chemin_fonds = "/home/mathis/github/pokemon/imageback"  # Remplace ça par le chemin réel vers ton dossier d'images de fond
fonds = []
for fichier in os.listdir(chemin_fonds):
    chemin_complet = os.path.join(chemin_fonds, fichier)
    if fichier.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = pygame.image.load(chemin_complet)
        fonds.append(pygame.transform.scale(img, (950, 600)))

fond_combat = random.choice(fonds)

# Charger la musique
chemin_musique = "/home/mathis/github/pokemon/music-comb/musiccombat.mp3"  # Remplace ça par le chemin réel de ta musique
pygame.mixer.music.load(chemin_musique)

# Chargez les images des Pokémon et redimensionnez-les
pokemon1_image = pygame.image.load("pokemon1.png")
pokemon2_image = pygame.image.load("pokemon2.png")

# Redimensionnez les images des Pokémon selon la taille souhaitée
taille_pokemon = (200, 200)  # Remplacez par la taille désirée
pokemon1_image = pygame.transform.scale(pokemon1_image, taille_pokemon)
pokemon2_image = pygame.transform.scale(pokemon2_image, taille_pokemon)

# Position initiale des Pokémon
pokemon1_position = (150, 380)
pokemon2_position = (600, 180)

# Barre de vie
barre_vie_largeur = 150
barre_vie_hauteur = 20

barre_vie_rect1 = pygame.Rect(pokemon1_position[0] + 20, pokemon1_position[1] - barre_vie_hauteur, barre_vie_largeur, barre_vie_hauteur)
barre_vie_rect2 = pygame.Rect(pokemon2_position[0] + 50, pokemon2_position[1] - barre_vie_hauteur, barre_vie_largeur, barre_vie_hauteur)

vie_pokemon1 = 100  # Exemple de la vie du premier Pokémon (modifiable selon le besoin)
vie_pokemon2 = 100  # Exemple de la vie du deuxième Pokémon (modifiable selon le besoin)

# Bouton "Attaquer"
bouton_attaquer_rect = pygame.Rect(20, hauteur - 70, 200, 50)  # J'ai augmenté la largeur du bouton
cadre_bouton = pygame.Rect(bouton_attaquer_rect.x - 5, bouton_attaquer_rect.y - 5, bouton_attaquer_rect.width + 10, bouton_attaquer_rect.height + 10)
couleur_bouton = VERT  # Couleur du bouton (verte)
couleur_cadre = NOIR  # Couleur du cadre (noir)
font = pygame.font.Font(None, 36)  # Police par défaut de pygame

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                # Vérifier si le clic est à l'intérieur du bouton "Attaquer"
                if bouton_attaquer_rect.collidepoint(event.pos):
                    print("Attaquer!")

    # Lancer la musique en boucle (-1 indique une lecture en boucle)
    pygame.mixer.music.play(-1)

    # Dessiner l'arrière-plan
    fenetre.fill(GRIS)
    fenetre.blit(fond_combat, (0, 0))  # Affiche le fond d'écran en premier

    # Dessiner les Pokémon
    fenetre.blit(pokemon1_image, pokemon1_position)
    fenetre.blit(pokemon2_image, pokemon2_position)

    # Dessiner les barres de vie vertes
    pygame.draw.rect(fenetre, VERT, barre_vie_rect1)
    pygame.draw.rect(fenetre, VERT, barre_vie_rect2)

    # Dessiner le cadre du bouton "Attaquer"
    pygame.draw.rect(fenetre, couleur_cadre, cadre_bouton)
    # Dessiner le bouton "Attaquer"
    pygame.draw.rect(fenetre, couleur_bouton, bouton_attaquer_rect)
    texte_attaquer = font.render("Attaquer", True, NOIR)
    fenetre.blit(texte_attaquer, (bouton_attaquer_rect.x + 50, bouton_attaquer_rect.y + 10))

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôle de la vitesse de la boucle
    pygame.time.Clock().tick(60)
