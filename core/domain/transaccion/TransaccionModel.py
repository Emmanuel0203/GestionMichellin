

# TransaccionModel:

####################################

import datetime
from pydantic import BaseModel

####################################

class ModeloTransaccion(BaseModel):
    Venta: str |None = None
    DetalleVenta: str |None = None
    Resultado: str |None = None


####################################