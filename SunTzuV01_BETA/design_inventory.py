import pygame
from design_class import Design
from inventaire_et_pioche_design import Inventaire
from typing import cast, Any

"""
pygame.mouse.get_pos() # donne la position (x, y)

pygame.mouse.get_pressed

sprites_clicked = [sprite for sprite in toute_ma_liste_de_sprites if sprite.rect.collidepoint(x, y)]

"""


class BoutonCardInventory(pygame.sprite.Sprite):

    def __init__(
        self,
        coord_x: int,
        coord_y: int,
        image_path: pygame.Surface,
        value: int,
        id: int,
        original_x: int | None = None,
        original_y: int | None = None,
        *groups: Any,
    ) -> None:
        super().__init__(*groups)
        self.image: pygame.Surface = image_path
        self.rect_x: int = coord_x
        self.rect_y: int = coord_y
        self.rect: pygame.Rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

        self.id: int = id
        self.value: int = value

        # Pour le drag & drop
        self.dragging: bool = False
        self.original_x: int = original_x if original_x is not None else coord_x
        self.original_y: int = original_y if original_y is not None else coord_y
        self.combat_slot: int | None = None
        self.clicked: bool = False
        self.linkReady: bool = False
        self.links: list[Any] = []

    def afficher_carte_bouton(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect_x, self.rect_y))
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

    def detruire_selection_rect(self):
        self.rect = self.image.get_rect(topleft=(-200, -200))

    def start_drag(self, mouse_pos: tuple[int, int]):
        """Commence le drag de la carte"""
        self.dragging = True

    def update_drag(self, mouse_pos: tuple[int, int]):
        """Met a jour la position pendant le drag"""
        if self.dragging:
            # Centre la carte sur la souris
            self.rect_x = mouse_pos[0] - self.image.get_width() // 2
            self.rect_y = mouse_pos[1] - self.image.get_height() // 2

    def stop_drag(self):
        """Arrete le drag"""
        self.dragging = False

    def return_to_original(self):
        """Retourne a la position d'origine"""
        self.rect_x = self.original_x
        self.rect_y = self.original_y
        self.combat_slot = None


class BoutonOKandUndo(pygame.sprite.Sprite):

    def __init__(self, coord_x: int, coord_y: int, image_path: pygame.Surface, value: str, id: int, *groups: Any) -> None:
        super().__init__(*groups)
        self.image: pygame.Surface = image_path
        self.rect_x: int = coord_x
        self.rect_y: int = coord_y
        self.rect: pygame.Rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))

        self.id: int = id
        self.value: str = value

        self.clicked: bool = False
        self.linkReady: bool = False
        self.links: list[Any] = []

    def afficher_ok_undo_bouton(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect_x, self.rect_y))
        self.rect = self.image.get_rect(topleft=(self.rect_x, self.rect_y))


