import random


class Zoneplay:

    def __init__(self) -> None:
        self.listvalue1: list[int] = []
        self.listvalue2: list[int] = []
        self.listvalue3: list[int] = []
        self.listvalue4: list[int] = []
        self.listvalue5: list[int] = []

    def random_zone_value(self):
        self.listvalue1 = random.sample([1, 2, 3], 3)
        self.listvalue2 = random.sample([1, 2, 3], 3)
        self.listvalue3 = random.sample([1, 2, 3], 3)
        self.listvalue4 = random.sample([1, 2, 3], 3)
        self.listvalue5 = random.sample([1, 2, 3], 3)
