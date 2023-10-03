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
    
    def ingresar_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]
            insert_data = {
                "NitEmpresa":"123456789-0",
                "NombreEmpresa": "Michellin",
                "NombreSede": "Sede Medellin",
                "DireccionSede":"Centro de Medellin",
                "DocumentoTrabajador":"123456789",
                "NombreTrabajador":"Cosme",
                "ApellidoTrabajador":"Fulanito"
                    }
                    
            resultado = col.insert_one(insert_data)
            organizacion.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            organizacion.Resultado = f"Ingresar Fallida: {ex}"
        finally:
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