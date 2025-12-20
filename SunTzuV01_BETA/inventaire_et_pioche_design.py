import pygame
from design_class import Design
from typing import cast


class Inventaire(object):

    def __init__(self, list_inventory_cards: list[int]) -> None:
        # Liste des positions "X" (haut à gauche des cartes) en fonction du nombre de cartes dans l'inventaire, centrés.
        self.liste_positions_x_inventory: list[int] = []
        # Liste des positions "X" (haut à gauche des cartes) dans la zone deck de combat, centrés.
        self.liste_positions_x_combat: list[int] = []
        self.list_inventory_cards: list[int] = list_inventory_cards

        self.designclass = Design()
        self.designclass.charger_liste_all_cards_img()

        self.back_wallet_inventory_img = pygame.image.load(
            "ressources/inventaire_wallet_back.png"
        )
        self.front_wallet_inventory_img = pygame.image.load(
            "ressources/inventaire_wallet_front.png"
        )

    # Affiche sur "designclass.screen" les cartes de l'inventaire de manière centrée sur X
    #       -> Résultat = 'self.liste_position_x_inventory'
    def afficher_inventaire(self):

        # remise à zéro de la liste des positions centrées des cartes de l'inventaire selon leur nombre total
        self.liste_positions_x_inventory = []

        if len(self.list_inventory_cards) == 0:
            return

        # pour chaque carte du nombre de carte de l'inventaire :
        for i in range(0, len(self.list_inventory_cards), 1):

            # si il y plus de 0 carte dans l'inventaire :
            if len(self.list_inventory_cards) > 0:

                # PARTIE logique et calcul :

                position_x = (
                    (self.designclass.width_screen // (len(self.list_inventory_cards)))
                    * i
                    + (
                        self.designclass.width_screen
                        // (len(self.list_inventory_cards))
                        + 6
                    )
                    * 1
                    // 2
                    - 50
                )

                int(round(position_x, 0))

                # Ajout des positions x des 5 cartes dans la liste suivante :
                self.liste_positions_x_inventory.append(position_x)

                # Affichage
                # self.designclass.screen.blit(self.designclass.liste_all_cards_img[image_temporary],
                #                            (position_x, self.designclass.height_screen - 150))

    # Affiche sur "designclass.screen" les 5 cartes selectionnées pour combattre de manière centrée sur X
    #       -> Résultat = 'self.liste_position_x_combat'
    def afficher_emplacement_combat_bleu(self):

        # remise à zéro de la liste des positions centrées des cartes de combat
        self.liste_positions_x_combat = []

        # pour chacune des 5 cartes en zone de combat :
        for i in range(0, 5, 1):

            # Calcul de x pour centrer les 5 cartes en fonction de la taille de l'écran
            position_x = (
                ((self.designclass.width_screen // 5) - 95) * i
                + ((self.designclass.width_screen // 5) + 240) * 1 // 2
                - 50
            )
            int(round(position_x, 0))

            # Ajout des positions x des 5 cartes dans la liste suivante :
            self.liste_positions_x_combat.append(position_x)

            # Affichage
            self.designclass.screen.blit(
                cast(pygame.Surface, self.designclass.liste_all_cards_img[0]),
                (position_x, self.designclass.height_screen // 2),
            )

    def afficher_emplacement_combat_rouge(self):

        # remise à zéro de la liste des positions centrées des cartes de combat
        self.liste_positions_x_combat = []

        # pour chacune des 5 cartes en zone de combat :
        for i in range(0, 5, 1):

            # Calcul de x pour centrer les 5 cartes en fonction de la taille de l'écran
            position_x = (
                ((self.designclass.width_screen // 5) - 95) * i
                + ((self.designclass.width_screen // 5) + 240) * 1 // 2
                - 50
            )
            int(round(position_x, 0))

            # Ajout des positions x des 5 cartes dans la liste suivante :
            self.liste_positions_x_combat.append(position_x)

            # Affichage
            self.designclass.screen.blit(
                cast(pygame.Surface, self.designclass.liste_all_cards_img[20]),
                (position_x, self.designclass.height_screen // 2),
            )

    def start_inventaire(self, couleur: str = "BLEU"):

        j = 0
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        font2 = pygame.font.SysFont("broadway", 40, bold=False, italic=False)
        text = font2.render("- tour n°1 -", 1, (200, 200, 100))
        text2 = font2.render("(CARTES POUR COMBAT)", 1, (20, 100, 180) if couleur == "BLEU" else (180, 20, 20))
        
        message = f" :  Inventaire du joueur {'Bleu' if couleur == 'BLEU' else 'Rouge'}  : "
        text_color = (20, 100, 180) if couleur == "BLEU" else (180, 20, 20)
        text3 = font.render(message, 1, text_color)

        running = True

        while running:

            if j < 1:
                self.designclass.screen.fill((0, 0, 0))
                self.designclass.screen.blit(
                    self.back_wallet_inventory_img,
                    (0, self.designclass.height_screen - 160),
                )
                self.afficher_inventaire()
                self.designclass.screen.blit(
                    self.front_wallet_inventory_img,
                    (0, self.designclass.height_screen - 50),
                )
                
                if couleur == "BLEU":
                    self.afficher_emplacement_combat_bleu()
                else:
                    self.afficher_emplacement_combat_rouge()
                    
                self.designclass.screen.blit(
                    text, ((self.designclass.width_screen // 2) - 70, 20)
                )
                self.designclass.screen.blit(
                    text2, ((self.designclass.width_screen // 2) - 170, 280)
                )
                self.designclass.screen.blit(
                    text3, ((self.designclass.width_screen // 2) - 260, 400)
                )
                pygame.display.flip()
                j += 1

            for event in pygame.event.get():
                # vérifier que l'évènement est fermeture de fenêtre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("fermeture du jeu 好好")


"""
#inventory_player_b = Inventaire()
#inventory_player_b.start_inventaire()
"""
