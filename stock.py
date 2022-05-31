from random import randint


def randomNumberIngredient():
    return randint(10, 45)


def randomNumberPate():
    return randint(5, 10)

nbrPate = randomNumberPate()




class Stock:
    def __init__(self):
        self.ingredientTab = {"Jambon": 0, "Ananas": 0
        , "Lamelle de roquette": 0, "Base Tomate": nbrPate}

    def createIngr(self):
        for i in range(nbrPate):
            val = randint(1, 2)
            if (val == 1):
                self.ingredientTab["Jambon"] += 3
                self.ingredientTab["Ananas"] += 3
            else:
                self.ingredientTab["Lamelle de roquette"] += 7
