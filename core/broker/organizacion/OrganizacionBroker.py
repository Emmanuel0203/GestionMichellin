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
from bson import ObjectId
from pymongo import MongoClient
from core.domain.organizacion.OrganizacionModel import ModeloOrganizacion

####################################

class BrokerOrganizacion:
    
    def ingresar_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]
            insert_data = {
                "NitEmpresa": "123456789-0",
                "NombreEmpresa": "Michellin",
                "NombreSede": "Sede Medellin",
                "DireccionSede": "Aranjuez",
                "DocumentoTrabajador": "1012397265",
                "NombreTrabajador": "Policarpio",
                "ApellidoTrabajador": "Salavarrieta",
                
                    }
            resultado = col.insert_one(insert_data)
            organizacion.Resultado = f"Ingresar Exitosa: {resultado.inserted_id}"
        except Exception as ex:
            organizacion.Resultado = f"Ingresar Fallida: {ex}"
        finally:
            client.close()
        return organizacion
    
##############################################################################################################################
		
    def modificar_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]
            
            filter_data = {
                            "NombreTrabajador": "Policarpio"
                           }
            update_data = {
                            "$set":
                                {
                                    "NitEmpresa": "123456789-0",
                                    "NombreEmpresa": "Michellin",
                                    "NombreSede": "Sede Medellin",
                                    "DireccionSede": "Robledo",
                                    "DocumentoTrabajador": "1012390005",
                                    "NombreTrabajador": "Policarpa",
                                    "ApellidoTrabajador": "Salvador"


                                }
                            }
            resultado = col.update_many(filter_data, update_data)
            
            resultado = col.update_many({"NombreTrabajador": organizacion.NombreTrabajador},
                                        {
                                                    "$set":
                                                    {
                                                        "NitEmpresa": organizacion.NitEmpresa,
                                                        "NombreEmpresa": organizacion.NombreEmpresa,
                                                        "NombreSede": organizacion.NombreSede,
                                                        "DireccionSede": organizacion.DireccionSede,
                                                        "DocumentoTrabajador": organizacion.DocumentoTrabajador,
                                                        "NombreTrabajador": organizacion.NombreTrabajador,
                                                        "ApellidoTrabajador": organizacion.ApellidoTrabajador,
                                                    }
                                                }
                                        )
            organizacion.Resultado = f"Modificar Exitosa: {resultado.modified_count}"
        except Exception as ex:
            organizacion.Resultado = f"Modificar Fallida: {ex}"
        finally:
            client.close()
        return organizacion
    
##############################################################################################################################
	
    def retirar_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]
            
            filter_data = {
                            "NombreTrabajador": "Policarpa"
                           }
            resultado = col.delete_many(filter_data)
            
            resultado = col.delete_many({"NombreTrabajador": organizacion.NombreTrabajador})
            organizacion.Resultado = f"Retirar Exitosa: {resultado.deleted_count}"
        except Exception as ex:
            organizacion.Resultado = f"Retirar Fallida: {ex}"
        finally:
            client.close()
        return organizacion
    
##############################################################################################################################

    def consultar_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]

            consult_data = {"NombreTrabajador": "Policarpa"}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            organizacion.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            organizacion.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return organizacion

##############################################################################################################################

    def consultarid_organizacion(self, organizacion: ModeloOrganizacion):
        URL = "mongodb+srv://dbauser:dbaPassword@cluster0.4ysq7er.mongodb.net/dbaReencauchadoraEA?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(URL)
            db = client["dbaReencauchadoraEA"]
            col = db["Organizacional"]

            consult_data = {"_id": ObjectId('65244995f2103cdacc70d3f3')}


            resultados = list(col.find(consult_data))
            resultado_formateado = [str(item) for item in resultados]

            organizacion.Resultado = f"Consultar Exitosa: {resultado_formateado}"
        except Exception as ex:
            organizacion.Resultado = f"Consultar Fallida: {str(ex)}"
        finally:
            client.close()
        return organizacion

##############################################################################################################################