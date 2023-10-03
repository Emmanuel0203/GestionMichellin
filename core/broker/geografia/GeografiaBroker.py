
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
    def ingresar_geografia(self, geografia: ModeloGeografia):
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
            geografia.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            geografia.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return geografia
		
    
    def modificar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]
            filter_data = {
                            "NombrePais": "Mexico"
                           }
            update_data = {
                            "$set":
                                {
                                    "NombrePais": "Mexico",
                                    "NombreDepartamento": "Distrito Federal",
                                    "NombreCiudad": "CDMX"
                                }
                            }
            resultado = col.update_many(filter_data, update_data)
            geografia.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            geografia.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return geografia
	
    def retirar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]
            filter_data = {
                            "NombrePais": "Mexico"
                           }
            resultado = col.delete_many(filter_data)
            geografia.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            geografia.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return geografia

    async def consultar_geografia(self, geografia: ModeloGeografia | None = None):
         URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
         client = pymongo.MongoClient(URL)
         db = client["dbaReencauchadoraEA"]
         col = db["Geografia"]


         for x in col.find():
             print(x)    
         return geografia
    
    async def consultarid_geografia(self, geografia: ModeloGeografia | None = None):
          URL = "mongodb+srv://dbauser:<Mono1011>@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
          client = pymongo.MongoClient(URL)
          db = client["dbaReencauchadoraEA"]
          col = db["Geografia"]
        
          for x in col.find():
              print(x)   
          return geografia

##########################################
