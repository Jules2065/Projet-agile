from random import randint

def randomNumberIngredient():
    return randint(10, 45)




nbrPate = 0

class Stock:
    def __init__(self):
        self.ingredientTab = {"Base Tomate": nbrPate}
        self.possiblePizzaDict = {1: {"kind": "hawaïenne", "recette": "base tomate, 3 morceaux de jambon, 3 morceaux d’ananas", "Ingrédients": [("Jambon", 3, False), ("Ananas", 3, False)]}, 
        2: {"kind": "rucola", "recette": "base tomate, 7 lamelles de roquette. La roquette doit être ajoutée après cuisson", "Ingrédients":  [("Roquette", 7, True)]}}
    def randomNumberPate(self):
        return randint(5, 10)
    
    def createIngr(self):
        nbrPate = self.randomNumberPate()
        self.ingredientTab["Base Tomate"] =  nbrPate
        for i in range(len(self.possiblePizzaDict)):
            for pizza in self.possiblePizzaDict[i+1]["Ingrédients"]:
                self.ingredientTab[pizza[0]] = 0

        for i in range(nbrPate):
            val = randint(1, len(self.possiblePizzaDict))
            for ingre in self.possiblePizzaDict[val]["Ingrédients"]:
                self.ingredientTab[ingre[0]] += int(ingre[1])
                
        
    
