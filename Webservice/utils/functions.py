import requests 

def getNewDeckID(url): 
    r = requests.get(url)
    json = r.json()
    return(json["deck_id"])


def DrawCards(nb_cartes):
    
    r = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    deck = r.json()
    deck_id = deck["deck_id"]

    req = requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count="+str(nb_cartes))
    json = req.json()
    res = {"deck_id": json["deck_id"], "cards": json["cards"]}
    return(res)