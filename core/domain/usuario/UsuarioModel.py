

# UsuarioModel:

####################################

from pydantic import BaseModel

####################################

class ModeloUsuario(BaseModel):
    NombreComprador: str |None = None
    ApellidoComprador: int |None = None
    DocumentoComprador: str |None = None
    DireccionComprador: str |None = None
    EmailComprador: str |None = None
    TelefonoComprador: str |None = None
    GeneroComprador: str |None = None


####################################