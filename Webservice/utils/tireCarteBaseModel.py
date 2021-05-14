from pydantic import BaseModel
from typing import Optional

### Corps métier du webservice ###
class TireCarte(BaseModel):
    nb_cartes : Optional[int] = 1
    card_id : Optional[str] = ""