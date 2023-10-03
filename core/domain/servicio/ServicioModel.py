

# ServicioModel:

####################################

from pydantic import BaseModel

####################################

class ModeloServicio(BaseModel):
    Producto: str |None = None
    DetalleProducto: int |None = None
    TipoProducto: str |None = None

####################################