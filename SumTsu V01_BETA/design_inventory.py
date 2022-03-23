import pygame
from design_class import Design
from deck_class import Deck
from inventaire_et_pioche_design import Inventaire
from zoneplay_values_class import Zoneplay

"""
pygame.mouse.get_pos() # donne la position (x, y)

pygame.mouse.get_pressed

sprites_clicked = [sprite for sprite in toute_ma_liste_de_sprites if sprite.rect.collidepoint(x, y)]

"""


class BoutonCardInventory(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, image_path, value, id):
        super(BoutonCardInventory, self).__init__()
        self.image = image_path
        self.rect_x = coord_x
        self.rect_y = coord_y
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

        self.id = id
        self.value = value

        self.clicked = False
        self.linkReady = False
        self.links = []

    def afficher_carte_bouton(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

    def detruire_selection_rect(self):
        self.rect = self.image.get_rect(topleft=(-200, -200))


class BoutonOKandUndo(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, image_path, value, id):
        super(BoutonOKandUndo, self).__init__()
        self.image = image_path
        self.rect_x = coord_x
        self.rect_y = coord_y
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

        self.id = id
        self.value = value

        self.clicked = False
        self.linkReady = False
        self.links = []

    def afficher_ok_undo_bouton(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))


class DesignInventoryBlue:

    def __init__(self, tour_de_jeu_deck_class=0, list_inventory_cards=[], listvalue1_img=0,
                 listvalue2_img=0, listvalue3_img=0, listvalue4_img=0, listvalue5_img=0,
                 liste_unite_terrain_a=[0, 0, 0, 0, 0], liste_unite_terrain_b=[0, 0, 0, 0, 0],
                 liste_all_numbers_img=[]):
        pygame.init()

        self.liste_combat_temp = [0, 0, 0, 0, 0]
        self.list_combat_validee = [0, 0, 0, 0, 0]

        self.listvalue1_img = listvalue1_img
        self.listvalue2_img = listvalue2_img
        self.listvalue3_img = listvalue3_img
        self.listvalue4_img = listvalue4_img
        self.listvalue5_img = listvalue5_img

        self.list_inventory_cards = list_inventory_cards

        self.liste_unite_terrain_a = liste_unite_terrain_a
        self.liste_unite_terrain_b = liste_unite_terrain_b
        self.liste_size_territories = [0, 0, 0, 0, 0]
        self.liste_color_territories = ["VIDE", "VIDE", "VIDE", "VIDE", "VIDE"]
        self.var_pos_unit = 0
        self.liste_all_numbers_img = liste_all_numbers_img

        self.design_class = Design()
        self.inventaire_et_pioche_design = Inventaire(self.list_inventory_cards)

        self.tour_de_jeu = tour_de_jeu_deck_class

        self.var01 = True
        self.statut = True

        self.width_screen = 1200
        self.height_screen = 700

        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen), pygame.FULLSCREEN)

        self.bouton_card_liste = pygame.sprite.Group()
        self.bouton_ok_undo = pygame.sprite.Group()

        self.ok_button_img = pygame.image.load("ressources/OK.png")
        self.undo_button_img = pygame.image.load("ressources/Undo.png")
        self.back_wallet_inventory_img = pygame.image.load("ressources/inventaire_wallet_back.png")
        self.front_wallet_inventory_img = pygame.image.load("ressources/inventaire_wallet_front.png")
        self.map_img = pygame.image.load("ressources/back_ground_700x330.png")

    def quitter(self):
        self.statut = False

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
    def position_unit_on_map(self, position, var_pos_unit):
        if self.liste_color_territories[var_pos_unit] == "BLEU":
            if self.liste_size_territories[var_pos_unit] < 14:
                self.screen.blit(self.liste_all_numbers_img[self.liste_size_territories[var_pos_unit]],
                                 position)
            if self.liste_size_territories[var_pos_unit] >= 14:
                self.screen.blit(self.liste_all_numbers_img[0], position)

        if self.liste_color_territories[var_pos_unit] == "ROUGE":

            if self.liste_size_territories[var_pos_unit] < 14:
                self.screen.blit(self.liste_all_numbers_img[self.liste_size_territories[var_pos_unit] + 20],
                                 position)
            if self.liste_size_territories[var_pos_unit] >= 14:
                self.screen.blit(self.liste_all_numbers_img[20], position)

        if self.liste_color_territories[var_pos_unit] == "VIDE":
            self.screen.blit(self.liste_all_numbers_img[14], position)

    def add_bouton_card(self):

        self.design_class.charger_liste_all_cards_img()

        self.inventaire_et_pioche_design.afficher_inventaire()
        self.inventaire_et_pioche_design.afficher_emplacement_combat_bleu()

        self.screen.blit(self.back_wallet_inventory_img,
                                      (0, self.height_screen - 160))

        for i in range(0, len(self.inventaire_et_pioche_design.list_inventory_cards), 1):
            self.bouton_card_liste.add(BoutonCardInventory(
                coord_x=self.inventaire_et_pioche_design.liste_positions_x_inventory[i],
                coord_y=self.height_screen - 150,
                image_path=self.design_class.liste_all_cards_img[
                    self.inventaire_et_pioche_design.list_inventory_cards[i]],
                value=self.inventaire_et_pioche_design.list_inventory_cards[i],
                id=len(self.bouton_card_liste) + 1))

            self.screen.blit(self.back_wallet_inventory_img,
                                          (0, self.height_screen - 160))

        self.bouton_ok_undo.add(BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 350,
            image_path=self.ok_button_img,
            value="OK",
            id=len(self.bouton_ok_undo) + 1))

        self.bouton_ok_undo.add(BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 270,
            image_path=self.undo_button_img,
            value="UNDO",
            id=len(self.bouton_ok_undo) + 1))

        for card in self.bouton_card_liste:
            card.afficher_carte_bouton(screen=self.screen)

        for button in self.bouton_ok_undo:
            button.afficher_ok_undo_bouton(screen=self.screen)

        self.screen.blit(self.front_wallet_inventory_img,
                                      (0, self.height_screen - 50))

    def en_cours_execution(self):
        events = pygame.event.get()

        for event in events:

            # affichage carte du jeu, pion du tour, cartes des valeurs des territoires, execute add_bouton_card
            if self.var01:
                self.screen.blit(self.map_img, (int(self.width_screen * 0.15), 0))

                self.screen.blit(self.design_class.pion_dragon_32x32,
                                              (int(self.width_screen / 2 + 211),
                                               33 * self.tour_de_jeu))
                
                # affiche carte zone value XINJIANG :
                self.screen.blit(self.listvalue1_img,
                                              (int(self.width_screen / 2 - 540),
                                               35))
                # affiche carte zone value TIBET :
                self.screen.blit(self.listvalue2_img,
                                              (int(self.width_screen / 2 - 540),
                                               185))
                # affiche carte zone value QINGHAI :
                self.screen.blit(self.listvalue3_img,
                                              (int(self.width_screen / 2 + 300),
                                               205))
                # affiche carte zone value MONGOLIA :
                self.screen.blit(self.listvalue4_img,
                                              (int(self.width_screen / 2 + 300),
                                               5))
                # affiche carte zone value MANDARIN :
                self.screen.blit(self.listvalue5_img,
                                              (int(self.width_screen / 2 + 300),
                                               105))

                self.add_bouton_card()
                self.var01 = False

            if event.type == pygame.QUIT:
                self.quitter()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quitter()
                    pygame.quit()

            # Si on clique avec un bouton de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                # position x , y souris
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                # bouton milieu souris
                if event.button == 2:
                    pass

                # bouton gauche souris
                elif event.button == 1:
                    for key in self.bouton_card_liste:
                        # si la position x , y du sprite entre en colision avec position (pos) <=> souris
                        if key.rect.collidepoint(pos):
                            for i in range(0, len(self.liste_combat_temp), 1):
                                if self.liste_combat_temp[i] == 0:
                                    self.liste_combat_temp[i] = key.value
                                    key.rect_x = (self.inventaire_et_pioche_design.liste_positions_x_combat[i])
                                    key.rect_y = self.height_screen // 2
                                    key.afficher_carte_bouton(screen=self.screen)
                                    self.screen.blit(self.design_class.liste_all_cards_img[0],
                                                                  (
                                                                      self.inventaire_et_pioche_design.liste_positions_x_inventory[
                                                                          key.id - 1],
                                                                      self.height_screen - 150))

                                    key.detruire_selection_rect()
                                    print(self.liste_combat_temp)
                                    break

                    for key in self.bouton_ok_undo:
                        if key.rect.collidepoint(pos):
                            if key.value == "OK":
                                for i in range(0, 5, 1):
                                    if self.liste_combat_temp.count(0) == 0:
                                        self.list_combat_validee = self.liste_combat_temp
                                        print(f"list_combat_validee : {self.list_combat_validee}")
                                        self.statut = False
                                        break
                                    else:
                                        print(f"list_combat_validee : {self.list_combat_validee}")
                                        break

                            if key.value == "UNDO":
                                for i in range(0, 5, 1):
                                    self.screen.blit(self.design_class.liste_all_cards_img[0],
                                                                  (
                                                                      self.inventaire_et_pioche_design.liste_positions_x_combat[
                                                                          i],
                                                                      self.height_screen // 2))
                                self.bouton_card_liste.empty()
                                self.bouton_ok_undo.empty()

                                self.add_bouton_card()

                                self.liste_combat_temp = [0, 0, 0, 0, 0]
                                break

                    pygame.display.flip()

                # bouton droit souris
                elif event.button == 2:
                    for key in self.bouton_card_liste:
                        if key.rect.collidepoint(pos):
                            break

        pygame.display.flip()


class DesignInventoryRed:

    def __init__(self, tour_de_jeu_deck_class=0, list_inventory_cards=[], listvalue1_img=0,
                 listvalue2_img=0, listvalue3_img=0, listvalue4_img=0, listvalue5_img=0):
        pygame.init()

        self.liste_combat_temp = [0, 0, 0, 0, 0]
        self.list_combat_validee = [0, 0, 0, 0, 0]

        self.listvalue1_img = listvalue1_img
        self.listvalue2_img = listvalue2_img
        self.listvalue3_img = listvalue3_img
        self.listvalue4_img = listvalue4_img
        self.listvalue5_img = listvalue5_img

        self.list_inventory_cards_red = list_inventory_cards

        self.design_class = Design()
        self.inventaire_et_pioche_design = Inventaire(self.list_inventory_cards_red)

        self.tour_de_jeu = tour_de_jeu_deck_class

        self.var01 = True
        self.statut = True

        self.width_screen = 1200
        self.height_screen = 700

        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen), pygame.FULLSCREEN)

        self.bouton_card_liste = pygame.sprite.Group()
        self.bouton_ok_undo = pygame.sprite.Group()

        self.ok_button_img = pygame.image.load("ressources/OK.png")
        self.undo_button_img = pygame.image.load("ressources/Undo.png")
        self.back_wallet_inventory_img = pygame.image.load("ressources/inventaire_wallet_back.png")
        self.front_wallet_inventory_img = pygame.image.load("ressources/inventaire_wallet_front.png")
        self.map_img = pygame.image.load("ressources/back_ground_700x330.png")

    def quitter(self):
        self.statut = False

    def add_bouton_card(self):

        self.design_class.charger_liste_all_cards_img()

        self.inventaire_et_pioche_design.afficher_inventaire()
        self.inventaire_et_pioche_design.afficher_emplacement_combat_rouge()

        self.screen.blit(self.back_wallet_inventory_img,
                         (0, self.height_screen - 160))

        for i in range(0, len(self.inventaire_et_pioche_design.list_inventory_cards), 1):
            self.bouton_card_liste.add(BoutonCardInventory(
                coord_x=self.inventaire_et_pioche_design.liste_positions_x_inventory[i],
                coord_y=self.height_screen - 150,
                image_path=self.design_class.liste_all_cards_img[
                    self.inventaire_et_pioche_design.list_inventory_cards[i] + 20],
                value=self.inventaire_et_pioche_design.list_inventory_cards[i],
                id=len(self.bouton_card_liste) + 1))

            self.screen.blit(self.back_wallet_inventory_img,
                             (0, self.height_screen - 160))

        self.bouton_ok_undo.add(BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 350,
            image_path=self.ok_button_img,
            value="OK",
            id=len(self.bouton_ok_undo) + 1))

        self.bouton_ok_undo.add(BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 270,
            image_path=self.undo_button_img,
            value="UNDO",
            id=len(self.bouton_ok_undo) + 1))

        for card in self.bouton_card_liste:
            card.afficher_carte_bouton(screen=self.screen)

        for button in self.bouton_ok_undo:
            button.afficher_ok_undo_bouton(screen=self.screen)

        self.screen.blit(self.front_wallet_inventory_img,
                         (0, self.height_screen - 50))

    def en_cours_execution(self):
        events = pygame.event.get()

        for event in events:

            # affichage carte du jeu, pion du tour, cartes des valeurs des territoires, execute add_bouton_card
            if self.var01:
                self.screen.blit(self.map_img, (int(self.width_screen * 0.15), 0))

                self.screen.blit(self.design_class.pion_dragon_32x32,
                                 (int(self.width_screen / 2 + 211),
                                  33 * self.tour_de_jeu))

                # affiche carte zone value XINJIANG :
                self.screen.blit(self.listvalue1_img,
                                 (int(self.width_screen / 2 - 540),
                                  35))
                # affiche carte zone value TIBET :
                self.screen.blit(self.listvalue2_img,
                                 (int(self.width_screen / 2 - 540),
                                  185))
                # affiche carte zone value QINGHAI :
                self.screen.blit(self.listvalue3_img,
                                 (int(self.width_screen / 2 + 300),
                                  205))
                # affiche carte zone value MONGOLIA :
                self.screen.blit(self.listvalue4_img,
                                 (int(self.width_screen / 2 + 300),
                                  5))
                # affiche carte zone value MANDARIN :
                self.screen.blit(self.listvalue5_img,
                                 (int(self.width_screen / 2 + 300),
                                  105))

                self.add_bouton_card()
                self.var01 = False

            if event.type == pygame.QUIT:
                self.quitter()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quitter()
                    pygame.quit()

            # Si on clique avec un bouton de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                # position x , y souris
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                # bouton milieu souris
                if event.button == 2:
                    pass

                # bouton gauche souris
                elif event.button == 1:
                    for key in self.bouton_card_liste:
                        # si la position x , y du sprite entre en colision avec position (pos) <=> souris
                        if key.rect.collidepoint(pos):
                            for i in range(0, len(self.liste_combat_temp), 1):
                                if self.liste_combat_temp[i] == 0:
                                    self.liste_combat_temp[i] = key.value
                                    key.rect_x = (self.inventaire_et_pioche_design.liste_positions_x_combat[i])
                                    key.rect_y = self.height_screen // 2
                                    key.afficher_carte_bouton(screen=self.screen)
                                    self.screen.blit(self.design_class.liste_all_cards_img[20],
                                                     (
                                                         self.inventaire_et_pioche_design.liste_positions_x_inventory[
                                                             key.id - 1],
                                                         self.height_screen - 150))

                                    key.detruire_selection_rect()
                                    print(self.liste_combat_temp)
                                    break

                    for key in self.bouton_ok_undo:
                        if key.rect.collidepoint(pos):
                            if key.value == "OK":
                                for i in range(0, 5, 1):
                                    if self.liste_combat_temp.count(0) == 0:
                                        self.list_combat_validee = self.liste_combat_temp
                                        print(f"list_combat_validee : {self.list_combat_validee}")
                                        self.statut = False
                                        break
                                    else:
                                        print(f"list_combat_validee : {self.list_combat_validee}")
                                        break

                            if key.value == "UNDO":
                                for i in range(0, 5, 1):
                                    self.screen.blit(self.design_class.liste_all_cards_img[20],
                                                     (
                                                         self.inventaire_et_pioche_design.liste_positions_x_combat[
                                                             i],
                                                         self.height_screen // 2))
                                self.bouton_card_liste.empty()
                                self.bouton_ok_undo.empty()

                                self.add_bouton_card()

                                self.liste_combat_temp = [0, 0, 0, 0, 0]
                                break

                    pygame.display.flip()

                # bouton droit souris
                elif event.button == 2:
                    for key in self.bouton_card_liste:
                        if key.rect.collidepoint(pos):
                            break

        pygame.display.flip()

"""
app = DesignInventory()

clock = pygame.time.Clock()

while app.statut:
    app.en_cours_execution()
"""