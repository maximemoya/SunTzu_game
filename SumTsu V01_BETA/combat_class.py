import random


class Combat(object):

    # systeme de carte possée sur le terrain, on va simuler le combat avec des valeurs aléatoires prises dans listA et listB

    def __init__(self, liste_de_combat_a=[0, 0, 0, 0, 0], liste_unite_terrain_a=[0, 0, 0, 0, 0],
                 liste_de_combat_b=[0, 0, 0, 0, 0], liste_unite_terrain_b=[0, 0, 0, 0, 0]):
        self.debut_jeu = True

        self.inventaire_A = []
        self.inventaire_B = []

        self.liste_de_combatA = liste_de_combat_a
        self.liste_de_combatB = liste_de_combat_b

        self.liste_unite_terrain_a = liste_unite_terrain_a
        self.liste_unite_terrain_b = liste_unite_terrain_b

    def remplir_inventaire(self):

        print("\nREMPLISSAGE INVENTAIRE . . .\n")

        if self.debut_jeu:
            # charge l'inventaire de 10 cartes valeur de 1 à 10 :
            for i in range(1, 16, 1):
                self.inventaire_A.append(i)
                self.inventaire_B.append(i)
            self.debut_jeu = False

        for i in range(0, 15, 1):
            self.inventaire_A.pop(i)
            self.inventaire_A.insert(i, i + 1)
            self.inventaire_B.pop(i)
            self.inventaire_B.insert(i, i + 1)

        random.shuffle(self.inventaire_A)
        random.shuffle(self.inventaire_B)

        # print(f"INVENTAIRE DE A :{self.inventaire_A}")
        # print(f"INVENTAIRE DE B :{self.inventaire_B}")

        for j in range(0, 5, 1):
            self.liste_de_combatA.pop(j)
            self.liste_de_combatA.insert(j, self.inventaire_A[j])
            self.liste_de_combatB.pop(j)
            self.liste_de_combatB.insert(j, self.inventaire_B[j])

        print(f"VALEURS DE COMBAT A :{self.liste_de_combatA}")
        print(f"VALEURS DE COMBAT B :{self.liste_de_combatB}")

        self.inventaire_A.sort()
        self.inventaire_B.sort()

        # print(f"INVENTAIRE DE A : {self.inventaire_A}")
        # print(f"INVENTAIRE DE B : {self.inventaire_B}")

    def combattre(self):
        result_combat = int(0)

        # Combat carte A vs B pour chacun des 5 territoires :
        for i in range(0, 5, 1):

            # SI A ET B utilisent des cartes de valeurs de 1 à 10 :
            if self.liste_de_combatA[i] <= self.liste_de_combatB[i] <= 10 or self.liste_de_combatB[i] <= \
                    self.liste_de_combatA[i] <= 10:

                print(f"\nCOMBAT pour le territoire {i + 1} :\n\n  "
                      f"    Troupe A : {self.liste_de_combatA[i]} + {self.liste_unite_terrain_a[i]} deja présent sur terrain"
                      f" VS Troupe B : {self.liste_de_combatB[i]} + {self.liste_unite_terrain_b[i]} deja présent sur terrain")

                total_troupe_a = self.liste_de_combatA[i] + self.liste_unite_terrain_a[i]
                total_troupe_b = self.liste_de_combatB[i] + self.liste_unite_terrain_b[i]

                print(f"\n          TOTAL :\n"
                      f"\n              Troupe A : {total_troupe_a} VS Troupe B : {total_troupe_b}")

                if total_troupe_a < total_troupe_b:
                    # B GAGNE
                    result_combat = total_troupe_b - total_troupe_a

                    if result_combat == 1:
                        print(f"\n              <( {total_troupe_b} - {total_troupe_a} = {result_combat} )>\n"
                              f"\n              B GAGNE le territoire {i + 1} et place {result_combat} troupe")
                    else:
                        print(f"\n              <( {total_troupe_b} - {total_troupe_a} = {result_combat} )>\n"
                              f"\n              B GAGNE le territoire {i + 1} et place {result_combat} troupes")

                    self.liste_unite_terrain_a.pop(i)
                    self.liste_unite_terrain_a.insert(i, 0)
                    self.liste_unite_terrain_b.pop(i)
                    self.liste_unite_terrain_b.insert(i, result_combat)

                if total_troupe_b < total_troupe_a:
                    # A GAGNE
                    result_combat = total_troupe_a - total_troupe_b

                    if result_combat == 1:
                        print(f"\n              <( {total_troupe_a} - {total_troupe_b} = {result_combat} )>\n"
                              f"\n              A GAGNE le territoire {i + 1} et place {result_combat} troupe")
                    else:
                        print(f"\n              <( {total_troupe_a} - {total_troupe_b} = {result_combat} )>\n"
                              f"\n              A GAGNE le territoire {i + 1} et place {result_combat} troupes")

                    self.liste_unite_terrain_a.pop(i)
                    self.liste_unite_terrain_a.insert(i, result_combat)
                    self.liste_unite_terrain_b.pop(i)
                    self.liste_unite_terrain_b.insert(i, 0)

                if total_troupe_b == total_troupe_a:
                    print(f"\n                  <( {total_troupe_a} - {total_troupe_b} = {result_combat} )>\n"
                          f"\n                  PAS DE GAGNANT ! le territoire {i + 1} est NEUTRE !")

                    self.liste_unite_terrain_a.pop(i)
                    self.liste_unite_terrain_a.insert(i, 0)
                    self.liste_unite_terrain_b.pop(i)
                    self.liste_unite_terrain_b.insert(i, 0)

            # SI A utilise carte (+1)
            if self.liste_de_combatA[i] == 11:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                # Si carte (-1) var_plus_1_ou_2 = -1
                var_plus_1_ou_2 = 1

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 0
                var_a_ou_b = ["A", "B"]

                # SI A utilise (+1) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatB[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if self.liste_unite_terrain_b[i] >= var_plus_1_ou_2:
                        result_combat = self.liste_unite_terrain_b[i] - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if self.liste_unite_terrain_b[i] < var_plus_1_ou_2:
                        result_combat = var_plus_1_ou_2 + self.liste_unite_terrain_a[i] - self.liste_unite_terrain_b[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+1) contre B qui utilise (+1)
                if self.liste_de_combatB[i] == 11:

                    result_combat = self.liste_unite_terrain_b[i] + 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+1) contre B qui utilise (+2)
                if self.liste_de_combatB[i] == 12:

                    result_combat = self.liste_unite_terrain_b[i] + 2 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+1) contre B qui utilise (-1)
                if self.liste_de_combatB[i] == 13:

                    result_combat = self.liste_unite_terrain_b[i] - 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"      -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        {var_plus_1_ou_2} + 1 unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+1) contre B qui utilise (50/50)
                if self.liste_de_combatB[i] >= 14:

                    result_combat = self.liste_unite_terrain_b[i] - (
                            var_plus_1_ou_2 - 1 + self.liste_unite_terrain_a[i] // 2)

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI A utilise carte (+2)
            if self.liste_de_combatA[i] == 12:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                # Si carte (-1) var_plus_1_ou_2 = -1
                var_plus_1_ou_2 = 2

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 0
                var_a_ou_b = ["A", "B"]

                # SI A utilise (+2) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatB[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if self.liste_unite_terrain_b[i] >= var_plus_1_ou_2:
                        result_combat = self.liste_unite_terrain_b[i] - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if self.liste_unite_terrain_b[i] < var_plus_1_ou_2:
                        result_combat = var_plus_1_ou_2 + self.liste_unite_terrain_a[i] - self.liste_unite_terrain_b[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+2) contre B qui utilise (+1)
                if self.liste_de_combatB[i] == 11:

                    result_combat = self.liste_unite_terrain_b[i] + 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+2) contre B qui utilise (+2)
                if self.liste_de_combatB[i] == 12:

                    result_combat = self.liste_unite_terrain_b[i] + 2 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+2) contre B qui utilise (-1)
                if self.liste_de_combatB[i] == 13:

                    result_combat = self.liste_unite_terrain_b[i] - 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"      -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        {var_plus_1_ou_2} + 1 unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (+2) contre B qui utilise (50/50)
                if self.liste_de_combatB[i] >= 14:

                    result_combat = self.liste_unite_terrain_b[i] - (
                            var_plus_1_ou_2 - 1 + self.liste_unite_terrain_a[i] // 2)

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} / 2 = {var_plus_1_ou_2 - 1} unites {var_a_ou_b[var_index]} "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI A utilise carte (-1)
            if self.liste_de_combatA[i] == 13:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                # Si carte (-1) var_plus_1_ou_2 = -1
                var_plus_1_ou_2 = -1

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 0
                var_a_ou_b = ["A", "B"]

                # SI A utilise (-1) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatB[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    result_combat = self.liste_unite_terrain_b[i] - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} + 1 = {self.liste_de_combatB[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # NEUTRE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} + 1 = {self.liste_de_combatB[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} + 1 = {self.liste_de_combatB[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (-1) contre B qui utilise (+1)
                if self.liste_de_combatB[i] == 11:

                    result_combat = self.liste_unite_terrain_b[i] + 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain +  1 unite {var_a_ou_b[var_index - 1]}"
                            f" = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (-1) contre B qui utilise (+2)
                if self.liste_de_combatB[i] == 12:

                    result_combat = self.liste_unite_terrain_b[i] + 2 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain +  1 unite {var_a_ou_b[var_index - 1]}"
                            f" = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (-1) contre B qui utilise (-1)
                if self.liste_de_combatB[i] == 13:

                    result_combat = self.liste_unite_terrain_b[i] - 1 - var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"      -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        -1 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        {var_plus_1_ou_2} + 1 unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (-1) contre B qui utilise (50/50)
                if self.liste_de_combatB[i] >= 14:

                    result_combat = self.liste_unite_terrain_b[i] - (self.liste_unite_terrain_a[i] // 2)

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain "
                            f"- {self.liste_unite_terrain_a[i]} / 2 = {self.liste_unite_terrain_a[i] // 2} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]}"
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI A utilise carte (50/50)
            if self.liste_de_combatA[i] >= 14:

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 0
                var_a_ou_b = ["A", "B"]

                # SI A utilise (50/50) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatB[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    result_combat = (self.liste_unite_terrain_b[i] + self.liste_de_combatB[i]) // 2 - \
                                    self.liste_unite_terrain_a[i]

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_b[i] + self.liste_de_combatB[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unites {var_a_ou_b[var_index - 1]} restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # NEUTRE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_b[i] + self.liste_de_combatB[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unite restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatB[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_b[i] + self.liste_de_combatB[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unites {var_a_ou_b[var_index]} restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (50/50) contre B qui utilise (+1)
                if self.liste_de_combatB[i] == 11:

                    result_combat = (self.liste_unite_terrain_b[i] + 1) // 2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        (1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        (1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+1) donne :\n "
                            f"        (1 unite {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (50/50) contre B qui utilise (+2)
                if self.liste_de_combatB[i] == 12:

                    result_combat = (self.liste_unite_terrain_b[i] + 2) // 2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        (2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        (2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (+2) donne :\n "
                            f"        (2 unites {var_a_ou_b[var_index - 1]} + {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (50/50) contre B qui utilise (-1)
                if self.liste_de_combatB[i] == 13:

                    result_combat = (self.liste_unite_terrain_b[i] - 1) // 2 - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - 1 unite {var_a_ou_b[var_index - 1]}) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - 1 unite {var_a_ou_b[var_index - 1]}) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unite "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (-1) donne :\n "
                            f"        ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain - 1 unite {var_a_ou_b[var_index - 1]}) / 2 - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                # SI A utilise (50/50) contre B qui utilise (50/50)
                if self.liste_de_combatB[i] >= 14:

                    result_combat = self.liste_unite_terrain_b[i] - self.liste_unite_terrain_a[i]

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if result_combat > 0:
                        # B GAGNE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      ({self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index - 1]} "
                            f"deja présent sur terrain) / 2  = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # MATCH NUL
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      {result_combat} unite sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat < 0:
                        # A GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte (50/50) donne :\n "
                            f"      ({self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index]} "
                            f"deja présent sur terrain) / 2  = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                        # AJOUTER B ...

            # ------------- PARTIE B ----------------------------------------------------------------------------------------------

            # SI B utilise carte (+1)
            if self.liste_de_combatB[i] == 11:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                var_plus_1_ou_2 = 1

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 1
                var_a_ou_b = ["A", "B"]

                # SI B utilise (+1) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatA[i] <= 10:

                    # B GAGNE
                    if self.liste_unite_terrain_a[i] <= var_plus_1_ou_2:
                        result_combat = self.liste_unite_terrain_b[i] + var_plus_1_ou_2 - self.liste_unite_terrain_a[i]

                        print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    # A GAGNE
                    if self.liste_unite_terrain_a[i] > var_plus_1_ou_2:
                        result_combat = self.liste_unite_terrain_a[i] - var_plus_1_ou_2

                        print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI B utilise carte (+2)
            if self.liste_de_combatB[i] == 12:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                # Si carte (-1) var_plus_1_ou_2 = -1
                var_plus_1_ou_2 = 2

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 1
                var_a_ou_b = ["A", "B"]

                # SI B utilise (+2) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatA[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    if self.liste_unite_terrain_a[i] <= var_plus_1_ou_2:
                        result_combat = var_plus_1_ou_2 + self.liste_unite_terrain_b[i] - self.liste_unite_terrain_a[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if self.liste_unite_terrain_a[i] > var_plus_1_ou_2:
                        result_combat = self.liste_unite_terrain_a[i] - var_plus_1_ou_2 - self.liste_unite_terrain_b[i]

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (+{var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatB[i]}) donne :\n "
                            f"        {var_plus_1_ou_2} unites {var_a_ou_b[var_index]} + {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain  - {self.liste_unite_terrain_a[i]} "
                            f"unites {var_a_ou_b[var_index - 1]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI B utilise carte (-1)
            if self.liste_de_combatB[i] == 13:

                # Si carte (+1) var_plus_1_ou_2 = 1
                # Si carte (+2) var_plus_1_ou_2 = 2
                # Si carte (-1) var_plus_1_ou_2 = -1
                var_plus_1_ou_2 = -1

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 1
                var_a_ou_b = ["A", "B"]

                # SI B utilise (-1) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatA[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    result_combat = self.liste_unite_terrain_a[i] - var_plus_1_ou_2 - self.liste_unite_terrain_b[i]

                    if result_combat < 0:
                        # B GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} + 1 = {self.liste_de_combatA[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # NEUTRE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} + 1 = {self.liste_de_combatA[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites "
                            f"restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat > 0:
                        # A GAGNE :

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte ({var_plus_1_ou_2}) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      {self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} + 1 = {self.liste_de_combatA[i] + 1} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} "
                            f"unites {var_a_ou_b[var_index]} deja présent sur terrain = {result_combat} unites {var_a_ou_b[var_index - 1]} "
                            f"restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

            # SI B utilise carte (50/50)
            if self.liste_de_combatB[i] >= 14:

                # Si A utilise cette carte alors var_index = 0
                # Si B utilise cette carte alors var_index = 1
                var_index = 1
                var_a_ou_b = ["A", "B"]

                # SI B utilise (50/50) contre cartes valeur de 1 à 10 :
                if self.liste_de_combatA[i] <= 10:

                    print(f"\nCOMBAT pour le territoire {i + 1} :\n")

                    result_combat = (self.liste_unite_terrain_a[i] + self.liste_de_combatA[i]) // 2 - \
                                    self.liste_unite_terrain_b[i]

                    if result_combat < 0:
                        # B GAGNE :
                        result_combat *= -1

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_a[i] + self.liste_de_combatA[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unites {var_a_ou_b[var_index]} restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, result_combat)

                    if result_combat == 0:
                        # NEUTRE :
                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_a[i] + self.liste_de_combatA[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unite restante sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, 0)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

                    if result_combat > 0:
                        # A GAGNE :

                        print(
                            f" '{var_a_ou_b[var_index]}' utilise carte (50/50) contre '{var_a_ou_b[var_index - 1]}' qui utilise carte ({self.liste_de_combatA[i]}) donne :\n "
                            f"      ({self.liste_unite_terrain_a[i]} unites {var_a_ou_b[var_index - 1]} deja présent sur terrain + "
                            f"{self.liste_de_combatA[i]} unite(s) en renfort)/2 = {(self.liste_unite_terrain_a[i] + self.liste_de_combatA[i]) // 2} unites {var_a_ou_b[var_index - 1]} "
                            f"- {self.liste_unite_terrain_b[i]} unites {var_a_ou_b[var_index]} deja présent sur terrain ="
                            f" {result_combat} unites {var_a_ou_b[var_index - 1]} restantes sur terrain n°{i + 1}")

                        self.liste_unite_terrain_a.pop(i)
                        self.liste_unite_terrain_a.insert(i, result_combat)
                        self.liste_unite_terrain_b.pop(i)
                        self.liste_unite_terrain_b.insert(i, 0)

        print(f"\nRESULTATS :\n\n UNITE A sur les terrains de (1 à 5) :{self.liste_unite_terrain_a}\n")
        print(f" UNITE B sur les terrains de (1 à 5) :{self.liste_unite_terrain_b}\n")


"""
test = Combat()

for i in range(0, 100, 1):
    test.remplir_inventaire()
    test.combattre()
"""
