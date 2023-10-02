####################################

# OrganizacionBroker:

####################################

from http import client
from typing import Collection
from socket import gaierror
from fastapi.datastructures import URL
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.organizacion.OrganizacionModel import ModeloOrganizacion

####################################

class BrokerOrganizacion:
    
    async def ingresar_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Organizacional"]
        data = json.dumps(organizacion)
        resultado = col.insert_one()
        organizacion.Resultado = resultado.insert_id
        

        client.close() 
        return organizacion
		
    async def modificar_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Organizacional"]
        
        for x in col.find():
            print(x)       
        return organizacion
	
    async def retirar_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Organizacional"]
        
        for x in col.find():
             print(x)   
        return organizacion

    async def consultar_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Organizacional"]


        for x in col.find():
             print(x)    
        return organizacion
    
    async def consultarid_organizacion(self, organizacion: ModeloOrganizacion | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Organizacional"]
        
        for x in col.find():
              print(x)   
        return organizacion

##########################################