class DesignInventoryBlue:

    def __init__(
        self,
        tour_de_jeu_deck_class: int = 0,
        list_inventory_cards: list[int] = [],
        listvalue1_img: pygame.Surface | int = 0,
        listvalue2_img: pygame.Surface | int = 0,
        listvalue3_img: pygame.Surface | int = 0,
        listvalue4_img: pygame.Surface | int = 0,
        listvalue5_img: pygame.Surface | int = 0,
        liste_unite_terrain_a: list[int] = [0, 0, 0, 0, 0],
        liste_unite_terrain_b: list[int] = [0, 0, 0, 0, 0],
        liste_all_numbers_img: list[pygame.Surface | int] = [],
    ) -> None:
        pygame.init()

        self.liste_combat_temp: list[int] = [0, 0, 0, 0, 0]
        self.list_combat_validee: list[int] = [0, 0, 0, 0, 0]

        self.listvalue1_img: pygame.Surface | int = listvalue1_img
        self.listvalue2_img: pygame.Surface | int = listvalue2_img
        self.listvalue3_img: pygame.Surface | int = listvalue3_img
        self.listvalue4_img: pygame.Surface | int = listvalue4_img
        self.listvalue5_img: pygame.Surface | int = listvalue5_img

        self.list_inventory_cards: list[int] = list_inventory_cards

        self.liste_unite_terrain_a: list[int] = liste_unite_terrain_a
        self.liste_unite_terrain_b: list[int] = liste_unite_terrain_b
        self.liste_size_territories: list[int] = [0, 0, 0, 0, 0]
        self.liste_color_territories: list[str] = ["VIDE", "VIDE", "VIDE", "VIDE", "VIDE"]
        self.var_pos_unit: int = 0
        self.liste_all_numbers_img: list[pygame.Surface | int] = liste_all_numbers_img

        self.design_class: Design = Design()
        self.inventaire_et_pioche_design: Inventaire = Inventaire(self.list_inventory_cards)

        self.tour_de_jeu: int = tour_de_jeu_deck_class

        self.var01: bool = True
        self.statut: bool = True

        self.width_screen: int = 1200
        self.height_screen: int = 700

        self.screen: pygame.Surface = pygame.display.get_surface()

        self.bouton_card_liste: pygame.sprite.Group[Any] = pygame.sprite.Group()
        self.bouton_ok_undo: pygame.sprite.Group[Any] = pygame.sprite.Group()

        # Variables pour le drag & drop
        self.dragged_card: BoutonCardInventory | None = None
        self.combat_slot_rects: list[pygame.Rect] = []  # Rectangles des emplacements de combat

        self.ok_button_img: pygame.Surface = pygame.image.load("ressources/OK.png")
        self.undo_button_img: pygame.Surface = pygame.image.load("ressources/Undo.png")
        self.back_wallet_inventory_img: pygame.Surface = pygame.image.load(
            "ressources/inventaire_wallet_back.png"
        )
        self.front_wallet_inventory_img: pygame.Surface = pygame.image.load(
            "ressources/inventaire_wallet_front.png"
        )
        self.map_img: pygame.Surface = pygame.image.load("ressources/back_ground_700x330.png")

        self.add_bouton_card()

    def quitter(self):
        self.statut = False

    def create_combat_slot_rects(self):
        """Cree les rectangles pour les zones de drop des cartes de combat"""
        self.combat_slot_rects = []
        card_width = 120  # Largeur de la zone de drop (plus large que la carte)
        card_height = 180  # Hauteur de la zone de drop (plus haute que la carte)
        for i in range(5):
            x_card = self.inventaire_et_pioche_design.liste_positions_x_combat[i]
            y_card = self.height_screen // 2
            # Centrer la zone de drop sur la position de la carte
            x = (
                x_card - (card_width - 70) // 2
            )  # 70 = largeur approximative de la carte
            y = (
                y_card - (card_height - 100) // 2
            )  # 100 = hauteur approximative de la carte
            rect = pygame.Rect(x, y, card_width, card_height)
            self.combat_slot_rects.append(rect)

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
    def position_unit_on_map(self, position: tuple[int, int], var_pos_unit: int):
        if self.liste_color_territories[var_pos_unit] == "BLEU":
            if self.liste_size_territories[var_pos_unit] < 14:
                self.screen.blit(
                    cast(
                        pygame.Surface,
                        self.liste_all_numbers_img[self.liste_size_territories[var_pos_unit]],
                    ),
                    position,
                )
            if self.liste_size_territories[var_pos_unit] >= 14:
                self.screen.blit(
                    cast(pygame.Surface, self.liste_all_numbers_img[0]), position
                )

        if self.liste_color_territories[var_pos_unit] == "ROUGE":

            if self.liste_size_territories[var_pos_unit] < 14:
                self.screen.blit(
                    cast(
                        pygame.Surface,
                        self.liste_all_numbers_img[
                            self.liste_size_territories[var_pos_unit] + 20
                        ],
                    ),
                    position,
                )
            if self.liste_size_territories[var_pos_unit] >= 14:
                self.screen.blit(
                    cast(pygame.Surface, self.liste_all_numbers_img[20]), position
                )

        if self.liste_color_territories[var_pos_unit] == "VIDE":
            self.screen.blit(
                cast(pygame.Surface, self.liste_all_numbers_img[14]), position
            )

    def add_bouton_card(self):

        self.design_class.charger_liste_all_cards_img()

        self.inventaire_et_pioche_design.afficher_inventaire()
        self.inventaire_et_pioche_design.afficher_emplacement_combat_bleu()

        # Creer les zones de drop
        self.create_combat_slot_rects()

        self.screen.blit(self.back_wallet_inventory_img, (0, self.height_screen - 160))

        for i in range(
            0, len(self.inventaire_et_pioche_design.list_inventory_cards), 1
        ):
            original_x = self.inventaire_et_pioche_design.liste_positions_x_inventory[i]
            original_y = self.height_screen - 150
            new_card = BoutonCardInventory(
                coord_x=original_x,
                coord_y=original_y,
                image_path=cast(
                    pygame.Surface,
                    self.design_class.liste_all_cards_img[
                        self.inventaire_et_pioche_design.list_inventory_cards[i]
                    ],
                ),
                value=self.inventaire_et_pioche_design.list_inventory_cards[i],
                id=len(self.bouton_card_liste) + 1,
                original_x=original_x,
                original_y=original_y,
            )
            self.bouton_card_liste.add(new_card)

            self.screen.blit(
                self.back_wallet_inventory_img, (0, self.height_screen - 160)
            )

        ok_btn = BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 350,
            image_path=self.ok_button_img,
            value="OK",
            id=len(self.bouton_ok_undo) + 1,
        )
        self.bouton_ok_undo.add(ok_btn)

        undo_btn = BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 270,
            image_path=self.undo_button_img,
            value="UNDO",
            id=len(self.bouton_ok_undo) + 1,
        )
        self.bouton_ok_undo.add(undo_btn)

        # Note: Drawing is handled in draw(), no need to blit here immediately if we are in a loop

    def update(self):
        """Mise a jour logique"""
        # Mise a jour du mouvement de la carte en cours de drag
        if self.dragged_card:
            mouse_pos = pygame.mouse.get_pos()
            self.dragged_card.update_drag(mouse_pos)

    def handle_event(self, event: pygame.event.Event) -> str | None:
        """Gestion des evenements"""
        if event.type == pygame.QUIT:
            self.quitter()
            return "QUIT"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quitter()
                return "QUIT"
                # pygame.quit() # On evite de quitter brutalement pygame ici

        # Gestion du drag & drop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Clic gauche - commence le drag
            if event.button == 1:
                # Verifie d'abord les boutons OK/UNDO
                clicked_button = False
                for key in self.bouton_ok_undo:
                    if key.rect.collidepoint(pos):
                        clicked_button = True
                        if key.value == "OK":
                            if self.liste_combat_temp.count(0) == 0:
                                self.list_combat_validee = self.liste_combat_temp
                                print(
                                    f"list_combat_validee : {self.list_combat_validee}"
                                )
                                self.statut = False
                            else:
                                print(f"Vous devez placer 5 cartes!")

                        elif key.value == "UNDO":
                            # Reinitialiser tout
                            # Note: Screen redraw handled in draw(), just reset logic
                            self.bouton_card_liste.empty()
                            self.bouton_ok_undo.empty()
                            self.add_bouton_card()
                            self.liste_combat_temp = [0, 0, 0, 0, 0]
                        break

                # Si on n'a pas clique sur un bouton, chercher une carte
                if not clicked_button:
                    for card in self.bouton_card_liste:
                        if card.rect.collidepoint(pos):
                            self.dragged_card = card
                            card.start_drag(pos)
                            break

            # Clic droit - retirer une carte placee
            elif event.button == 3:
                for card in self.bouton_card_liste:
                    if card.rect.collidepoint(pos) and card.combat_slot is not None:
                        # Retirer la carte de l'emplacement de combat
                        self.liste_combat_temp[card.combat_slot] = 0
                        card.return_to_original()
                        print(
                            f"Carte retiree - liste_combat_temp: {self.liste_combat_temp}"
                        )
                        break

        # Fin du drag
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragged_card:
                pos = pygame.mouse.get_pos()
                dropped_in_slot = False

                # Verifier si on drop sur un emplacement de combat
                for slot_index, slot_rect in enumerate(self.combat_slot_rects):
                    if slot_rect.collidepoint(pos):
                        # Verifier si l'emplacement est libre ou occupé
                        if self.liste_combat_temp[slot_index] == 0:
                            # Emplacement libre - placer la carte
                            if self.dragged_card.combat_slot is not None:
                                # La carte vient d'un autre emplacement
                                self.liste_combat_temp[
                                    self.dragged_card.combat_slot
                                ] = 0

                            self.liste_combat_temp[slot_index] = (
                                self.dragged_card.value
                            )
                            self.dragged_card.combat_slot = slot_index
                            self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                slot_index
                            ]
                            self.dragged_card.rect_y = self.height_screen // 2
                            dropped_in_slot = True
                            print(
                                f"Carte placee - liste_combat_temp: {self.liste_combat_temp}"
                            )
                        else:
                            # Emplacement occupe - echanger les cartes
                            for other_card in self.bouton_card_liste:
                                if other_card.combat_slot == slot_index:
                                    # Echanger les positions
                                    old_slot = self.dragged_card.combat_slot

                                    if old_slot is not None:
                                        # Echange entre deux emplacements
                                        self.liste_combat_temp[slot_index] = (
                                            self.dragged_card.value
                                        )
                                        self.liste_combat_temp[old_slot] = (
                                            other_card.value
                                        )

                                        other_card.combat_slot = old_slot
                                        other_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                            old_slot
                                        ]
                                        other_card.rect_y = self.height_screen // 2
                                    else:
                                        # Deplacement de l'inventaire vers un emplacement occupé
                                        self.liste_combat_temp[slot_index] = (
                                            self.dragged_card.value
                                        )
                                        other_card.return_to_original()

                                    self.dragged_card.combat_slot = slot_index
                                    self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                        slot_index
                                    ]
                                    self.dragged_card.rect_y = (
                                        self.height_screen // 2
                                    )
                                    dropped_in_slot = True
                                    print(
                                        f"Cartes echangees - liste_combat_temp: {self.liste_combat_temp}"
                                    )
                                    break
                        break

                # Si pas droppé sur un emplacement valide, retourner à l'origine
                if not dropped_in_slot:
                    if self.dragged_card.combat_slot is None:
                        self.dragged_card.return_to_original()
                    else:
                        # Retourner a l'emplacement de combat precedent
                        slot = self.dragged_card.combat_slot
                        self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                            slot
                        ]
                        self.dragged_card.rect_y = self.height_screen // 2

                self.dragged_card.stop_drag()
                self.dragged_card = None

    def draw(self):
        """Redessine tout l'ecran"""
        # Effacer l'ecran completement
        self.screen.fill((0, 0, 0))

        # Fond de la carte
        self.screen.blit(self.map_img, (int(self.width_screen * 0.15), 0))

        # Pion du tour
        self.screen.blit(
            self.design_class.pion_dragon_32x32,
            (int(self.width_screen / 2 + 211), 33 * (self.tour_de_jeu - 1)),
        )

        # Cartes des valeurs de zone
        self.screen.blit(
            cast(pygame.Surface, self.listvalue1_img),
            (int(self.width_screen / 2 - 540), 35),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue2_img),
            (int(self.width_screen / 2 - 540), 185),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue3_img),
            (int(self.width_screen / 2 + 300), 205),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue4_img),
            (int(self.width_screen / 2 + 300), 5),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue5_img),
            (int(self.width_screen / 2 + 300), 105),
        )

        # Fond du wallet
        self.screen.blit(self.back_wallet_inventory_img, (0, self.height_screen - 160))

        # Dessiner les emplacements de combat (cartes vides)
        for i in range(5):
            self.screen.blit(
                cast(pygame.Surface, self.design_class.liste_all_cards_img[0]),
                (
                    self.inventaire_et_pioche_design.liste_positions_x_combat[i],
                    self.height_screen // 2,
                ),
            )

        # Dessiner toutes les cartes SAUF celle en cours de drag
        for card in self.bouton_card_liste:
            if card != self.dragged_card:
                card.afficher_carte_bouton(screen=self.screen)

        # Dessiner les boutons OK/UNDO
        for button in self.bouton_ok_undo:
            button.afficher_ok_undo_bouton(screen=self.screen)

        # Dessiner la carte en cours de drag EN DERNIER (au premier plan)
        if self.dragged_card:
            self.dragged_card.afficher_carte_bouton(screen=self.screen)

        # Fond avant du wallet
        self.screen.blit(self.front_wallet_inventory_img, (0, self.height_screen - 50))


