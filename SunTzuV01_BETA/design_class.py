import pygame
import random

#Class graphique, requiert 4 arguments : les listes de combat a et b, et les listes d'unitees a et b presentes sur les terrains

class Design(object):

    def __init__(self, liste_combat_a_bas=[0, 0, 0, 0, 0], liste_unite_terrain_a=[0, 0, 0, 0, 0],
                 liste_combat_b_haut=[0, 0, 0, 0, 0], liste_unite_terrain_b=[0, 0, 0, 0, 0], tour_de_jeu_deck_class=0,
                 listvalue1=[0, 0, 0], listvalue2=[0, 0, 0], listvalue3=[0, 0, 0], listvalue4=[0, 0, 0],
                 listvalue5=[0, 0, 0]):

        self.liste_combat_a = liste_combat_a_bas
        self.liste_combat_b = liste_combat_b_haut

        self.liste_unite_terrain_a = liste_unite_terrain_a
        self.liste_unite_terrain_b = liste_unite_terrain_b

        self.liste_all_cards_img = []
        self.liste_all_numbers_img = []

        self.liste_color_territories = [9, 9, 9, 9, 9]
        self.liste_size_territories = [99, 99, 99, 99, 99]

        self.var01 = True
        self.tour_de_jeu = tour_de_jeu_deck_class

        self.listvalue1 = listvalue1
        self.listvalue2 = listvalue2
        self.listvalue3 = listvalue3
        self.listvalue4 = listvalue4
        self.listvalue5 = listvalue5

        self.score_blue = int(0)
        self.score_red = int(0)

        self.listvalue1_img = pygame.image.load("ressources/pion_dragon_40x40.png")
        self.listvalue2_img = pygame.image.load("ressources/pion_dragon_40x40.png")
        self.listvalue3_img = pygame.image.load("ressources/pion_dragon_40x40.png")
        self.listvalue4_img = pygame.image.load("ressources/pion_dragon_40x40.png")
        self.listvalue5_img = pygame.image.load("ressources/pion_dragon_40x40.png")


        self.var_pos_unit = 0
        self.running = True

        self.width_screen = 1200
        self.height_screen = 700

        pygame.display.set_caption("FENETRE design_class SUN TZU")
        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen), pygame.FULLSCREEN)
        self.background_img = pygame.image.load('ressources/back_ground_550x300.png')

        # RESSOURCES GRAPHIQUES :

        # ZONE POINT VALUE :
        self.zone_point_123 = pygame.image.load("ressources/zone_point_123.png")
        self.zone_point_213 = pygame.image.load("ressources/zone_point_213.png")
        self.zone_point_312 = pygame.image.load("ressources/zone_point_312.png")
        self.zone_point_132 = pygame.image.load("ressources/zone_point_132.png")
        self.zone_point_231 = pygame.image.load("ressources/zone_point_231.png")
        self.zone_point_321 = pygame.image.load("ressources/zone_point_321.png")

        # PION TOUR DE JEU
        self.pion_dragon_32x32 = pygame.image.load("ressources/pion_dragon_40x40.png")

        # VIDE
        self.unit_number_empty_img = pygame.image.load('ressources/unit_number_vide.png')

        # BLEU
        self.blue_back_card_img = pygame.image.load('ressources/card_blue_back.png')
        self.blue_card_1_img = pygame.image.load(f'ressources/card_blue_1.png')
        self.blue_card_2_img = pygame.image.load(f'ressources/card_blue_2.png')
        self.blue_card_3_img = pygame.image.load(f'ressources/card_blue_3.png')
        self.blue_card_4_img = pygame.image.load(f'ressources/card_blue_4.png')
        self.blue_card_5_img = pygame.image.load(f'ressources/card_blue_5.png')
        self.blue_card_6_img = pygame.image.load(f'ressources/card_blue_6.png')
        self.blue_card_7_img = pygame.image.load(f'ressources/card_blue_7.png')
        self.blue_card_8_img = pygame.image.load(f'ressources/card_blue_8.png')
        self.blue_card_9_img = pygame.image.load(f'ressources/card_blue_9.png')
        self.blue_card_10_img = pygame.image.load(f'ressources/card_blue_10.png')
        self.blue_card_11_img = pygame.image.load(f'ressources/card_blue_11.png')
        self.blue_card_12_img = pygame.image.load(f'ressources/card_blue_12.png')
        self.blue_card_13_img = pygame.image.load(f'ressources/card_blue_13.png')
        self.blue_card_14_img = pygame.image.load(f'ressources/card_blue_14_peste.png')
        self.blue_card_15_img = pygame.image.load(f'ressources/card_blue_14_peste.png')

        self.blue_unit_number_0_img = pygame.image.load(f"ressources/unit_number_blue_14.png")
        self.blue_unit_number_1_img = pygame.image.load(f"ressources/unit_number_blue_1.png")
        self.blue_unit_number_2_img = pygame.image.load(f"ressources/unit_number_blue_2.png")
        self.blue_unit_number_3_img = pygame.image.load(f"ressources/unit_number_blue_3.png")
        self.blue_unit_number_4_img = pygame.image.load(f"ressources/unit_number_blue_4.png")
        self.blue_unit_number_5_img = pygame.image.load(f"ressources/unit_number_blue_5.png")
        self.blue_unit_number_6_img = pygame.image.load(f"ressources/unit_number_blue_6.png")
        self.blue_unit_number_7_img = pygame.image.load(f"ressources/unit_number_blue_7.png")
        self.blue_unit_number_8_img = pygame.image.load(f"ressources/unit_number_blue_8.png")
        self.blue_unit_number_9_img = pygame.image.load(f"ressources/unit_number_blue_9.png")
        self.blue_unit_number_10_img = pygame.image.load(f"ressources/unit_number_blue_10.png")
        self.blue_unit_number_11_img = pygame.image.load(f"ressources/unit_number_blue_11.png")
        self.blue_unit_number_12_img = pygame.image.load(f"ressources/unit_number_blue_12.png")
        self.blue_unit_number_13_img = pygame.image.load(f"ressources/unit_number_blue_13.png")

        # ROUGE
        self.red_back_card_img = pygame.image.load('ressources/card_red_back.png')
        self.red_card_1_img = pygame.image.load(f'ressources/card_red_1.png')
        self.red_card_2_img = pygame.image.load(f'ressources/card_red_2.png')
        self.red_card_3_img = pygame.image.load(f'ressources/card_red_3.png')
        self.red_card_4_img = pygame.image.load(f'ressources/card_red_4.png')
        self.red_card_5_img = pygame.image.load(f'ressources/card_red_5.png')
        self.red_card_6_img = pygame.image.load(f'ressources/card_red_6.png')
        self.red_card_7_img = pygame.image.load(f'ressources/card_red_7.png')
        self.red_card_8_img = pygame.image.load(f'ressources/card_red_8.png')
        self.red_card_9_img = pygame.image.load(f'ressources/card_red_9.png')
        self.red_card_10_img = pygame.image.load(f'ressources/card_red_10.png')
        self.red_card_11_img = pygame.image.load(f'ressources/card_red_11.png')
        self.red_card_12_img = pygame.image.load(f'ressources/card_red_12.png')
        self.red_card_13_img = pygame.image.load(f'ressources/card_red_13.png')
        self.red_card_14_img = pygame.image.load(f'ressources/card_red_14_peste.png')
        self.red_card_15_img = pygame.image.load(f'ressources/card_red_14_peste.png')

        self.red_unit_number_0_img = pygame.image.load(f"ressources/unit_number_red_14.png")
        self.red_unit_number_1_img = pygame.image.load(f"ressources/unit_number_red_1.png")
        self.red_unit_number_2_img = pygame.image.load(f"ressources/unit_number_red_2.png")
        self.red_unit_number_3_img = pygame.image.load(f"ressources/unit_number_red_3.png")
        self.red_unit_number_4_img = pygame.image.load(f"ressources/unit_number_red_4.png")
        self.red_unit_number_5_img = pygame.image.load(f"ressources/unit_number_red_5.png")
        self.red_unit_number_6_img = pygame.image.load(f"ressources/unit_number_red_6.png")
        self.red_unit_number_7_img = pygame.image.load(f"ressources/unit_number_red_7.png")
        self.red_unit_number_8_img = pygame.image.load(f"ressources/unit_number_red_8.png")
        self.red_unit_number_9_img = pygame.image.load(f"ressources/unit_number_red_9.png")
        self.red_unit_number_10_img = pygame.image.load(f"ressources/unit_number_red_10.png")
        self.red_unit_number_11_img = pygame.image.load(f"ressources/unit_number_red_11.png")
        self.red_unit_number_12_img = pygame.image.load(f"ressources/unit_number_red_12.png")
        self.red_unit_number_13_img = pygame.image.load(f"ressources/unit_number_red_13.png")

    # LISTE "liste_all_cards_img" comprenant toutes les images des cartes à jouer ( 0 à 15 Bleues, 20 à 35 Rouges ) :
    def charger_liste_all_cards_img(self):
        self.liste_all_cards_img.append(self.blue_back_card_img)
        self.liste_all_cards_img.append(self.blue_card_1_img)
        self.liste_all_cards_img.append(self.blue_card_2_img)
        self.liste_all_cards_img.append(self.blue_card_3_img)
        self.liste_all_cards_img.append(self.blue_card_4_img)
        self.liste_all_cards_img.append(self.blue_card_5_img)
        self.liste_all_cards_img.append(self.blue_card_6_img)
        self.liste_all_cards_img.append(self.blue_card_7_img)
        self.liste_all_cards_img.append(self.blue_card_8_img)
        self.liste_all_cards_img.append(self.blue_card_9_img)
        self.liste_all_cards_img.append(self.blue_card_10_img)
        self.liste_all_cards_img.append(self.blue_card_11_img)
        self.liste_all_cards_img.append(self.blue_card_12_img)
        self.liste_all_cards_img.append(self.blue_card_13_img)
        self.liste_all_cards_img.append(self.blue_card_14_img)
        self.liste_all_cards_img.append(self.blue_card_15_img)
        self.liste_all_cards_img.append(0)
        self.liste_all_cards_img.append(0)
        self.liste_all_cards_img.append(0)
        self.liste_all_cards_img.append(0)
        self.liste_all_cards_img.append(self.red_back_card_img)
        self.liste_all_cards_img.append(self.red_card_1_img)
        self.liste_all_cards_img.append(self.red_card_2_img)
        self.liste_all_cards_img.append(self.red_card_3_img)
        self.liste_all_cards_img.append(self.red_card_4_img)
        self.liste_all_cards_img.append(self.red_card_5_img)
        self.liste_all_cards_img.append(self.red_card_6_img)
        self.liste_all_cards_img.append(self.red_card_7_img)
        self.liste_all_cards_img.append(self.red_card_8_img)
        self.liste_all_cards_img.append(self.red_card_9_img)
        self.liste_all_cards_img.append(self.red_card_10_img)
        self.liste_all_cards_img.append(self.red_card_11_img)
        self.liste_all_cards_img.append(self.red_card_12_img)
        self.liste_all_cards_img.append(self.red_card_13_img)
        self.liste_all_cards_img.append(self.red_card_14_img)
        self.liste_all_cards_img.append(self.red_card_15_img)

    # LISTE "liste_all_number_img" comprenant toutes les images des résultats du nombres d'unités par territoire ( 0 à 13 Bleues, 20 à 33 Rouges ) :
    def charger_liste_all_numbers_img(self):

        self.liste_all_numbers_img.append(self.blue_unit_number_0_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_1_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_2_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_3_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_4_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_5_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_6_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_7_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_8_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_9_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_10_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_11_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_12_img)
        self.liste_all_numbers_img.append(self.blue_unit_number_13_img)
        self.liste_all_numbers_img.append(self.unit_number_empty_img)
        self.liste_all_numbers_img.append(0)
        self.liste_all_numbers_img.append(0)
        self.liste_all_numbers_img.append(0)
        self.liste_all_numbers_img.append(0)
        self.liste_all_numbers_img.append(0)
        self.liste_all_numbers_img.append(self.red_unit_number_0_img)
        self.liste_all_numbers_img.append(self.red_unit_number_1_img)
        self.liste_all_numbers_img.append(self.red_unit_number_2_img)
        self.liste_all_numbers_img.append(self.red_unit_number_3_img)
        self.liste_all_numbers_img.append(self.red_unit_number_4_img)
        self.liste_all_numbers_img.append(self.red_unit_number_5_img)
        self.liste_all_numbers_img.append(self.red_unit_number_6_img)
        self.liste_all_numbers_img.append(self.red_unit_number_7_img)
        self.liste_all_numbers_img.append(self.red_unit_number_8_img)
        self.liste_all_numbers_img.append(self.red_unit_number_9_img)
        self.liste_all_numbers_img.append(self.red_unit_number_10_img)
        self.liste_all_numbers_img.append(self.red_unit_number_11_img)
        self.liste_all_numbers_img.append(self.red_unit_number_12_img)
        self.liste_all_numbers_img.append(self.red_unit_number_13_img)

    # Fonction qui renvoie une liste (liste_size_territories) de 5 valeurs de type nombre, désignant le nombre d'unité présente sur les territoires.
    def analyse_number_unit_on_each_territories(self):
        for i in range(0, 5, 1):
            if self.liste_unite_terrain_a[i] > 0:
                self.liste_size_territories.pop(i)
                self.liste_size_territories.insert(i, self.liste_unite_terrain_a[i])
            elif self.liste_unite_terrain_b[i] > 0:
                self.liste_size_territories.pop(i)
                self.liste_size_territories.insert(i, self.liste_unite_terrain_b[i])
            else:
                self.liste_size_territories.pop(i)
                self.liste_size_territories.insert(i, 0)

    # Fonction qui renvoie une liste (liste_color_territories) de 5 valeurs de type string, désignant l'appartenance des territoires, soit "ROUGE" "BLEU" ou "VIDE" selon les unitées présentes.
    def analyse_color_unit_on_each_territories(self):
        for i in range(0, 5, 1):
            if self.liste_unite_terrain_b[i] > 0:
                self.liste_color_territories.pop(i)
                self.liste_color_territories.insert(i, "ROUGE")
            elif self.liste_unite_terrain_a[i] > 0:
                self.liste_color_territories.pop(i)
                self.liste_color_territories.insert(i, "BLEU")
            else:
                self.liste_color_territories.pop(i)
                self.liste_color_territories.insert(i, "VIDE")

    # Fonction qui affiche les troupes sur le plateau selon leur nombre et leur couleur en fonction du paramètre (position) qui doit être rempli comme cela (x,y)
    def position_unit_on_map(self, position):
        if self.liste_color_territories[self.var_pos_unit] == "BLEU":
            if self.liste_size_territories[self.var_pos_unit] < 14:
                self.screen.blit(self.liste_all_numbers_img[self.liste_size_territories[self.var_pos_unit]], position)
            if self.liste_size_territories[self.var_pos_unit] >= 14:
                self.screen.blit(self.liste_all_numbers_img[0], position)

        if self.liste_color_territories[self.var_pos_unit] == "ROUGE":

            if self.liste_size_territories[self.var_pos_unit] < 14:
                self.screen.blit(self.liste_all_numbers_img[self.liste_size_territories[self.var_pos_unit] + 20],
                                 position)
            if self.liste_size_territories[self.var_pos_unit] >= 14:
                self.screen.blit(self.liste_all_numbers_img[20], position)

        if self.liste_color_territories[self.var_pos_unit] == "VIDE":
            self.screen.blit(self.liste_all_numbers_img[14], position)

    # Fonction qui permet d'identifier les images des cartes terrains suivant le tirage dans zoneplay_values_class
    def selection_imgcardterrainvalue(self):
        if self.listvalue1 == [1, 2, 3]:
            self.listvalue1_img = self.zone_point_123
        elif self.listvalue1 == [1, 3, 2]:
            self.listvalue1_img = self.zone_point_132
        elif self.listvalue1 == [2, 1, 3]:
            self.listvalue1_img = self.zone_point_213
        elif self.listvalue1 == [2, 3, 1]:
            self.listvalue1_img = self.zone_point_231
        elif self.listvalue1 == [3, 2, 1]:
            self.listvalue1_img = self.zone_point_321
        elif self.listvalue1 == [3, 1, 2]:
            self.listvalue1_img = self.zone_point_312

        if self.listvalue2 == [1, 2, 3]:
            self.listvalue2_img = self.zone_point_123
        elif self.listvalue2 == [1, 3, 2]:
            self.listvalue2_img = self.zone_point_132
        elif self.listvalue2 == [2, 1, 3]:
            self.listvalue2_img = self.zone_point_213
        elif self.listvalue2 == [2, 3, 1]:
            self.listvalue2_img = self.zone_point_231
        elif self.listvalue2 == [3, 2, 1]:
            self.listvalue2_img = self.zone_point_321
        elif self.listvalue2 == [3, 1, 2]:
            self.listvalue2_img = self.zone_point_312

        if self.listvalue3 == [1, 2, 3]:
            self.listvalue3_img = self.zone_point_123
        elif self.listvalue3 == [1, 3, 2]:
            self.listvalue3_img = self.zone_point_132
        elif self.listvalue3 == [2, 1, 3]:
            self.listvalue3_img = self.zone_point_213
        elif self.listvalue3 == [2, 3, 1]:
            self.listvalue3_img = self.zone_point_231
        elif self.listvalue3 == [3, 2, 1]:
            self.listvalue3_img = self.zone_point_321
        elif self.listvalue3 == [3, 1, 2]:
            self.listvalue3_img = self.zone_point_312

        if self.listvalue4 == [1, 2, 3]:
            self.listvalue4_img = self.zone_point_123
        elif self.listvalue4 == [1, 3, 2]:
            self.listvalue4_img = self.zone_point_132
        elif self.listvalue4 == [2, 1, 3]:
            self.listvalue4_img = self.zone_point_213
        elif self.listvalue4 == [2, 3, 1]:
            self.listvalue4_img = self.zone_point_231
        elif self.listvalue4 == [3, 2, 1]:
            self.listvalue4_img = self.zone_point_321
        elif self.listvalue4 == [3, 1, 2]:
            self.listvalue4_img = self.zone_point_312

        if self.listvalue5 == [1, 2, 3]:
            self.listvalue5_img = self.zone_point_123
        elif self.listvalue5 == [1, 3, 2]:
            self.listvalue5_img = self.zone_point_132
        elif self.listvalue5 == [2, 1, 3]:
            self.listvalue5_img = self.zone_point_213
        elif self.listvalue5 == [2, 3, 1]:
            self.listvalue5_img = self.zone_point_231
        elif self.listvalue5 == [3, 2, 1]:
            self.listvalue5_img = self.zone_point_321
        elif self.listvalue5 == [3, 1, 2]:
            self.listvalue5_img = self.zone_point_312

    def update_design(self, score_blue, score_red,
                      liste_combat_a_bas, liste_unite_terrain_a,
                      liste_combat_b_haut, liste_unite_terrain_b, tour_de_jeu_deck_class,
                      listvalue1, listvalue2, listvalue3, listvalue4,
                      listvalue5):

        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen), pygame.FULLSCREEN)
        self.background_img = pygame.image.load('ressources/back_ground_550x300.png')

        self.score_blue = score_blue
        self.score_red = score_red

        self.liste_combat_a = liste_combat_a_bas
        self.liste_combat_b = liste_combat_b_haut

        self.liste_unite_terrain_a = liste_unite_terrain_a
        self.liste_unite_terrain_b = liste_unite_terrain_b

        self.tour_de_jeu = tour_de_jeu_deck_class

        self.listvalue1 = listvalue1
        self.listvalue2 = listvalue2
        self.listvalue3 = listvalue3
        self.listvalue4 = listvalue4
        self.listvalue5 = listvalue5

    def quitter(self):
        self.running = False

    def start_design(self):
        self.charger_liste_all_cards_img()
        self.charger_liste_all_numbers_img()
        self.analyse_color_unit_on_each_territories()
        self.analyse_number_unit_on_each_territories()

        black = (0, 0, 0)
        blue = (0, 0, 180)
        red = (255, 0, 0)
        white = (255, 255, 255)
        font_score = pygame.font.Font("freesansbold.ttf", 32)
        font_continue = pygame.font.Font("freesansbold.ttf", 26)
        text_surface_score_blue = font_score.render(f'SCORE BLEU : {self.score_blue}', True, black, blue)
        text_surface_score_red = font_score.render(f'SCORE ROUGE : {self.score_red}', True, black, red)
        text_surface_continue = font_continue.render('APPUYEZ SUR ESPACE POUR CONTINUER', True, white, black)
        self.screen.blit(text_surface_score_blue, (20, self.height_screen - 100))
        self.screen.blit(text_surface_score_red, (10, 100))
        # Centrer le message en bas de l'ecran
        text_rect = text_surface_continue.get_rect(center=(self.width_screen // 2 + 20, self.height_screen - 10))
        self.screen.blit(text_surface_continue, text_rect)

        print(f"liste_color_territories{self.liste_color_territories}")
        print(f"liste_size_territories{self.liste_size_territories}")

        while self.running:

            self.screen.blit(self.background_img, (self.width_screen // 2 - 265, self.height_screen // 2 - 140))

            j = 0
            # en HAUT du plateau, positionne cartes attaques du joueur B, ROUGE
            for i in self.liste_combat_b:
                self.screen.blit(self.liste_all_cards_img[20 + i],
                                 (self.width_screen // 2 - 260 + 110 * j, self.height_screen // 2 - 295))
                j += 1
            j = 0
            # en bas du plateau, positionne cartes attaques du joueur A, BLEU
            for i in self.liste_combat_a:
                self.screen.blit(self.liste_all_cards_img[i],
                                 (self.width_screen // 2 - 260 + 110 * j, self.height_screen // 2 + 160))
                j += 1
            j = 0

            # Position des unités sur les terrains (1 à 5) :
            if self.var_pos_unit < 4:
                # Terrain 1 : "XINJIANG"
                self.position_unit_on_map((self.width_screen // 2 - 90, self.height_screen // 2 - 70))
                self.var_pos_unit += 1

                # Terrain 1 : "TIBET"
                self.position_unit_on_map((self.width_screen // 2 - 105, self.height_screen // 2 + 5))
                self.var_pos_unit += 1

                # Terrain 1 : "QINGHAI"
                self.position_unit_on_map((self.width_screen // 2 + 100, self.height_screen // 2 + 30))
                self.var_pos_unit += 1

                # Terrain 1 : "MONGOLIA"
                self.position_unit_on_map((self.width_screen // 2 + 80, self.height_screen // 2 - 110))
                self.var_pos_unit += 1

                # Terrain 1 : "MANDARIN"
                self.position_unit_on_map((self.width_screen // 2 + 100, self.height_screen // 2 - 50))
                self.var_pos_unit += 1
                pygame.display.flip()

            for event in pygame.event.get():

                if self.var01:
                    self.screen.blit(self.pion_dragon_32x32,
                                     (int(self.width_screen // 2 + 225),
                                      195 + 28 * self.tour_de_jeu))

                    # affiche carte zone value XINJIANG :
                    self.screen.blit(self.listvalue1_img,
                                     (int(self.width_screen / 2 - 370),
                                      265))
                    # affiche carte zone value TIBET :
                    self.screen.blit(self.listvalue2_img,
                                     (int(self.width_screen / 2 - 370),
                                      380))
                    # affiche carte zone value QINGHAI :
                    self.screen.blit(self.listvalue3_img,
                                     (int(self.width_screen / 2 + 290),
                                      420))
                    # affiche carte zone value MONGOLIA :
                    self.screen.blit(self.listvalue4_img,
                                     (int(self.width_screen / 2 + 290),
                                      220))
                    # affiche carte zone value MANDARIN :
                    self.screen.blit(self.listvalue5_img,
                                     (int(self.width_screen / 2 + 290),
                                      320))

                    pygame.display.flip()
                    self.var01 = False

                # vérifier que l'évènement est fermeture de fenêtre
                if event.type == pygame.QUIT:
                    self.quitter()
                    pygame.quit()
                    print("fermeture du jeu 好好")

                if event.type == pygame.KEYDOWN:
                    # détecter si la touche espace est pressée
                    if event.key == pygame.K_SPACE:
                        print("ESPACE PRESSE")
                        self.quitter()
                        break

                    if event.key == pygame.K_ESCAPE:
                        print("fermeture du jeu avec key_ESCAPE 好好")
                        pygame.quit()

    def afficher_ecran_victoire(self, gagnant, score_blue, score_red):
        """Affiche un ecran de victoire graphique avec le gagnant et les scores finaux"""
        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen), pygame.FULLSCREEN)

        running_victory = True

        while running_victory:
            if gagnant == "BLEU":
                background_color = (20, 50, 150)
                winner_color = (100, 150, 255)
                text_color = (255, 255, 255)
            elif gagnant == "ROUGE":
                background_color = (150, 20, 20)
                winner_color = (255, 100, 100)
                text_color = (255, 255, 255)
            else:
                background_color = (80, 80, 80)
                winner_color = (150, 150, 150)
                text_color = (255, 255, 255)

            self.screen.fill(background_color)

            font_title = pygame.font.Font("freesansbold.ttf", 100)
            font_winner = pygame.font.Font("freesansbold.ttf", 80)
            font_score = pygame.font.Font("freesansbold.ttf", 50)
            font_instruction = pygame.font.Font("freesansbold.ttf", 30)

            if gagnant == "NUL":
                text_title = font_title.render("MATCH NUL", True, text_color)
                title_rect = text_title.get_rect(center=(self.width_screen // 2, self.height_screen // 2 - 200))
                printprint(f"FIN DU JEU : MATCH NUL")
            else:
                text_title = font_title.render("VICTOIRE !", True, text_color)
                title_rect = text_title.get_rect(center=(self.width_screen // 2, self.height_screen // 2 - 200))

                text_winner = font_winner.render(f"LES {gagnant}S", True, winner_color)
                winner_rect = text_winner.get_rect(center=(self.width_screen // 2, self.height_screen // 2 - 80))
                self.screen.blit(text_winner, winner_rect)
                printprint(f"FIN DU JEU : VICTOIRE {gagnant}")

            self.screen.blit(text_title, title_rect)

            text_score_blue = font_score.render(f"Score Bleu : {score_blue}", True, (100, 150, 255))
            score_blue_rect = text_score_blue.get_rect(center=(self.width_screen // 2, self.height_screen // 2 + 50))
            self.screen.blit(text_score_blue, score_blue_rect)

            text_score_red = font_score.render(f"Score Rouge : {score_red}", True, (255, 100, 100))
            score_red_rect = text_score_red.get_rect(center=(self.width_screen // 2, self.height_screen // 2 + 120))
            self.screen.blit(text_score_red, score_red_rect)

            text_instruction = font_instruction.render("Appuyez sur ESPACE pour continuer ou ESC pour quitter", True, text_color)
            instruction_rect = text_instruction.get_rect(center=(self.width_screen // 2, self.height_screen - 100))
            self.screen.blit(text_instruction, instruction_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_victory = False
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running_victory = False
                        return

                    if event.key == pygame.K_ESCAPE:
                        running_victory = False
                        pygame.quit()
                        return





