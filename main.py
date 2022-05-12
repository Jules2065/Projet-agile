from stock import Stock
from function import *

possiblePizzaDict = {1: {"kind": "hawaïenne", "recette": "base tomate, 3 morceaux de jambon, 3 morceaux d’ananas", "nbJambon" : 3, "nbAnanas": 3}, 2:{"kind": "rucola", "recette": "base tomate, 7 lamelles de roquette. La roquette doit être ajoutée après cuisson", "nbRoquette" : 7}}
stock = Stock()
affichageBase(possiblePizzaDict, stock)





