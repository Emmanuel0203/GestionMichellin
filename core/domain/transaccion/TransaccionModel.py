

# TransaccionModel:

####################################

import datetime
from pydantic import BaseModel

####################################

class ModeloTransaccion(BaseModel):
    CodigoVenta: str |None = None
    FechaVenta: str |None = None
    CantidadVenta: int |None = None
    TotalVenta: int |None = None


####################################