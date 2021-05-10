import requests 
from utils.fonctions import countCards

url = "http://127.0.0.1:8000"
req = requests.get(url+"/creer-un-deck/")
deck = req.json()

print(deck["deck_id"])

nbCarte = input("Combien de cartes voulez vous tirer ? (1 est pris en défault) ")

try :
    parameters = {"card_id": deck["deck_id"],"nb_cartes" : int(nbCarte)}
except:
    parameters = {"card_id": deck["deck_id"],"nb_cartes" : 1}

req = requests.post(url+"/cartes", json=parameters)
drawn = req.json()

cards = drawn["cards"]
print(cards)
print(countCards(cards))