class DesignInventoryRed:

    def __init__(
        self,
        tour_de_jeu_deck_class: int = 0,
        list_inventory_cards: list[int] = [],
        listvalue1_img: pygame.Surface | int = 0,
        listvalue2_img: pygame.Surface | int = 0,
        listvalue3_img: pygame.Surface | int = 0,
        listvalue4_img: pygame.Surface | int = 0,
        listvalue5_img: pygame.Surface | int = 0,
    ) -> None:
        pygame.init()

        self.liste_combat_temp: list[int] = [0, 0, 0, 0, 0]
        self.list_combat_validee: list[int] = [0, 0, 0, 0, 0]

        self.listvalue1_img: pygame.Surface | int = listvalue1_img
        self.listvalue2_img: pygame.Surface | int = listvalue2_img
        self.listvalue3_img: pygame.Surface | int = listvalue3_img
        self.listvalue4_img: pygame.Surface | int = listvalue4_img
        self.listvalue5_img: pygame.Surface | int = listvalue5_img

        self.list_inventory_cards_red: list[int] = list_inventory_cards

        self.design_class: Design = Design()
        self.inventaire_et_pioche_design: Inventaire = Inventaire(self.list_inventory_cards_red)

        self.tour_de_jeu: int = tour_de_jeu_deck_class

        self.var01: bool = True
        self.statut: bool = True

        self.width_screen: int = 1200
        self.height_screen: int = 700

        self.screen: pygame.Surface = pygame.display.get_surface()

        self.bouton_card_liste: pygame.sprite.Group[Any] = pygame.sprite.Group()
        self.bouton_ok_undo: pygame.sprite.Group[Any] = pygame.sprite.Group()

        # Variables pour le drag & drop
        self.dragged_card: BoutonCardInventory | None = None
        self.combat_slot_rects: list[pygame.Rect] = []  # Rectangles des emplacements de combat

        self.ok_button_img: pygame.Surface = pygame.image.load("ressources/OK.png")
        self.undo_button_img: pygame.Surface = pygame.image.load("ressources/Undo.png")
        self.back_wallet_inventory_img: pygame.Surface = pygame.image.load(
            "ressources/inventaire_wallet_back.png"
        )
        self.front_wallet_inventory_img: pygame.Surface = pygame.image.load(
            "ressources/inventaire_wallet_front.png"
        )
        self.map_img: pygame.Surface = pygame.image.load("ressources/back_ground_700x330.png")

        self.add_bouton_card()

    def quitter(self):
        self.statut = False

    def create_combat_slot_rects(self):
        """Cree les rectangles pour les zones de drop des cartes de combat"""
        self.combat_slot_rects = []
        card_width = 120  # Largeur de la zone de drop (plus large que la carte)
        card_height = 180  # Hauteur de la zone de drop (plus haute que la carte)
        for i in range(5):
            x_card = self.inventaire_et_pioche_design.liste_positions_x_combat[i]
            y_card = self.height_screen // 2
            # Centrer la zone de drop sur la position de la carte
            x = (
                x_card - (card_width - 70) // 2
            )  # 70 = largeur approximative de la carte
            y = (
                y_card - (card_height - 100) // 2
            )  # 100 = hauteur approximative de la carte
            rect = pygame.Rect(x, y, card_width, card_height)
            self.combat_slot_rects.append(rect)

    def add_bouton_card(self):

        self.design_class.charger_liste_all_cards_img()

        self.inventaire_et_pioche_design.afficher_inventaire()
        self.inventaire_et_pioche_design.afficher_emplacement_combat_rouge()

        # Creer les zones de drop
        self.create_combat_slot_rects()

        self.screen.blit(self.back_wallet_inventory_img, (0, self.height_screen - 160))

        for i in range(
            0, len(self.inventaire_et_pioche_design.list_inventory_cards), 1
        ):
            original_x = self.inventaire_et_pioche_design.liste_positions_x_inventory[i]
            original_y = self.height_screen - 150
            new_card = BoutonCardInventory(
                coord_x=original_x,
                coord_y=original_y,
                image_path=cast(
                    pygame.Surface,
                    self.design_class.liste_all_cards_img[
                        self.inventaire_et_pioche_design.list_inventory_cards[i] + 20
                    ],
                ),
                value=self.inventaire_et_pioche_design.list_inventory_cards[i],
                id=len(self.bouton_card_liste) + 1,
                original_x=original_x,
                original_y=original_y,
            )
            self.bouton_card_liste.add(new_card)

            self.screen.blit(
                self.back_wallet_inventory_img, (0, self.height_screen - 160)
            )

        ok_btn = BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 350,
            image_path=self.ok_button_img,
            value="OK",
            id=len(self.bouton_ok_undo) + 1,
        )
        self.bouton_ok_undo.add(ok_btn)

        undo_btn = BoutonOKandUndo(
            coord_x=self.width_screen - 100,
            coord_y=self.height_screen - 270,
            image_path=self.undo_button_img,
            value="UNDO",
            id=len(self.bouton_ok_undo) + 1,
        )
        self.bouton_ok_undo.add(undo_btn)

        for card in self.bouton_card_liste:
            card.afficher_carte_bouton(screen=self.screen)

        for button in self.bouton_ok_undo:
            button.afficher_ok_undo_bouton(screen=self.screen)

        self.screen.blit(self.front_wallet_inventory_img, (0, self.height_screen - 50))

    def update(self):
        """Mise a jour logique"""
        # Mise a jour du mouvement de la carte en cours de drag
        if self.dragged_card:
            mouse_pos = pygame.mouse.get_pos()
            self.dragged_card.update_drag(mouse_pos)

    def handle_event(self, event: pygame.event.Event) -> str | None:
        """Gestion des evenements"""
        if event.type == pygame.QUIT:
            self.quitter()
            return "QUIT"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quitter()
                return "QUIT"
                # pygame.quit()

        # Gestion du drag & drop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Clic gauche - commence le drag
            if event.button == 1:
                # Verifie d'abord les boutons OK/UNDO
                clicked_button = False
                for key in self.bouton_ok_undo:
                    if key.rect.collidepoint(pos):
                        clicked_button = True
                        if key.value == "OK":
                            if self.liste_combat_temp.count(0) == 0:
                                self.list_combat_validee = self.liste_combat_temp
                                print(
                                    f"list_combat_validee : {self.list_combat_validee}"
                                )
                                self.statut = False
                            else:
                                print(f"Vous devez placer 5 cartes!")

                        elif key.value == "UNDO":
                            # Reinitialiser tout
                            self.bouton_card_liste.empty()
                            self.bouton_ok_undo.empty()
                            self.add_bouton_card()
                            self.liste_combat_temp = [0, 0, 0, 0, 0]
                        break

                # Si on n'a pas clique sur un bouton, chercher une carte
                if not clicked_button:
                    for card in self.bouton_card_liste:
                        if card.rect.collidepoint(pos):
                            self.dragged_card = card
                            card.start_drag(pos)
                            break

            # Clic droit - retirer une carte placee
            elif event.button == 3:
                for card in self.bouton_card_liste:
                    if card.rect.collidepoint(pos) and card.combat_slot is not None:
                        # Retirer la carte de l'emplacement de combat
                        self.liste_combat_temp[card.combat_slot] = 0
                        card.return_to_original()
                        print(
                            f"Carte retiree - liste_combat_temp: {self.liste_combat_temp}"
                        )
                        break

        # Fin du drag
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragged_card:
                pos = pygame.mouse.get_pos()
                dropped_in_slot = False

                # Verifier si on drop sur un emplacement de combat
                for slot_index, slot_rect in enumerate(self.combat_slot_rects):
                    if slot_rect.collidepoint(pos):
                        # Verifier si l'emplacement est libre ou occupé
                        if self.liste_combat_temp[slot_index] == 0:
                            # Emplacement libre - placer la carte
                            if self.dragged_card.combat_slot is not None:
                                # La carte vient d'un autre emplacement
                                self.liste_combat_temp[
                                    self.dragged_card.combat_slot
                                ] = 0

                            self.liste_combat_temp[slot_index] = (
                                self.dragged_card.value
                            )
                            self.dragged_card.combat_slot = slot_index
                            self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                slot_index
                            ]
                            self.dragged_card.rect_y = self.height_screen // 2
                            dropped_in_slot = True
                            print(
                                f"Carte placee - liste_combat_temp: {self.liste_combat_temp}"
                            )
                        else:
                            # Emplacement occupe - echanger les cartes
                            for other_card in self.bouton_card_liste:
                                if other_card.combat_slot == slot_index:
                                    # Echanger les positions
                                    old_slot = self.dragged_card.combat_slot

                                    if old_slot is not None:
                                        # Echange entre deux emplacements
                                        self.liste_combat_temp[slot_index] = (
                                            self.dragged_card.value
                                        )
                                        self.liste_combat_temp[old_slot] = (
                                            other_card.value
                                        )

                                        other_card.combat_slot = old_slot
                                        other_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                            old_slot
                                        ]
                                        other_card.rect_y = self.height_screen // 2
                                    else:
                                        # Deplacement de l'inventaire vers un emplacement occupé
                                        self.liste_combat_temp[slot_index] = (
                                            self.dragged_card.value
                                        )
                                        other_card.return_to_original()

                                    self.dragged_card.combat_slot = slot_index
                                    self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                                        slot_index
                                    ]
                                    self.dragged_card.rect_y = (
                                        self.height_screen // 2
                                    )
                                    dropped_in_slot = True
                                    print(
                                        f"Cartes echangees - liste_combat_temp: {self.liste_combat_temp}"
                                    )
                                    break
                        break

                # Si pas droppé sur un emplacement valide, retourner à l'origine
                if not dropped_in_slot:
                    if self.dragged_card.combat_slot is None:
                        self.dragged_card.return_to_original()
                    else:
                        # Retourner a l'emplacement de combat precedent
                        slot = self.dragged_card.combat_slot
                        self.dragged_card.rect_x = self.inventaire_et_pioche_design.liste_positions_x_combat[
                            slot
                        ]
                        self.dragged_card.rect_y = self.height_screen // 2

                self.dragged_card.stop_drag()
                self.dragged_card = None

    def draw(self):
        """Redessine tout l'ecran"""
        # Effacer l'ecran completement
        self.screen.fill((0, 0, 0))

        # Fond de la carte
        self.screen.blit(self.map_img, (int(self.width_screen * 0.15), 0))

        # Pion du tour
        self.screen.blit(
            self.design_class.pion_dragon_32x32,
            (int(self.width_screen / 2 + 211), 33 * (self.tour_de_jeu - 1)),
        )

        # Cartes des valeurs de zone
        self.screen.blit(
            cast(pygame.Surface, self.listvalue1_img),
            (int(self.width_screen / 2 - 540), 35),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue2_img),
            (int(self.width_screen / 2 - 540), 185),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue3_img),
            (int(self.width_screen / 2 + 300), 205),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue4_img),
            (int(self.width_screen / 2 + 300), 5),
        )
        self.screen.blit(
            cast(pygame.Surface, self.listvalue5_img),
            (int(self.width_screen / 2 + 300), 105),
        )

        # Fond du wallet
        self.screen.blit(self.back_wallet_inventory_img, (0, self.height_screen - 160))

        # Dessiner les emplacements de combat (cartes vides rouges)
        for i in range(5):
            self.screen.blit(
                cast(pygame.Surface, self.design_class.liste_all_cards_img[20]),
                (
                    self.inventaire_et_pioche_design.liste_positions_x_combat[i],
                    self.height_screen // 2,
                ),
            )

        # Dessiner toutes les cartes SAUF celle en cours de drag
        for card in self.bouton_card_liste:
            if card != self.dragged_card:
                card.afficher_carte_bouton(screen=self.screen)

        # Dessiner les boutons OK/UNDO
        for button in self.bouton_ok_undo:
            button.afficher_ok_undo_bouton(screen=self.screen)

        # Dessiner la carte en cours de drag EN DERNIER (au premier plan)
        if self.dragged_card:
            self.dragged_card.afficher_carte_bouton(screen=self.screen)

        # Fond avant du wallet
        self.screen.blit(self.front_wallet_inventory_img, (0, self.height_screen - 50))


"""
app = DesignInventory()

clock = pygame.time.Clock()

while app.statut:
    app.en_cours_execution()
"""
