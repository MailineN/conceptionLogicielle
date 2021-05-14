import requests 

### Fonction de récupération de l'Id ###
def getNewDeckID(url): 
    r = requests.get(url)
    json = r.json()
    return(json["deck_id"])

### Fonction de tirage de cartes ###
def DrawCards(deck_id,nb_cartes):
    
    if deck_id == "" : 
        r = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        deck = r.json()
        deck_id = deck["deck_id"]

    req = requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count="+str(nb_cartes))
    if (req.status_code == 200) or (req.status_code == 201):
        json = req.json()
        res = {"deck_id": json["deck_id"], "cards": json["cards"]}
        return(res)
    # If error in json marche aussi pour détecter les erreurs
    else : 
        return {"deck_id": deck_id, "error": req.status_code}
