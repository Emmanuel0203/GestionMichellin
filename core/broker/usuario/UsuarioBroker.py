####################################

# UsuarioBroker:

####################################

from http import client
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.usuario.UsuarioModel import ModeloUsuario

####################################

class BrokerUsuario:
    
    

    async def ingresar_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Usuario"]
        
        client.close()
        return usuario
    
    async def modificar_usuario(self, usuario: ModeloUsuario | None = None):
        return usuario
    
    async def retirar_usuario(self, usuario: ModeloUsuario | None = None):
        return usuario
    
    async def consultar_usuario(self, usuario: ModeloUsuario | None = None):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["dbaMichellin"]
        col = db["Usuario"]
        #geografia = col.find()

        

        for x in col.find():
            print(x)
        return usuario
    
    async def consultarid_usuario(self, usuario: ModeloUsuario | None = None):
        return usuario
        

####################################