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
from bson import ObjectId
from pymongo import MongoClient
from core.domain.servicio.ServicioModel import ModeloServicio

####################################

class BrokerServicio:
    
    def ingresar_servicio(self, servicio: ModeloServicio):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Servicio"]
            insert_data = {
                "CodigoProducto": "RN652",
                "PrecioProducto": "105000",
                "NombreProducto": "Rin Special",
                "MarcaProducto": "Rinstone",
                "DescripcionProducto": "Rin importado desde italia",                
                    }
                    
            resultado = col.insert_one(insert_data)
            servicio.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            servicio.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return servicio
    
##############################################################################################################################
		
    def modificar_servicio(self, servicio: ModeloServicio):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Servicio"]
            
            filter_data = {
                            "CodigoProducto": "RN652"
                           }
            update_data = {
                            "$set":
                                {
                                    "CodigoProducto": "RN652",
                                    "PrecioProducto": "105000",
                                    "NombreProducto": "Rin Especial",
                                    "MarcaProducto": "Ringstone",
                                    "DescripcionProducto": "Rin importado desde italia y fabricado en Roma"

                                }
                            }
            resultado = col.update_many(filter_data, update_data)
            
            resultado = col.update_many({"CodigoProducto": servicio.CodigoProducto},
                                        {
                                                    "$set":
                                                    {
                                                        "CodigoProducto": servicio.CodigoProducto,
                                                        "PrecioProducto": servicio.PrecioProducto,
                                                        "NombreProducto": servicio.NombreProducto,
                                                        "MarcaProducto": servicio.MarcaProducto,
                                                        "DescripcionProducto": servicio.DescripcionProducto,
                                                    }
                                                }
                                        )
            servicio.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            servicio.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return servicio
    
##############################################################################################################################
	
    def retirar_servicio(self, servicio: ModeloServicio):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Servicio"]
            
            filter_data = {
                            "CodigoProducto": "RN652"
                           }
            resultado = col.delete_many(filter_data)
            
            resultado = col.delete_many({"CodigoProducto": servicio.CodigoProducto})
            servicio.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            servicio.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return servicio
    
##############################################################################################################################

    def consultar_servicio(self, servicio: ModeloServicio):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Servicio"]

            consult_data = {"CodigoProducto": "CP661"}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            servicio.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            servicio.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return servicio

##############################################################################################################################

    def consultarid_servicio(self, servicio: ModeloServicio):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Servicio"]

            consult_data = {"_id": ObjectId('651b04a297ce3fc75fce00af')}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            servicio.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            servicio.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return servicio

##############################################################################################################################