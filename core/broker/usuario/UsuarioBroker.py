####################################

# UsuarioBroker:

####################################

from http import client
from typing import Collection
from socket import gaierror
from fastapi.datastructures import URL
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.usuario.UsuarioModel import ModeloUsuario

####################################

class BrokerUsuario:
    
    def ingresar_usuario(self, usuario: ModeloUsuario):
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
            usuario.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            usuario.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return usuario
		
    async def modificar_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Usuario"]
        
        for x in col.find():
            print(x)       
        return usuario
	
    async def retirar_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Usuario"]
        
        for x in col.find():
             print(x)   
        return usuario

    async def consultar_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Usuario"]


        for x in col.find():
             print(x)    
        return usuario
    
    async def consultarid_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaReencauchadoraEA"]
        col = db["Usuario"]
        
        for x in col.find():
              print(x)   
        return usuario

##########################################