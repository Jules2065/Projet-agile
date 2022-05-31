from stock import Stock
from function import *
import time

cls()
gamePlaying = True
score = 0
pizzaPrete = 0
pizzaFour = 0
timeInGame = int(time.time())
timeout = 300
possiblePizzaDict = {1: {"kind": "hawaïenne", "recette": "base tomate, 3 morceaux de jambon, 3 morceaux d’ananas", "nbJambon": 3, "nbAnanas": 3}, 2: {
    "kind": "rucola", "recette": "base tomate, 7 lamelles de roquette. La roquette doit être ajoutée après cuisson", "nbRoquette": 7}}
stock = Stock()
stock.createIngr()


print("Bienvenue dans l'application pizza! Miam!")

while gamePlaying and int(time.time()) - timeInGame < timeout:
    print("Temps écoulé : " + str(int(time.time()) - timeInGame) + " / " +str(timeout))
    affichageBase(possiblePizzaDict, stock, pizzaPrete, score)
    gamePlaying, pizzaPrete, score = choixTypePizzaEtReductionStock(stock, possiblePizzaDict, pizzaPrete, score)
EndOfGame(score, stock)




