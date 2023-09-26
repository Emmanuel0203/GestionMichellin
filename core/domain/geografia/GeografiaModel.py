

# GeografiaModel:

####################################

from pydantic import BaseModel

####################################

class Geografia(BaseModel):
    Pais: str |None = None
    Departamento: str |None = None
    Ciudad: str |None = None

####################################

