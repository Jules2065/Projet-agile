import os


def affichageBase(possiblePizza:  dict, stock):
    os.system('clear')
    for key, value in possiblePizza.items():
        print("Pour la pizza " + value + " entrer le nombre", key)
