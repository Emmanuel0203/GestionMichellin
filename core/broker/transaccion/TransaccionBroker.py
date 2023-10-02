####################################

# TransaccionBroker:

####################################

from http import client
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.transaccion.TransaccionModel import ModeloTransaccion

####################################

class BrokerTransaccion:
    
    

    async def ingresar_transaccion(self, geografia: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Transaccion"]
        
        client.close()
        return geografia
    
    async def modificar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        return transaccion
    
    async def retirar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        return transaccion
    
    async def consultar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Transaccion"]
        #transaccion = col.find()

        

        for x in col.find():
            print(x)
        return transaccion
    
    async def consultarid_geografia(self, transaccion: ModeloTransaccion | None = None):
        return transaccion
        

####################################