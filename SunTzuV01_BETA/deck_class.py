import random


class Deck(object):

    def __init__(self, player: str = "No_Name", tour_de_jeu: int = 0) -> None:

        self.list_special_cards: list[int] = [7, 8, 9, 10, 11, 12, 13, 14, 14]
        self.list_normals_cards: list[int] = [1, 2, 3, 4, 5, 6]
        self.list_inventory_cards: list[int] = []
        self.list_combat_cards: list[int] = [0, 0, 0, 0, 0]
        self.tour_de_jeu: int = tour_de_jeu
        self.player: str = player

    def shuffle(self):
        # melange la liste du deck
        random.shuffle(self.list_special_cards)
        print(f"\nMELANGE DE LA PIOCHE . . .")

    def distribute_special(self):

        # DISTRIBUTION des cartes au tour 1 début de la MANCHE 1
        if self.tour_de_jeu == 0:

            print(f"\nDébut de la MANCHE : {(self.tour_de_jeu//3)+1}")
            # donne 3 cartes spéciales et les retire de la pioche des cartes spéciales
            for _ in range(0, 3, 1):
                self.list_inventory_cards.append(self.list_special_cards.pop(0))

        # DISTRIBUTION des cartes au tour 3 début de la MANCHE 2
        if self.tour_de_jeu == 3:

            print(f"\nDébut de la MANCHE : {(self.tour_de_jeu//3)+1}")
            # donne 3 cartes spéciales et les retire de la pioche des cartes spéciales
            for _ in range(0, 3, 1):
                self.list_inventory_cards.append(self.list_special_cards.pop(0))

        # DISTRIBUTION des cartes au tour 6 début de la MANCHE 3
        if self.tour_de_jeu == 6:

            print(f"\nDébut de la MANCHE : {(self.tour_de_jeu//3)+1}")
            # donne 3 cartes spéciales et les retire de la pioche des cartes spéciales
            for _ in range(0, 3, 1):
                self.list_inventory_cards.append(self.list_special_cards.pop(0))

    def distribute_normal(self):
        # donne les cartes de 1 à 6
        print(f"\nTour numéro : {self.tour_de_jeu+1}")
        for j in range(1, 7, 1):
            if 0 == self.list_inventory_cards.count(j):
                self.list_inventory_cards.append(self.list_normals_cards[j - 1])

    def distribute(self):
        print(f"\n            JOUEUR : {self.player}\n")
        print(
            f"DEBUT DISTRIBUTION . . .\n"
            f"CARTES présentes avant distribution dans l'inventaire du joueur {self.player} : {self.list_inventory_cards} (list_inventory_cards)"
        )

        self.distribute_special()
        self.distribute_normal()
        self.list_inventory_cards.sort()

        print(
            f"FIN DISTRIBUTION . . .\n"
            f"CARTES présentent dans l'inventaire du joueur {self.player} : {self.list_inventory_cards} (list_inventory_cards)"
        )
        print("###COMBAT###")

    def show(self):

        # SIMULATION D'un tour (5 cartes enlevées)
        for _ in range(0, 5):
            self.list_inventory_cards.pop(random.randrange(3, 5, 1))

        print(f"APRES COMBAT{self.list_inventory_cards} Inventory_cards")

    def random_combat_list(self):
        random.shuffle(self.list_inventory_cards)
        for i in range(0, 5, 1):
            self.list_combat_cards.pop(i)
            self.list_combat_cards.insert(i, self.list_inventory_cards[0])
            self.list_inventory_cards.pop(0)
        print(
            f"LISTE de cartes sélectionnées aléatoirement parmis l'inventaire du joueur {self.player} "
            f"pour le combat (territoires 1 à 5) :\n      CARTES à jouer pour le combat = {self.list_combat_cards} "
        )


"""
test = Deck(player="Maxime")
for i in range(0, 9, 1):
    test.shuffle()
    test.distribute()
"""
