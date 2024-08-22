from pydantic import BaseModel
from decimal import Decimal


class Parcelas(BaseModel):
    id:str
    latitud : Decimal
    longitud : Decimal
    tamaño: Decimal
    tipo_Cultivo : str