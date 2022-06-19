from urllib import request
from stock import Stock
from function import *
import time
from flask import Flask, render_template, request
import json

app = Flask(__name__)


gamePlaying = True
score = 0
pizzaPrete = 0
pizzaFour = 0
timeout = 300
stock = Stock()
fourEnCours = False
#Gestion des actions du menu
@app.route("/")
def menu():
    return render_template('menu.html', timer=timeout)


@app.route("/menu/add-pizza")
def add_pizza():
    return render_template('add-pizza.html', timer=timeout)

@app.route("/menu/get-new-pizza", methods=['GET', 'POST'])
def get_new_pizza():
    global stock
    data = request.data
    dico_recup = json.loads(data)
    dico_nouveau = {}
    dico_nouveau["kind"] = dico_recup["pizza_name"]
    dico_nouveau["recette"] = dico_recup["pizza_receipt"]
    tab = []
    for i in range(len(dico_recup["pizza_ingredients"])):
        tab.append((dico_recup["pizza_ingredients"][i][0], dico_recup["pizza_ingredients"][i][1], dico_recup["pizza_ingredients"][i][2]))
    dico_nouveau["Ingrédients"] = tab
    stock.possiblePizzaDict[len(stock.possiblePizzaDict) + 1] = dico_nouveau

    return render_template('pizza.html', timer=timeout)

#Passe le stock en json
@app.route("/menu/get-stock")
def get_stock():
    global stock
    json_dump = json.dumps(stock.ingredientTab)
    return json_dump

#Vérifie que la recette est valide et possible
@app.route("/menu/check-stock", methods=['GET', 'POST'])
def check_stock():
    global stock
    global pizzaPrete
    data = request.data
    dico_recup = json.loads(data)
    success = recetteValide(dico_recup, stock)
    if success != False:
        success = checkStock(success, stock)
    else:
        success = 1
    ret = ""
    if pizzaPrete < 3:
        if success == 0:
            pizzaPrete += 1
            ret = affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Pizza ajoutée!")
        elif success == 1: 
            ret = affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "La recette est mauvaise...")
        elif success == 2:
            ret = affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Le stock ne permet pas cette recette.")
    else :
        ret = affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Pas plus de 3 pizzas à la fois")
    return ret

#Vérifie que la recette est valide et possible
@app.route("/menu/lancer-four", methods=['GET', 'POST'])
def lancer_four():
    global pizzaPrete
    global pizzaFour
    global fourEnCours
    if pizzaPrete > 0 and fourEnCours == False:
        print("ALOOOOOOOOOOOOOOOOOOOOOO")
        fourEnCours = True
        pizzaPrete = pizzaFour
        pizzaPrete = 0
        return affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Four lancé")
    return " " + affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Pas de pizza prête")

#Vérifie que la recette est valide et possible
@app.route("/menu/fin-four", methods=['GET', 'POST'])
def fin_four():
    global pizzaFour
    global fourEnCours
    global stock
    global score
    fourEnCours = False
    score = pizzaFour * 10
    if stock.ingredientTab["Base Tomate"] == 0:
        
        return game_over()
    return affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score, "Cuisson terminée")


#Gestion des actions du jeu
@app.route("/menu/pizza")
def pizza():
    global stock
    stock.createIngr()
    return render_template('pizza.html', text=affichageBase(stock.possiblePizzaDict, stock, pizzaPrete, score), timer=timeout)

@app.route("/menu/game-over")
def game_over():
    global stock
    global score
    score = EndOfGame(score, stock)
    return render_template('final.html', score=score)


# while gamePlaying and int(time.time()) - timeInGame < timeout:
#     print("Temps écoulé : " + str(int(time.time()) - timeInGame) + " / " +str(timeout))
#     affichageBase(possiblePizzaDict, stock, pizzaPrete, score)
#     gamePlaying, pizzaPrete, score = choixTypePizzaEtReductionStock(stock, possiblePizzaDict, pizzaPrete, score)
# EndOfGame(score, stock)




