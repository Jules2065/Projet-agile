import argparse
from glob import glob
import os
import time
from turtle import screensize, st


def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    print(sorted(list_1))
    print(sorted(list_2))
    return sorted(list_1) == sorted(list_2)


def affichageBase(possiblePizza: dict, stock, pizzaPrete, score, annexe: str = ""):
    ret = ''
    for key, value in stock.ingredientTab.items():
        if value == 0:
            continue
        ret += 'Il reste ' + str(value) + ' ' + key + '<br>'

    for key, value in possiblePizza.items():
        ret += str(key) + ' - ' + value["kind"] + \
            ' (' + value["recette"] +'<br>'
    ret += 'Pizza prête à la cuisson : ' + str(pizzaPrete) +'<br>'
    ret += 'Score actuel :' + str(score) +'<br>'
    ret += annexe
    return ret



def recetteValide(tab, stock):
    arr = []
    contient = []
    for i in range(len(tab["pizza_ingredients"])):
        if tab["pizza_ingredients"][i][0] not in contient:
            tab["pizza_ingredients"][i][1] = int(tab["pizza_ingredients"][i][1])
            arr.append(tuple(tab["pizza_ingredients"][i]))
            contient.append(tab["pizza_ingredients"][i][0])
        else:
            for j in range(len(arr)):
                if arr[j][0] == tab["pizza_ingredients"][i][0]:
                    tempo = list(arr[j])
                    tempo[1] = arr[j][1] + int(tab["pizza_ingredients"][i][1])
                    arr = tuple(tempo)
    
    
    for k in range (len(stock.possiblePizzaDict)):
        if check_if_equal(arr, stock.possiblePizzaDict[k+1]["Ingrédients"]):
            return (k+1)
    return False
def checkStock(typePizza, stock):
    typePizza = int(typePizza)

    for sto in stock.possiblePizzaDict[typePizza]["Ingrédients"]:
        if stock.ingredientTab[sto[0]] < int(sto[1]):
            return 2
    stock.ingredientTab["Base Tomate"] -= 1
    for sto in stock.possiblePizzaDict[typePizza]["Ingrédients"]:
        stock.ingredientTab[sto[0]] -= int(sto[1])
    
    return 0









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
    return score
