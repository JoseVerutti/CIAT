from pydantic import BaseModel

from datetime import datetime
    

class Activities(BaseModel):
    id:str
    fecha : datetime
    tipo_de_actividad : str
    insumos : list[str]    
    duracion : int