

# ServicioModel:

####################################

from pydantic import BaseModel

####################################

class ModeloServicio(BaseModel):
    CodigoProducto: str |None = None
    PrecioProducto: int |None = None
    NombreProducto: str |None = None
    MarcaProducto: str |None = None
    DocumentoConductor: str |None = None
    DescripcionProducto: str |None = None


####################################