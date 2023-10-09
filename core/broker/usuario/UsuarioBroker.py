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
from bson import ObjectId
from pymongo import MongoClient
from core.domain.usuario.UsuarioModel import ModeloUsuario

####################################

class BrokerUsuario:
    
    def ingresar_usuario(self, usuario: ModeloUsuario):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Usuario"]
            insert_data = {
                "NombreComprador": "Julio",
                "ApellidoComprador": "Perso",
                "DocumentoComprador": "71695400",
                "DireccionComprador": "Ispania",
                "EmailComprador": "jjulio@example.com",
                "TelefonoComprador": "32317187338",
                "GeneroComprador": "Mujer",
                
                    }
            resultado = col.insert_one(insert_data)
            usuario.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            usuario.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return usuario
    
##############################################################################################################################
		
    def modificar_usuario(self, usuario: ModeloUsuario):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Usuario"]
            
            filter_data = {
                            "NombreComprador": "Julio"
                           }
            update_data = {
                            "$set":
                                {
                                    "NombreComprador": "Julio",
                                    "ApellidoComprador": "Perso",
                                    "DocumentoComprador": "71695400",
                                    "DireccionComprador": "Cali",
                                    "EmailComprador": "jjulio@example.com",
                                    "TelefonoComprador": "32317187338",
                                    "GeneroComprador": "Hombre"


                                }
                            }
            resultado = col.update_many(filter_data, update_data)
            
            resultado = col.update_many({"NombreComprador": usuario.NombreComprador},
                                        {
                                                    "$set":
                                                    {
                                                        "NombreComprador": usuario.NombreComprador,
                                                        "ApellidoComprador": usuario.ApellidoComprador,
                                                        "DocumentoComprador": usuario.DocumentoComprador,
                                                        "DireccionComprador": usuario.DireccionComprador,
                                                        "EmailComprador": usuario.EmailComprador,
                                                        "TelefonoComprador": usuario.TelefonoComprador,
                                                        "GeneroComprador": usuario.GeneroComprador,
                                                    }
                                                }
                                        )
            usuario.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            usuario.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return usuario
    
##############################################################################################################################
	
    def retirar_usuario(self, usuario: ModeloUsuario):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Usuario"]
            
            filter_data = {
                            "NombreComprador": "Julio"
                           }
            resultado = col.delete_many(filter_data)
            
            resultado = col.delete_many({"NombreComprador": usuario.NombreComprador})
            
            usuario.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            usuario.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return usuario
    
##############################################################################################################################

    def consultar_usuario(self, usuario: ModeloUsuario):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Usuario"]

            consult_data = {"NombreComprador": "Julio"}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            usuario.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            usuario.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return usuario

##############################################################################################################################

    def consultar_usuario(self, usuario: ModeloUsuario):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Usuario"]

            consult_data = {"_id": ObjectId('65172cfc97ce3fc75fe97c04')}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            usuario.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            usuario.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return usuario

##############################################################################################################################