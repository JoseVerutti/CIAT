from pydantic import BaseModel
from schemas.activities import Activities
from schemas.parcelas import Parcelas

class User(BaseModel):

    nombre: str
    id:str
    correo:str
    contraseña:str
    parcelas : list[Parcelas]
    actividades : list[Activities]