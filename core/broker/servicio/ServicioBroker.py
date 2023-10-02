####################################

# ServicioBroker:

####################################

from http import client
from typing import Collection
from socket import gaierror
from fastapi.datastructures import URL
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.servicio.ServicioModel import ModeloServicio

####################################

class BrokerServicio:
    
    async def ingresar_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Servicio"]
        data = json.dumps(servicio)
        resultado = col.insert_one()
        servicio.Resultado = resultado.insert_id
        

        client.close() 
        return servicio
		
    async def modificar_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Servicio"]
        
        for x in col.find():
            print(x)       
        return servicio
	
    async def retirar_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Servicio"]
        
        for x in col.find():
             print(x)   
        return servicio

    async def consultar_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Servicio"]


        for x in col.find():
             print(x)    
        return servicio
    
    async def consultarid_servicio(self, servicio: ModeloServicio | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Servicio"]
        
        for x in col.find():
              print(x)   
        return servicio

##########################################