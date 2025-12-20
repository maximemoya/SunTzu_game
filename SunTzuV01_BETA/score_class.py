class Score:

    def __init__(self, tour_de_jeu: int = 0, liste_unitee_terrain_a: list[int] = [0, 0, 0, 0, 0], liste_unitee_terrain_b: list[int] = [0, 0, 0, 0, 0],
                 listvalue1: list[int] = [0, 0, 0], listvalue2: list[int] = [0, 0, 0], listvalue3: list[int] = [0, 0, 0], listvalue4: list[int] = [0, 0, 0], listvalue5: list[int] = [0, 0, 0],
                 liste_color_territories: list[str | int] = [9, 9, 9, 9, 9], liste_size_territories: list[int] = [99, 99, 99, 99, 99]) -> None:

        self.tour_de_jeu = tour_de_jeu
        self.liste_unitee_terrain_a_bleu = liste_unitee_terrain_a
        self.liste_unitee_terrain_b_rouge = liste_unitee_terrain_b
        self.listvalue1 = listvalue1
        self.listvalue2 = listvalue2
        self.listvalue3 = listvalue3
        self.listvalue4 = listvalue4
        self.listvalue5 = listvalue5
        self.combined_list_values_12345 = [self.listvalue1, self.listvalue2,
                                           self.listvalue3, self.listvalue4, self.listvalue5]

        self.liste_color_territories = liste_color_territories
        self.liste_size_territories = liste_size_territories

        self.score_a_blue = int(0)
        self.score_b_red = int(0)
        self.score_a_blue_win = False
        self.score_b_red_win = False
        self.end_game = False
        self.gagnant: str | None = None

    def update(self, tour_de_jeu: int, liste_unitee_terrain_a: list[int], liste_unitee_terrain_b: list[int], liste_color_territories: list[str | int]) -> None:
        self.tour_de_jeu = tour_de_jeu
        self.liste_unitee_terrain_a_bleu = liste_unitee_terrain_a
        self.liste_unitee_terrain_b_rouge = liste_unitee_terrain_b
        self.liste_color_territories = liste_color_territories

    def win_condition(self):
        if self.tour_de_jeu == 3:
            for i in range(0, 5, 1):
                if self.liste_color_territories[i] == "BLEU":
                    liste = self.combined_list_values_12345[i]
                    self.score_a_blue += liste[0]

                elif self.liste_color_territories[i] == "ROUGE":
                    liste = self.combined_list_values_12345[i]
                    self.score_b_red += liste[0]

            if self.score_a_blue > self.score_b_red:
                self.score_a_blue_win = True

            if self.score_a_blue < self.score_b_red:
                self.score_b_red_win = True

            print(f"\n    SCORE BLEU : {self.score_a_blue} / SCORE ROUGE : {self.score_b_red} \n")

        if self.tour_de_jeu == 6:
            for i in range(0, 5, 1):
                if self.liste_color_territories[i] == "BLEU":
                    liste = self.combined_list_values_12345[i]
                    self.score_a_blue += liste[1]

                if self.liste_color_territories[i] == "ROUGE":
                    liste = self.combined_list_values_12345[i]
                    self.score_b_red += liste[1]
            print(f"\n    SCORE BLEU : {self.score_a_blue} / SCORE ROUGE : {self.score_b_red} \n")

            if self.score_a_blue_win == True and self.score_a_blue > self.score_b_red:
                print(f"\n LES BLEUS REMPORTENT LA VICTOIRE !!!")
                self.end_game = True
                self.gagnant = "BLEU"

            if self.score_b_red_win == True and self.score_a_blue < self.score_b_red:
                print(f"\n LES ROUGES REMPORTENT LA VICTOIRE !!!")
                self.end_game = True
                self.gagnant = "ROUGE"

            else:
                self.score_a_blue_win = False
                self.score_b_red_win = False

        if self.tour_de_jeu == 9:
            for i in range(0, 5, 1):
                if self.liste_color_territories[i] == "BLEU":
                    liste = self.combined_list_values_12345[i]
                    self.score_a_blue += liste[2]
                elif self.liste_color_territories[i] == "ROUGE":
                    liste = self.combined_list_values_12345[i]
                    self.score_b_red += liste[2]
            print(f"\n    SCORE BLEU : {self.score_a_blue} / SCORE ROUGE : {self.score_b_red} \n")

            if self.score_a_blue > self.score_b_red:
                print(f"\n LES BLEUS REMPORTENT LA VICTOIRE !!!")
                self.end_game = True
                self.gagnant = "BLEU"

            elif self.score_a_blue < self.score_b_red:
                print(f"\n LES ROUGES REMPORTENT LA VICTOIRE !!!")
                self.end_game = True
                self.gagnant = "ROUGE"

            else:
                print(f"\n MATCH NUL...")
                self.end_game = True
                self.gagnant = "NUL"