from random import randint


def randomNumberIngredient():
    return randint(5, 45)


class Stock:
    def __init__(self):
        self.ingredientTab = {"Jambon": randomNumberIngredient(), "Ananas": randomNumberIngredient(), "Base Tomate": randomNumberIngredient(), "Lamelle de roquette": randomNumberIngredient()}




