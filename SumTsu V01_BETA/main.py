import pygame
from zoneplay_values_class import Zoneplay
from deck_class import Deck
from design_inventory import DesignInventoryBlue
from design_inventory import DesignInventoryRed
from combat_class import Combat
from design_class import Design
from score_class import Score


class Game:

    def __init__(self):

        pygame.init()

        self.zoneplay_values_class = Zoneplay()
        self.zoneplay_values_class.random_zone_value()
        self.listvalue1 = self.zoneplay_values_class.listvalue1
        self.listvalue2 = self.zoneplay_values_class.listvalue2
        self.listvalue3 = self.zoneplay_values_class.listvalue3
        self.listvalue4 = self.zoneplay_values_class.listvalue4
        self.listvalue5 = self.zoneplay_values_class.listvalue5

        self.tour_de_jeu = 0

        self.deck_class_a = Deck('A, BLEU', tour_de_jeu=self.tour_de_jeu)
        self.deck_class_b = Deck('B, ROUGE', tour_de_jeu=self.tour_de_jeu)
        # self.deck_class_b.random_combat_list()
        # self.liste_combat_b = self.deck_class_b.list_combat_cards

        self.liste_combat_a = [0, 0, 0, 0, 0]
        self.liste_combat_b = [0, 0, 0, 0, 0]
        self.liste_unitee_terrain_a = [0, 0, 0, 0, 0]
        self.liste_unitee_terrain_b = [0, 0, 0, 0, 0]
        self.var_pos_unit = 0

        self.deck_class_a.shuffle()
        self.deck_class_a.distribute()

        self.deck_class_b.shuffle()
        self.deck_class_b.distribute()

        self.blue_theme_music = pygame.mixer.Sound("ressources/blue_theme.ogg")
        self.red_theme_music = pygame.mixer.Sound("ressources/red_theme.ogg")
        self.battle_theme_music = pygame.mixer.Sound("ressources/battle_theme.ogg")

        self.design_class = Design(liste_combat_a_bas=self.liste_combat_a,
                                   liste_unite_terrain_a=self.liste_unitee_terrain_a,
                                   liste_combat_b_haut=self.liste_combat_b,
                                   liste_unite_terrain_b=self.liste_unitee_terrain_b,
                                   tour_de_jeu_deck_class=self.tour_de_jeu,
                                   listvalue1=self.listvalue1,
                                   listvalue2=self.listvalue2,
                                   listvalue3=self.listvalue3,
                                   listvalue4=self.listvalue4,
                                   listvalue5=self.listvalue5,)

        self.design_class.selection_imgcardterrainvalue()
        self.design_class.charger_liste_all_numbers_img()

        self.score_class = Score(tour_de_jeu=self.tour_de_jeu,
                                 liste_unitee_terrain_a=self.liste_unitee_terrain_a,
                                 liste_unitee_terrain_b=self.liste_unitee_terrain_b,
                                 listvalue1=self.listvalue1,
                                 listvalue2=self.listvalue2,
                                 listvalue3=self.listvalue3,
                                 listvalue4=self.listvalue4,
                                 listvalue5=self.listvalue5,
                                 liste_color_territories=self.design_class.liste_color_territories,
                                 liste_size_territories=self.design_class.liste_size_territories)

    def phase_distribution_carte(self):
        self.deck_class_a.shuffle()
        self.deck_class_a.distribute()

        self.deck_class_b.shuffle()
        self.deck_class_b.distribute()
        # self.deck_class_b.random_combat_list()
        # self.liste_combat_b = self.deck_class_b.list_combat_cards

    def phase_choix_carte_combat_blue(self):
        self.design_inventory_blue = DesignInventoryBlue(tour_de_jeu_deck_class=self.tour_de_jeu,
                                                         list_inventory_cards=self.deck_class_a.list_inventory_cards,
                                                         listvalue1_img=self.design_class.listvalue1_img,
                                                         listvalue2_img=self.design_class.listvalue2_img,
                                                         listvalue3_img=self.design_class.listvalue3_img,
                                                         listvalue4_img=self.design_class.listvalue4_img,
                                                         listvalue5_img=self.design_class.listvalue5_img,
                                                         liste_unite_terrain_a=self.liste_unitee_terrain_a,
                                                         liste_unite_terrain_b=self.liste_unitee_terrain_b,
                                                         liste_all_numbers_img=self.design_class.liste_all_numbers_img
                                                         )
        self.design_inventory_blue.analyse_number_unit_on_each_territories()
        self.design_inventory_blue.analyse_color_unit_on_each_territories()

        self.design_inventory_blue.statut = True
        while self.design_inventory_blue.statut:
            self.design_inventory_blue.en_cours_execution()
            if self.var_pos_unit < 4:
                # Terrain 1 : "XINJIANG"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 - 195,
                                                                          self.design_class.height_screen // 2 - 290))
                self.var_pos_unit += 1

                # Terrain 1 : "TIBET"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 - 215,
                                                                          self.design_class.height_screen // 2 - 200))
                self.var_pos_unit += 1

                # Terrain 1 : "QINGHAI"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 45,
                                                                          self.design_class.height_screen // 2 - 170))
                self.var_pos_unit += 1

                # Terrain 1 : "MONGOLIA"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 15,
                                                                          self.design_class.height_screen // 2 - 330))
                self.var_pos_unit += 1

                # Terrain 1 : "MANDARIN"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 40,
                                                                          self.design_class.height_screen // 2 - 265))
                self.var_pos_unit += 1
                pygame.display.flip()

        self.var_pos_unit = 0
        self.liste_combat_a = self.design_inventory_blue.list_combat_validee

    def phase_choix_carte_combat_red(self):
        self.design_inventory_red = DesignInventoryRed(self.tour_de_jeu, self.deck_class_b.list_inventory_cards,
                                                       listvalue1_img=self.design_class.listvalue1_img,
                                                       listvalue2_img=self.design_class.listvalue2_img,
                                                       listvalue3_img=self.design_class.listvalue3_img,
                                                       listvalue4_img=self.design_class.listvalue4_img,
                                                       listvalue5_img=self.design_class.listvalue5_img
                                                       )
        self.design_inventory_red.statut = True
        while self.design_inventory_red.statut:
            self.design_inventory_red.en_cours_execution()

            # UTILISATION DE L'OBJET design_inventory_blue.position_unit_on_map car on affiche unitee on map identique...
            # ET ON L'UTILISE TJS APRES phase_choix_carte_combat_blue

            if self.var_pos_unit < 4:
                # Terrain 1 : "XINJIANG"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 - 195,
                                                                          self.design_class.height_screen // 2 - 290))
                self.var_pos_unit += 1

                # Terrain 1 : "TIBET"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 - 215,
                                                                          self.design_class.height_screen // 2 - 200))
                self.var_pos_unit += 1

                # Terrain 1 : "QINGHAI"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 45,
                                                                          self.design_class.height_screen // 2 - 170))
                self.var_pos_unit += 1

                # Terrain 1 : "MONGOLIA"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 15,
                                                                          self.design_class.height_screen // 2 - 330))
                self.var_pos_unit += 1

                # Terrain 1 : "MANDARIN"
                self.design_inventory_blue.position_unit_on_map(var_pos_unit=self.var_pos_unit,
                                                                position=(self.design_class.width_screen // 2 + 40,
                                                                          self.design_class.height_screen // 2 - 265))
                self.var_pos_unit += 1
                pygame.display.flip()

        self.var_pos_unit = 0
        self.liste_combat_b = self.design_inventory_red.list_combat_validee

    def phase_combat(self, liste_combat_a, liste_unitee_terrain_a, liste_combat_b, liste_unitee_terrain_b):
        # self.design_inventory.deck_bleu.list_combat_cards
        # self.inventaire_B.list_combat_cards

        versus_a_b = Combat(liste_de_combat_a=liste_combat_a,
                            liste_unite_terrain_a=liste_unitee_terrain_a,
                            liste_de_combat_b=liste_combat_b,
                            liste_unite_terrain_b=liste_unitee_terrain_b)
        print(versus_a_b.liste_unite_terrain_a)
        print(versus_a_b.liste_unite_terrain_b)

        versus_a_b.combattre()
        self.liste_unitee_terrain_a = versus_a_b.liste_unite_terrain_a
        self.liste_unitee_terrain_b = versus_a_b.liste_unite_terrain_b

        print(versus_a_b.liste_unite_terrain_a)
        print(versus_a_b.liste_unite_terrain_b)

    def phase_execusion_combat_design(self):

        self.design_class = Design(
            liste_combat_a_bas=self.liste_combat_a,
            liste_unite_terrain_a=self.liste_unitee_terrain_a,
            liste_combat_b_haut=self.liste_combat_b,
            liste_unite_terrain_b=self.liste_unitee_terrain_b,
            tour_de_jeu_deck_class=self.tour_de_jeu,
            listvalue1=self.listvalue1,
            listvalue2=self.listvalue2,
            listvalue3=self.listvalue3,
            listvalue4=self.listvalue4,
            listvalue5=self.listvalue5
        )
        self.design_class.selection_imgcardterrainvalue()
        self.design_class.running = True
        self.design_class.score_blue = self.score_class.score_a_blue
        self.design_class.score_red = self.score_class.score_b_red

        pygame.display.flip()
        while self.design_class.running:
            self.design_class.start_design()


    def update_tour_de_jeu(self):
        self.deck_class_a.tour_de_jeu = self.tour_de_jeu
        self.deck_class_b.tour_de_jeu = self.tour_de_jeu

    def verification_cartes_speciales_utilisees(self):
        for carte_combat in self.liste_combat_a:
            for carte_inventaire in self.deck_class_a.list_inventory_cards:
                if carte_combat == carte_inventaire and carte_combat > 6:
                    self.deck_class_a.list_inventory_cards.pop(
                        self.deck_class_a.list_inventory_cards.index(carte_inventaire))

        for carte_combat in self.liste_combat_b:
            for carte_inventaire in self.deck_class_b.list_inventory_cards:
                if carte_combat == carte_inventaire and carte_combat > 6:
                    self.deck_class_b.list_inventory_cards.pop(
                        self.deck_class_b.list_inventory_cards.index(carte_inventaire))

    def verification_victoire(self):
        self.score_class.update(tour_de_jeu=self.tour_de_jeu,
                                liste_unitee_terrain_a=self.liste_unitee_terrain_a,
                                liste_unitee_terrain_b=self.liste_unitee_terrain_b,
                                liste_color_territories=self.design_class.liste_color_territories)

        self.score_class.win_condition()



    def deroulement_test(self):
        self.blue_theme_music.play(loops=-1)
        self.phase_choix_carte_combat_blue()
        self.blue_theme_music.stop()
        self.red_theme_music.play(loops=-1)
        self.phase_choix_carte_combat_red()
        self.red_theme_music.stop()
        self.phase_combat(liste_combat_a=self.liste_combat_a, liste_unitee_terrain_a=self.liste_unitee_terrain_a,
                          liste_combat_b=self.liste_combat_b, liste_unitee_terrain_b=self.liste_unitee_terrain_b)
        self.tour_de_jeu += 1
        print(f"TOUR DE JEU {self.tour_de_jeu}")
        self.update_tour_de_jeu()
        self.verification_victoire()
        self.battle_theme_music.play(loops=-1)
        self.phase_execusion_combat_design()
        self.battle_theme_music.stop()
        self.verification_cartes_speciales_utilisees()
        self.phase_distribution_carte()
        self.verification_victoire()

        

test = Game()
for i in range(0, 9, 1):
    test.deroulement_test()
    if test.score_class.end_game:
        break
