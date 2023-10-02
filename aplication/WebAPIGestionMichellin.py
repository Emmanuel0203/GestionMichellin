
#WebAPIGestionMichellin

#####################################

from fastapi import FastAPI

from core.domain.geografia.GeografiaModel import ModeloGeografia
from core.broker.geografia.GeografiaBroker import BrokerGeografia
#######################################################################
from core.domain.organizacion.OrganizacionModel import ModeloOrganizacion
from core.broker.organizacion.OrganizacionBroker import BrokerOrganizacion
#######################################################################
from core.domain.servicio.ServicioModel import ModeloServicio
from core.broker.servicio.ServicioBroker import BrokerServicio
#######################################################################
from core.domain.transaccion.TransaccionModel import ModeloTransaccion
from core.broker.transaccion.TransaccionBroker import BrokerTransaccion
#######################################################################
from core.domain.usuario.UsuarioModel import ModeloUsuario
from core.broker.usuario.UsuarioBroker import BrokerUsuario


app: FastAPI = FastAPI(
                        title='Web API Gestion Michellin',
                        description='UUSBGS - 202302'
                        )

###########################################

@app.post(
            "/ingresargeografia",
            response_model=ModeloGeografia,
            summary="Ingresar Geografia",
            description="API para Ingresar Geografia",
            tags=["Geografia"]
            )
async def ingresar_geografia(geografia: ModeloGeografia | None = None):
    return geografia


@app.post(
            "/modificargeografia",
            response_model=ModeloGeografia,
            summary="Modificar Geografia",
            description="API para Modificar Geografia",
            tags=["Geografia"]
            )
async def modificar_geografia(geografia: ModeloGeografia | None = None):
    return geografia


@app.post(
            "/retirargeografia",
            response_model=ModeloGeografia,
            summary="Retirar Geografia",
            description="API para Retirar Geografia",
            tags=["Geografia"]
            )
async def retirar_geografia(geografia: ModeloGeografia | None = None):
    return geografia


@app.post(
            "/consultargeografia",
            response_model=ModeloGeografia,
            summary="Consultar Geografia",
            description="API para Consultar Geografia",
            tags=["Geografia"]
            )
async def consultar_geografia(geografia: ModeloGeografia | None = None):
    brokergeografia = BrokerGeografia()
    geografia = brokergeografia.consultar_geografia(geografia)
    return geografia


@app.post(
            "/consultaridgeografia",
            response_model=ModeloGeografia,
            summary="Consultar ID Geografia",
            description="API para Consultar ID Geografia",
            tags=["Geografia"]
            )
async def consultarid_geografia(geografia: ModeloGeografia | None = None):
    return geografia

#####################################################

@app.post(
            "/ingresarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Ingresar Organizacion",
            description="API para Ingresar Organizacion",
            tags=["Organizacion"]
            )
async def ingresar_organizacion(organizacion: ModeloOrganizacion | None = None):
    return organizacion


@app.post(
            "/modificarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Modificar Organizacion",
            description="API para Modificar Organizacion",
            tags=["Organizacion"]
            )
async def modificar_organizacion(organizacion: ModeloOrganizacion | None = None):
    return organizacion


@app.post(
            "/retirarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Retirar Organizacion",
            description="API para Retirar Organizacion",
            tags=["Organizacion"]
            )
async def retirar_organizacion(organizacion: ModeloOrganizacion | None = None):
    return organizacion


@app.post(
            "/consultarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Consultar Organizacion",
            description="API para Consultar Organizacion",
            tags=["Organizacion"]
            )
async def consultar_organizacion(organizacion: ModeloOrganizacion | None = None):
    brokerorganizacion = BrokerOrganizacion()
    organizacion = brokerorganizacion.consultar_organizacion(organizacion)
    return organizacion


@app.post(
            "/consultaridorganizacion",
            response_model=ModeloOrganizacion,
            summary="Consultar ID Organizacion",
            description="API para Consultar ID Organizacion",
            tags=["Organizacion"]
            )
async def consultarid_organizacion(organizacion: ModeloOrganizacion | None = None):
    return organizacion

#####################################################

@app.post(
            "/ingresarservicio",
            response_model=ModeloServicio,
            summary="Ingresar Servicio",
            description="API para Ingresar Servicio",
            tags=["Servicio"]
            )
async def ingresar_servicio(servicio: ModeloServicio | None = None):
    return servicio


