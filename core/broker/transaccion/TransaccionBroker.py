####################################

# TransaccionBroker:

####################################

from http import client
from typing import Collection
from socket import gaierror
from fastapi.datastructures import URL
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.transaccion.TransaccionModel import ModeloTransaccion

####################################

class BrokerTransaccion:
    
    def ingresar_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]
            insert_data = {
                "NombrePais": "Mexico",
                "NombreDepartamento": "DF",
                "NombreCiudad": "CDMX"
                    }
            resultado = col.insert_one(insert_data)
            transaccion.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            transaccion.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return transaccion
		
    async def modificar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Transaccional"]
        
        for x in col.find():
            print(x)       
        return transaccion
	
    async def retirar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Transaccional"]
        
        for x in col.find():
             print(x)   
        return transaccion

    async def consultar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Transaccional"]


        for x in col.find():
             print(x)    
        return transaccion
    
    async def consultarid_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Transaccional"]
        
        for x in col.find():
              print(x)   
        return transaccion

##########################################