import os


def affichageBase(possiblePizza:  dict, stock):
    os.system('clear')

    for key, value in stock.ingredientTab.items():
        if value == 0:
            continue
        print("Il reste " + str(value) + " " + key)

    for key, value in possiblePizza.items():
        print(str(key) + " - " + value["kind"] + " (" + value["recette"] + ")")


def checkStock(typePizza, stock):
    if typePizza == 1:
        if stock.ingredientTab["Jambon"] > 2 and stock.ingredientTab["Ananas"] > 2 and stock.ingredientTab["Base Tomate"] > 0:
            return True
    if typePizza == 2:
        if stock.ingredientTab["Lamelle de roquette"] > 6 and stock.ingredientTab["Base Tomate"] > 0:
            return True
    return False



