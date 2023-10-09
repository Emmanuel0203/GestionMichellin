

# UsuarioModel:

####################################

from pydantic import BaseModel

####################################

class ModeloUsuario(BaseModel):
    Comprador: str |None = None
    Genero: str |None = None
    Resultado: str |None = None

####################################