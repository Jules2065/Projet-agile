from glob import glob
import os
import time
from turtle import screensize


def affichageBase(possiblePizza: dict, stock, pizzaPrete, score):
    ret = ''
    for key, value in stock.ingredientTab.items():
        if value == 0:
            continue
        ret += 'Il reste ' + str(value) + ' ' + key + '<br>'

    for key, value in possiblePizza.items():
        ret += str(key) + ' - ' + value["kind"] + \
            ' (' + value["recette"] +'<br>'
    ret += '10 - mettre les pizzas au four<br>'
    ret += 'Pizza prête à la cuisson : ' + str(pizzaPrete) +'<br>'
    ret += 'Score actuel :' + str(score)
    return ret

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


def choixTypePizzaEtReductionStock(stock, possiblePizzaDict, pizzaPrete, score):
    nbrRucola = 0
    ret = True
    typePizza = int(input("Veuillez choisir un type de pizza : "))
    cls()
    if 0 < int(typePizza) < 3:
        if checkStock(typePizza, stock):
            if pizzaPrete < 3:
                if typePizza == 1:
                    stock.ingredientTab["Jambon"] -= possiblePizzaDict[1]["nbJambon"]
                    stock.ingredientTab["Ananas"] -= possiblePizzaDict[1]["nbAnanas"]
                    stock.ingredientTab["Base Tomate"] -= 1
                if typePizza == 2:
                    nbrRucola += 1
                    stock.ingredientTab["Base Tomate"] -= 1
                pizzaPrete += 1
            else:
                print("Pas plus de trois pizza à la fois, veuillez les mettre au four")
        else:
            print("Pas assez d'ingrédient pour cette pizza")
            ret = False
    elif int(typePizza) == 10:
        if pizzaPrete > 0:
            print("Cuisson lancée pendant 30 secondes")
            for i in range(30):
                print("Temps de cuisson écoulé : " + str(i) + " secondes")
                time.sleep(1)
                cls()
            for i in range (nbrRucola):
                stock.ingredientTab["Lamelle de roquette"] -= possiblePizzaDict[1]["nbRoquette"]
            score += pizzaPrete * 10
            pizzaPrete = 0
        else:
            print("Pas de pizza à cuire")

    return ret, pizzaPrete, score

def EndOfGame(score, stock):
    print("Jeu fini")
    print("Score de base : " + str(score))

    for key, value in stock.ingredientTab.items():
        print("Key : " + str(key))
        print("Value : " + str(value))
        if key == "Base Tomate":
            score -= value * 4
        else:
            score -= value
    print("Score final : " + str(score))
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
