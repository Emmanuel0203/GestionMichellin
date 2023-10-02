

# OrganizacionModel:

####################################

from pydantic import BaseModel

####################################

class ModeloOrganizacion(BaseModel):
    NitEmpresa: str |None = None
    NombreEmpresa: str |None = None
    NombreSede: str |None = None
    DireccionSede: str |None = None
    DocumentoConductor: str |None = None
    NombreConductor: str |None = None
    ApellidoConductor: str |None = None


####################################