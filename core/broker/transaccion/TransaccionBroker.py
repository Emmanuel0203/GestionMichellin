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
from bson import ObjectId
from pymongo import MongoClient
from core.domain.transaccion.TransaccionModel import ModeloTransaccion

####################################

class BrokerTransaccion:
    
    def ingresar_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Transaccional"]
            insert_data = {
                "CodigoVenta": "CD999806",
                "FechaVenta": "2023-12-20T00:00:00",
                "CantidadVenta": "3",
                "TotalVenta": "270000",                
                    }
            resultado = col.insert_one(insert_data)
            transaccion.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            transaccion.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return transaccion
    
##############################################################################################################################
		
    def modificar_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Transaccional"]
            
            filter_data = {
                            "CodigoVenta": "CD999804"
                           }
            update_data = {
                            "$set":
                                {
                                    "CodigoVenta": "CD999806",
                                    "FechaVenta": "2023-12-20T00:00:00",
                                    "CantidadVenta": "5",
                                    "TotalVenta": "500000"
                                }
                            }
            resultado = col.update_many(filter_data, update_data)
            
            resultado = col.update_many({"CodigoVenta": transaccion.CodigoVenta},
                                        {
                                                    "$set":
                                                    {
                                                        "CodigoVenta": transaccion.CodigoVenta,
                                                        "FechaVenta": transaccion.FechaVenta,
                                                        "CantidadVenta": transaccion.CantidadVenta,
                                                        "TotalVenta": transaccion.TotalVenta,
                                                    }
                                                }
                                        )
            transaccion.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            transaccion.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return transaccion
    
##############################################################################################################################
	
    def retirar_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Transaccional"]
            
            filter_data = {
                            "CodigoVenta": "CD999804"
                           }
            resultado = col.delete_many(filter_data)
            
            resultado = col.delete_many({"CodigoVenta": transaccion.CodigoVenta})
            transaccion.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            transaccion.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return transaccion
    
##############################################################################################################################

    def consultar_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Transaccional"]

            consult_data = {"CodigoVenta": "CD999804"}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            transaccion.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            transaccion.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return transaccion

##############################################################################################################################

    def consultarid_transaccion(self, transaccion: ModeloTransaccion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Transaccional"]

            consult_data = {"_id": ObjectId('651b07c297ce3fc75fda01e6')}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            transaccion.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            transaccion.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return transaccion

##############################################################################################################################