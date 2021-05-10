from fastapi import FastAPI
from pydantic import BaseModel
import http3
from utils.functions import *
from utils.tireCarteBaseModel import TireCarte

app = FastAPI()


client = http3.AsyncClient()

async def call_deck(url: str):

    r = await client.get(url)
    return r.text

@app.get("/")
async def root():
    return {"message": "Miam Miam le chocolat"}


@app.get("/creer-un-deck/")
async def get_id(): 
    r = getNewDeckID("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    return {"deck_id" : r}

@app.post("/cartes")
def draw(nb : TireCarte):
    res = DrawCards(nb.nb_cartes)
    return(res)
