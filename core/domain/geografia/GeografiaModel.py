

# GeografiaModel:

####################################

from pydantic import BaseModel

####################################

class ModeloGeografia(BaseModel):
    Pais: str |None = None
    Departamento: str |None = None
    Ciudad: str |None = None
    Resultado: str |None = None

####################################

