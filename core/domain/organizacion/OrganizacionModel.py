

# OrganizacionModel:

####################################

from pydantic import BaseModel

####################################

class ModeloOrganizacion(BaseModel):
    Empresa: str |None = None
    Sede: str |None = None
    Trabajador: str |None = None


####################################