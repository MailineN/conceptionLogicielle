
def countCards(cards):
    rep = {"SPADES":0,"DIAMONDS":0,"CLUBS":0,"HEARTS":0}
    for c in cards : 
        rep[c["suit"]] += 1
    
    return rep