@app.post(
            "/modificarservicio",
            response_model=ModeloServicio,
            summary="Modificar Servicio",
            description="API para Modificar Servicio",
            tags=["Servicio"]
            )
async def modificar_servicio(servicio: ModeloServicio | None = None):
    return servicio


@app.post(
            "/retirarservicio",
            response_model=ModeloServicio,
            summary="Retirar Servicio",
            description="API para Retirar Servicio",
            tags=["Servicio"]
            )
async def retirar_servicio(servicio: ModeloServicio | None = None):
    return servicio


@app.post(
            "/consultarservicio",
            response_model=ModeloServicio,
            summary="Consultar Servicio",
            description="API para Consultar Servicio",
            tags=["Servicio"]
            )
async def consultar_servicio(servicio: ModeloServicio | None = None):
    brokerservicio = BrokerServicio()
    servicio = brokerservicio.consultar_servicio(servicio)
    return servicio


@app.post(
            "/consultaridservicio",
            response_model=ModeloServicio,
            summary="Consultar ID Servicio",
            description="API para Consultar ID Servicio",
            tags=["Servicio"]
            )
async def consultarid_servicio(servicio: ModeloServicio | None = None):
    return servicio

#####################################################

@app.post(
            "/ingresartransaccion",
            response_model=ModeloTransaccion,
            summary="Ingresar Transaccion",
            description="API para Ingresar Transaccion",
            tags=["Transaccion"]
            )
async def ingresar_transaccion(transaccion: ModeloTransaccion | None = None):
    return transaccion


@app.post(
            "/modificartransaccion",
            response_model=ModeloTransaccion,
            summary="Modificar Transaccion",
            description="API para Modificar Transaccion",
            tags=["Transaccion"]
            )
async def modificar_transaccion(transaccion: ModeloTransaccion | None = None):
    return transaccion


@app.post(
            "/retirartransaccion",
            response_model=ModeloTransaccion,
            summary="Retirar Transaccion",
            description="API para Retirar Transaccion",
            tags=["Transaccion"]
            )
async def retirar_transaccion(transaccion: ModeloTransaccion | None = None):
    return transaccion


@app.post(
            "/consultartransaccion",
            response_model=ModeloTransaccion,
            summary="Consultar Transaccion",
            description="API para Consultar Transaccion",
            tags=["Transaccion"]
            )
async def consultar_transaccion(transaccion: ModeloTransaccion | None = None):
    brokertransaccion = BrokerTransaccion()
    transaccion = brokertransaccion.consultar_transaccion(transaccion)
    return transaccion


@app.post(
            "/consultaridtransaccion",
            response_model=ModeloTransaccion,
            summary="Consultar ID Transaccion",
            description="API para Consultar ID Transaccion",
            tags=["Transaccion"]
            )
async def consultarid_transaccion(transaccion: ModeloTransaccion | None = None):
    return transaccion

#####################################################

@app.post(
            "/ingresarusuario",
            response_model=ModeloUsuario,
            summary="Ingresar Usuario",
            description="API para Ingresar Usuario",
            tags=["Usuario"]
            )
async def ingresar_usuario(usuario: ModeloUsuario | None = None):
    return usuario


@app.post(
            "/modificarusuario",
            response_model=ModeloUsuario,
            summary="Modificar Usuario",
            description="API para Modificar Usuario",
            tags=["Geografia"]
            )
async def modificar_usuario(usuario: ModeloUsuario | None = None):
    return usuario


@app.post(
            "/retirarusuario",
            response_model=ModeloUsuario,
            summary="Retirar Usuario",
            description="API para Retirar Usuario",
            tags=["Usuario"]
            )
async def retirar_usuario(usuario: ModeloUsuario | None = None):
    return usuario


@app.post(
            "/consultarusuario",
            response_model=ModeloUsuario,
            summary="Consultar Usuario",
            description="API para Consultar Usuario",
            tags=["Usuario"]
            )
async def consultar_usuario(usuario: ModeloUsuario | None = None):
    brokerusuario = BrokerUsuario()
    usuario = brokerusuario.consultar_usuario(usuario)
    return usuario


@app.post(
            "/consultaridusuario",
            response_model=ModeloUsuario,
            summary="Consultar ID Usuario",
            description="API para Consultar ID Usuario",
            tags=["Usuario"]
            )
async def consultarid_geografia(usuario: ModeloUsuario | None = None):
    return usuario

#####################################################

