import random


class Zoneplay:

    def __init__(self):
        self.listvalue1 = []
        self.listvalue2 = []
        self.listvalue3 = []
        self.listvalue4 = []
        self.listvalue5 = []

    def random_zone_value(self):
        self.listvalue1 = random.sample([1, 2, 3], 3)
        self.listvalue2 = random.sample([1, 2, 3], 3)
        self.listvalue3 = random.sample([1, 2, 3], 3)
        self.listvalue4 = random.sample([1, 2, 3], 3)
        self.listvalue5 = random.sample([1, 2, 3], 3)
