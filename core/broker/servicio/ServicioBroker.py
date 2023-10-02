####################################

# ServicioBroker:

####################################

from http import client
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.servicio.ServicioModel import ModeloServicio

####################################

class BrokerServicio:
    
    

    async def ingresar_servicio(self, geografia: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Servicio "]
        
        client.close()
        return geografia
    
    async def modificar_servicio(self, servicio: ModeloServicio | None = None):
        return servicio
    
    async def retirar_servicio(self, servicio: ModeloServicio | None = None):
        return servicio
    
    async def consultar_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Servicio "]
        #servicio = col.find()

        

        for x in col.find():
            print(x)
        return servicio
    
    async def consultarid_servicio(self, servicio: ModeloServicio | None = None):
        return servicio
        

####################################