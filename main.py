from stock import Stock
from function import *
import time
from flask import Flask, render_template

app = Flask(__name__)





# cls()
gamePlaying = True
score = 0
pizzaPrete = 0
pizzaFour = 0
timeout = 300
possiblePizzaDict = {1: {"kind": "hawaïenne", "recette": "base tomate, 3 morceaux de jambon, 3 morceaux d’ananas", "nbJambon": (3, False), "nbAnanas": (3, False)}, 
2: {"kind": "rucola", "recette": "base tomate, 7 lamelles de roquette. La roquette doit être ajoutée après cuisson", "nbRoquette": (7, True)}}
stock = Stock()
stock.createIngr()

#Gestion des actions du menu
@app.route("/menu")
def menu():
    return render_template('menu.html', text="Caca", timer=timeout)


@app.route("/menu/add-pizza")
def add_pizza():
    return render_template('add-pizza.html', text="Caca", timer=timeout)


#Gestion des actions du jeu
print(affichageBase(possiblePizzaDict, stock, pizzaPrete, score))
@app.route("/pizza")
def pizza():
    return render_template('pizza.html', text=affichageBase(possiblePizzaDict, stock, pizzaPrete, score), timer=timeout)

#print("Bienvenue dans l'application pizza! Miam!")

# while gamePlaying and int(time.time()) - timeInGame < timeout:
#     print("Temps écoulé : " + str(int(time.time()) - timeInGame) + " / " +str(timeout))
#     affichageBase(possiblePizzaDict, stock, pizzaPrete, score)
#     gamePlaying, pizzaPrete, score = choixTypePizzaEtReductionStock(stock, possiblePizzaDict, pizzaPrete, score)
# EndOfGame(score, stock)




