from pydantic import BaseModel
from typing import Optional

class TireCarte(BaseModel):
    nb_cartes : Optional[int] = 1
    card_id : Optional[str] = ""