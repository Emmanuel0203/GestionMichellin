####################################

# OrganizacionBroker:

####################################

from http import client
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.organizacion.OrganizacionModel import ModeloOrganizacion

####################################

class BrokerOrganizacion:
    
    

    async def ingresar_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Organizacion"]
        
        client.close()
        return organizacion
    
    async def modificar_geografia(self, organizacion: ModeloOrganizacion | None = None):
        return organizacion
    
    async def retirar_geografia(self, organizacion: ModeloOrganizacion | None = None):
        return organizacion
    
    async def consultar_geografia(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Organizacion"]
        #organizacion = col.find()

        

        for x in col.find():
            print(x)
        return organizacion
    
    async def consultarid_geografia(self, organizacion: ModeloOrganizacion | None = None):
        return organizacion
        

####################################