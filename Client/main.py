import requests 
from utils.fonctions import countCards

### Lancement du webservice et génération d'un deck ###
url = "http://127.0.0.1:8000"
req = requests.get(url+"/creer-un-deck/")
deck = req.json()

print("Id du deck : " + deck["deck_id"])

### Demande à l'utilisateur combien de cartes il veut tirer ####
print("\n♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
nbCarte = input("Combien de cartes voulez vous tirer ? (1 est pris en défault) ")

if (int(nbCarte) > 52) :
    print("Vous avez entré un nombre trop grand, le paquet entier va être tiré \n")
try :
    parameters = {"card_id": deck["deck_id"],"nb_cartes" : int(nbCarte)}
except:
    parameters = {"card_id": deck["deck_id"],"nb_cartes" : 1}

req = requests.post(url+"/cartes", json=parameters)
drawn = req.json()

try: 
    cards = drawn["cards"]

    ### Affichage des résultats ###
    print("List of cards : \n")
    for card in cards: 
        print(card["value"]+" of "+ card["suit"])
    print("\n♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
    print("\nRésultats du comptage: \n")
    print(countCards(cards))

    print("\n♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
    print("\nBonne journée :) \n")
except: 
    print("Une erreur est survenue \n")
