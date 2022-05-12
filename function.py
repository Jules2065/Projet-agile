import os


def affichageBase(possiblePizza: dict, stock):
    os.system('clear' or 'clr')

    for key, value in stock.ingredientTab.items():
        if value == 0:
            continue
        print("Il reste " + str(value) + " " + key)

    for key, value in possiblePizza.items():
        print(str(key) + " - " + value["kind"] + " (" + value["recette"] + ")")


def checkStock(typePizza, stock):
    typePizza = int(typePizza)
    if typePizza == 1:
        if stock.ingredientTab["Jambon"] > 2 and stock.ingredientTab["Ananas"] > 2 and stock.ingredientTab[
            "Base Tomate"] > 0:
            return True
    if typePizza == 2:
        if stock.ingredientTab["Lamelle de roquette"] > 6 and stock.ingredientTab["Base Tomate"] > 0:
            return True
    return False


def choixTypePizzaEtReductionStock(stock, possiblePizzaDict):
    typePizza = int(input("Veuillez choisir un type de pizza : "))
    if 0 < int(typePizza) < 3:
        if checkStock(typePizza, stock):
            if typePizza == 1:
                stock.ingredientTab["Jambon"] -= possiblePizzaDict[1]["nbJambon"]
                stock.ingredientTab["Ananas"] -= possiblePizzaDict[1]["nbAnanas"]
                stock.ingredientTab["Base Tomate"] -= 1
            if typePizza == 2:
                stock.ingredientTab["Lamelle de roquette"] -= possiblePizzaDict[2]["nbRoquette"]
                stock.ingredientTab["Base Tomate"] -= 1
        else:
            print("Pas assez d'ingrédient pour cette pizza")

