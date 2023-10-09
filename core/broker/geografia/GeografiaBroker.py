# GeografiaBroker:

##########################################

import pymongo
import json
from bson import json_util
import collections

##########################################
from bson import ObjectId
from pymongo import MongoClient
from core.domain.geografia.GeografiaModel import ModeloGeografia


##########################################

class BrokerGeografia:
    def ingresar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]
            insert_data = {
                "NombrePais": "Mexico",
                "NombreDepartamento": "DF",
                "NombreCiudad": "CDMX",
                
                    }
            resultado = col.insert_one(insert_data)
            geografia.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            geografia.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return geografia
    
##############################################################################################################################

    def modificar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
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
            
            resultado = col.update_many({"NombrePais": geografia.NombrePais},
                                        {
                                                    "$set":
                                                    {
                                                        "NombrePais": geografia.NombrePais,
                                                        "NombreDepartamento": geografia.NombreDepartamento,
                                                        "NombreCiudad": geografia.NombreCiudad,
                                                    }
                                                }
                                        )
            geografia.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            geografia.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return geografia

##############################################################################################################################

    def retirar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]
            
            filter_data = {
                            "NombrePais": "Mexico"
                           }
            resultado = col.delete_many(filter_data)
            
            resultado = col.delete_many({"NombrePais": geografia.NombrePais})
            geografia.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            geografia.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return geografia

##############################################################################################################################

    def consultar_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]

            consult_data = {"NombrePais": "Canada"}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            geografia.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            geografia.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return geografia

##############################################################################################################################

    def consultarid_geografia(self, geografia: ModeloGeografia):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Geografia"]

            consult_data = {"_id": ObjectId('6509190997ce3fc75ff74b8e')}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            geografia.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            geografia.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return geografia

##############################################################################################################################