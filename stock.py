from random import randint


class Stock:
    def __init__(self):
        self.roquette = self.random()
        self.jambon = self.random()
        self.ananas = self.random()
        self.baseTomate = self.random()

    def random(self):
        return randint(5, 45)


