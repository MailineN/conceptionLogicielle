from fastapi import FastAPI
from pydantic import BaseModel
from utils.functions import *
from utils.tireCarteBaseModel import TireCarte

#### Définition d'un webservice utilisant FastApi ####
app = FastAPI()

#### Message de la racine ####
@app.get("/")
async def root():
    return {"message": "Miam Miam le chocolat"}

#### Création d'un deck sur creer un deck ####
@app.get("/creer-un-deck/")
async def get_id(): 
    r = getNewDeckID("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    return {"deck_id" : r}

### Tirage de cartes sur cartes ###
@app.post("/cartes")
def draw(nb : TireCarte):
    res = DrawCards(nb.card_id,nb.nb_cartes)
    return(res)
