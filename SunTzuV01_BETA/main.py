import os
import sys

# Si le jeu est lancé en tant qu'exécutable (frozen), on se déplace dans le dossier temporaire d'extraction
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

import pygame
import asyncio
from enum import Enum, auto
from typing import Union, cast
from zoneplay_values_class import Zoneplay
from deck_class import Deck
from design_inventory import DesignInventoryBlue
from design_inventory import DesignInventoryRed
from combat_class import Combat
from design_class import Design
from score_class import Score


class GameState(Enum):
    CHOIX_BLEU = auto()
    CHOIX_ROUGE = auto()
    COMBAT_LOGIQUE = auto()
    COMBAT_ANIM = auto()
    VICTOIRE = auto()


class Game:

    def __init__(self):
        pygame.init()
        # Initialize screen once for the whole game
        self.width_screen = 1200
        self.height_screen = 700

        # Mode fenetre pour toutes les plateformes (evite les soucis de resolution/coordonnees)
        self.screen = pygame.display.set_mode((self.width_screen, self.height_screen))

        self.zoneplay_values_class = Zoneplay()
        self.zoneplay_values_class.random_zone_value()
        self.listvalue1 = self.zoneplay_values_class.listvalue1
        self.listvalue2 = self.zoneplay_values_class.listvalue2
        self.listvalue3 = self.zoneplay_values_class.listvalue3
        self.listvalue4 = self.zoneplay_values_class.listvalue4
        self.listvalue5 = self.zoneplay_values_class.listvalue5

        self.tour_de_jeu = 1
        self.max_tours = 10

        self.deck_class_a = Deck("A, BLEU", tour_de_jeu=self.tour_de_jeu)
        self.deck_class_b = Deck("B, ROUGE", tour_de_jeu=self.tour_de_jeu)

        self.liste_combat_a: list[int] = [0, 0, 0, 0, 0]
        self.liste_combat_b: list[int] = [0, 0, 0, 0, 0]
        self.liste_unitee_terrain_a: list[int] = [0, 0, 0, 0, 0]
        self.liste_unitee_terrain_b: list[int] = [0, 0, 0, 0, 0]
        self.var_pos_unit = 0

        self.deck_class_a.shuffle()
        self.deck_class_a.distribute()

        self.deck_class_b.shuffle()
        self.deck_class_b.distribute()

        self.blue_theme_music = pygame.mixer.Sound("ressources/blue_theme.ogg")
        self.red_theme_music = pygame.mixer.Sound("ressources/red_theme.ogg")
        self.battle_theme_music = pygame.mixer.Sound("ressources/battle_theme.ogg")

        # Initialisation du Design Class (utilisé pour les assets communs)
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
            listvalue5=self.listvalue5,
        )
        self.design_class.selection_imgcardterrainvalue()
        self.design_class.charger_liste_all_numbers_img()

        self.score_class = Score(
            tour_de_jeu=self.tour_de_jeu,
            liste_unitee_terrain_a=self.liste_unitee_terrain_a,
            liste_unitee_terrain_b=self.liste_unitee_terrain_b,
            listvalue1=self.listvalue1,
            listvalue2=self.listvalue2,
            listvalue3=self.listvalue3,
            listvalue4=self.listvalue4,
            listvalue5=self.listvalue5,
            liste_color_territories=self.design_class.liste_color_territories,
            liste_size_territories=self.design_class.liste_size_territories,
        )

        # State Machine Initialization
        self.state = GameState.CHOIX_BLEU
        self.current_ui: Union[
            DesignInventoryBlue, DesignInventoryRed, Design, None
        ] = None
        self.start_phase_choix_blue()

    def start_phase_choix_blue(self):
        print(f"--- DEBUT TOUR {self.tour_de_jeu} ---")
        self.blue_theme_music.play(loops=-1)
        self.design_inventory_blue = DesignInventoryBlue(
            tour_de_jeu_deck_class=self.tour_de_jeu,
            list_inventory_cards=self.deck_class_a.list_inventory_cards,
            listvalue1_img=self.design_class.listvalue1_img,
            listvalue2_img=self.design_class.listvalue2_img,
            listvalue3_img=self.design_class.listvalue3_img,
            listvalue4_img=self.design_class.listvalue4_img,
            listvalue5_img=self.design_class.listvalue5_img,
            liste_unite_terrain_a=self.liste_unitee_terrain_a,
            liste_unite_terrain_b=self.liste_unitee_terrain_b,
            liste_all_numbers_img=self.design_class.liste_all_numbers_img,
            score_blue=self.score_class.score_a_blue,
            score_red=self.score_class.score_b_red,
        )
        self.design_inventory_blue.analyse_number_unit_on_each_territories()
        self.design_inventory_blue.analyse_color_unit_on_each_territories()

        # Pre-position units on map for display (from old code loop)
        # Note: In the new system, we trust the draw loop to handle this if coords are correct.

        self.current_ui = self.design_inventory_blue
        self.state = GameState.CHOIX_BLEU

    def start_phase_choix_red(self):
        self.blue_theme_music.stop()
        self.red_theme_music.play(loops=-1)
        self.design_inventory_red = DesignInventoryRed(
            self.tour_de_jeu,
            self.deck_class_b.list_inventory_cards,
            listvalue1_img=self.design_class.listvalue1_img,
            listvalue2_img=self.design_class.listvalue2_img,
            listvalue3_img=self.design_class.listvalue3_img,
            listvalue4_img=self.design_class.listvalue4_img,
            listvalue5_img=self.design_class.listvalue5_img,
            liste_unite_terrain_a=self.liste_unitee_terrain_a,
            liste_unite_terrain_b=self.liste_unitee_terrain_b,
            liste_all_numbers_img=self.design_class.liste_all_numbers_img,
            score_blue=self.score_class.score_a_blue,
            score_red=self.score_class.score_b_red,
        )
        self.design_inventory_red.analyse_number_unit_on_each_territories()
        self.design_inventory_red.analyse_color_unit_on_each_territories()
        
        self.current_ui = self.design_inventory_red
        self.state = GameState.CHOIX_ROUGE

    def execute_combat_logic(self):
        self.red_theme_music.stop()

        # Retrieve choices
        self.liste_combat_a = self.design_inventory_blue.list_combat_validee
        self.liste_combat_b = self.design_inventory_red.list_combat_validee

        versus_a_b = Combat(
            liste_de_combat_a=self.liste_combat_a,
            liste_unite_terrain_a=self.liste_unitee_terrain_a,
            liste_de_combat_b=self.liste_combat_b,
            liste_unite_terrain_b=self.liste_unitee_terrain_b,
        )

        versus_a_b.combattre()
        self.liste_unitee_terrain_a = versus_a_b.liste_unite_terrain_a
        self.liste_unitee_terrain_b = versus_a_b.liste_unite_terrain_b

        print(f"Unités A: {self.liste_unitee_terrain_a}")
        print(f"Unités B: {self.liste_unitee_terrain_b}")

        # Prepare Animation
        self.start_phase_anim_combat()

    def start_phase_anim_combat(self):
        self.battle_theme_music.play(loops=-1)
        self.tour_de_jeu += (
            1  # Increment turn here as per old logic (it was before update_tour_de_jeu)
        )
        self.update_tour_de_jeu()

        # Update Design data for analysis (needed for score calculation)
        self.design_class.liste_unite_terrain_a = self.liste_unitee_terrain_a
        self.design_class.liste_unite_terrain_b = self.liste_unitee_terrain_b
        self.design_class.analyse_color_unit_on_each_territories()

        # Update Score data and calculate score BEFORE animation display
        self.score_class.update(
            tour_de_jeu=self.tour_de_jeu,
            liste_unitee_terrain_a=self.liste_unitee_terrain_a,
            liste_unitee_terrain_b=self.liste_unitee_terrain_b,
            liste_color_territories=self.design_class.liste_color_territories,
        )
        self.score_class.win_condition()

        # Re-init Design for animation with updated values (including score)
        self.design_class.update_design(
            score_blue=self.score_class.score_a_blue,
            score_red=self.score_class.score_b_red,
            liste_combat_a_bas=self.liste_combat_a,
            liste_unite_terrain_a=self.liste_unitee_terrain_a,
            liste_combat_b_haut=self.liste_combat_b,
            liste_unite_terrain_b=self.liste_unitee_terrain_b,
            tour_de_jeu_deck_class=self.tour_de_jeu,
            listvalue1=self.listvalue1,
            listvalue2=self.listvalue2,
            listvalue3=self.listvalue3,
            listvalue4=self.listvalue4,
            listvalue5=self.listvalue5,
        )
        self.design_class.charger_liste_all_cards_img()  # Ensure images loaded
        self.design_class.analyse_color_unit_on_each_territories()
        self.design_class.analyse_number_unit_on_each_territories()

        self.current_ui = self.design_class
        self.state = GameState.COMBAT_ANIM

    def update_tour_de_jeu(self):
        self.deck_class_a.tour_de_jeu = self.tour_de_jeu
        self.deck_class_b.tour_de_jeu = self.tour_de_jeu

    def check_victory_and_cleanup(self):
        self.battle_theme_music.stop()

        # Score calculation is now done in start_phase_anim_combat
        
        if self.score_class.end_game:
            self.state = GameState.VICTOIRE
            # Design class handles victory drawing, just need to set data if needed
            # But Design class methods for victory take args, so we handle it in draw loop
        else:
            if self.tour_de_jeu >= self.max_tours:
                # Should have ended by score logic, but just in case
                self.state = GameState.VICTOIRE
            else:
                # Prepare next turn
                self.verification_cartes_speciales_utilisees()
                self.phase_distribution_carte()
                self.start_phase_choix_blue()

    def verification_cartes_speciales_utilisees(self):
        for carte_combat in self.liste_combat_a:
            for carte_inventaire in self.deck_class_a.list_inventory_cards:
                if carte_combat == carte_inventaire and carte_combat > 6:
                    self.deck_class_a.list_inventory_cards.pop(
                        self.deck_class_a.list_inventory_cards.index(carte_inventaire)
                    )

        for carte_combat in self.liste_combat_b:
            for carte_inventaire in self.deck_class_b.list_inventory_cards:
                if carte_combat == carte_inventaire and carte_combat > 6:
                    self.deck_class_b.list_inventory_cards.pop(
                        self.deck_class_b.list_inventory_cards.index(carte_inventaire)
                    )

    def phase_distribution_carte(self):
        self.deck_class_a.shuffle()
        self.deck_class_a.distribute()

        self.deck_class_b.shuffle()
        self.deck_class_b.distribute()

    def handle_event(self, event: pygame.event.Event) -> bool:
        if self.state == GameState.VICTOIRE:
            result = self.design_class.handle_event_victory(event)
            if result == "QUIT":
                return False  # Exit Game
            return True

        if self.current_ui:
            result = self.current_ui.handle_event(event)
            if result == "QUIT":
                return False  # Exit Game
            if result == "CONTINUE" and self.state == GameState.COMBAT_ANIM:
                self.check_victory_and_cleanup()

        return True

    def update(self):
        if self.state == GameState.COMBAT_LOGIQUE:
            self.execute_combat_logic()
            return

        if self.current_ui is None:
            return

        if self.state == GameState.CHOIX_BLEU:
            inventory_blue = cast(DesignInventoryBlue, self.current_ui)
            inventory_blue.update()
            if not inventory_blue.statut:  # Done
                self.start_phase_choix_red()

        elif self.state == GameState.CHOIX_ROUGE:
            inventory_red = cast(DesignInventoryRed, self.current_ui)
            inventory_red.update()
            if not inventory_red.statut:  # Done
                self.state = GameState.COMBAT_LOGIQUE

        elif self.state == GameState.COMBAT_ANIM:
            cast(Design, self.current_ui).update()

        elif self.state == GameState.VICTOIRE:
            pass  # Nothing to update usually

    def draw(self):
        if self.state == GameState.VICTOIRE:
            self.design_class.draw_victory(
                gagnant=cast(str, self.score_class.gagnant),
                score_blue=self.score_class.score_a_blue,
                score_red=self.score_class.score_b_red,
            )
        elif self.current_ui:
            self.current_ui.draw()


async def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if not game.handle_event(event):
                running = False

        game.update()
        game.draw()

        pygame.display.flip()
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
