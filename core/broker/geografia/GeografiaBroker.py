
# GeografiaBroker:

####################################

from http import client
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.geografia.GeografiaModel import ModeloGeografia

####################################

class BrokerGeografia:
    
    

    async def ingresar_geografia(self, geografia: ModeloGeografia | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Geografia"]
        
        client.close()
        return geografia
    
    async def modificar_geografia(self, geografia: ModeloGeografia | None = None):
        return geografia
    
    async def retirar_geografia(self, geografia: ModeloGeografia | None = None):
        return geografia
    
    async def consultar_geografia(self, geografia: ModeloGeografia | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Geografia"]
        #geografia = col.find()

        

        for x in col.find():
            print(x)
        return geografia
    
    async def consultarid_geografia(self, geografia: ModeloGeografia | None = None):
        return geografia
        

####################################