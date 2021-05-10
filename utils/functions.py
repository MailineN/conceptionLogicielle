import requests 

def getNewDeckID(url): 
    r = requests.get(url)
    json = r.json()
    return(json["deck_id"])

