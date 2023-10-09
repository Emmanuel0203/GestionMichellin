
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

###############################################################################

@app.post(
            "/ingresargeografia",
            response_model=ModeloGeografia,
            summary="Ingresar Geografia",
            description="API para Ingresar Geografia",
            tags=["Geografia"]
            )
async def ingresar_geografia(geografia: ModeloGeografia):
    print("Ingreso API ingresar_geografia")
    brokerGeografia = BrokerGeografia()
    return brokerGeografia.ingresar_geografia(geografia)


@app.post(
            "/modificargeografia",
            response_model=ModeloGeografia,
            summary="Modificar Geografia",
            description="API para Modificar Geografia",
            tags=["Geografia"]
            )
async def modificar_geografia(geografia: ModeloGeografia | None = None):
    print("Ingreso API modificar_geografia")
    brokerGeografia = BrokerGeografia()
    return brokerGeografia.modificar_geografia(geografia)


@app.post(
            "/retirargeografia",
            response_model=ModeloGeografia,
            summary="Retirar Geografia",
            description="API para Retirar Geografia",
            tags=["Geografia"]
            )
async def retirar_geografia(geografia: ModeloGeografia | None = None):
    print("Ingreso API retirar_geografia")
    brokerGeografia = BrokerGeografia()
    return brokerGeografia.retirar_geografia(geografia)


@app.post(
            "/consultargeografia",
            response_model=ModeloGeografia,
            summary="Consultar Geografia",
            description="API para Consultar Geografia",
            tags=["Geografia"]
            )
async def consultar_geografia(geografia: ModeloGeografia | None = None):
    print("Ingreso API consultar_geografia")
    brokergeografia = BrokerGeografia()
    return brokergeografia.consultar_geografia(geografia)


@app.post(
            "/consultaridgeografia",
            response_model=ModeloGeografia,
            summary="Consultar ID Geografia",
            description="API para Consultar ID Geografia",
            tags=["Geografia"]
            )
async def consultarid_geografia(geografia: ModeloGeografia | None = None):
    print("Ingreso API consultarid_geografia")
    brokergeografia = BrokerGeografia()
    return brokergeografia.consultarid_geografia(geografia)

###############################################################################

@app.post(
            "/ingresarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Ingresar Organizacion",
            description="API para Ingresar Organizacion",
            tags=["Organizacion"]
            )
async def ingresar_organizacion(organizacion: ModeloOrganizacion | None = None):
    print("Ingreso API ingresar_organizacion")
    brokerOrganizacion = BrokerOrganizacion()
    return brokerOrganizacion.ingresar_organizacion(organizacion)


@app.post(
            "/modificarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Modificar Organizacion",
            description="API para Modificar Organizacion",
            tags=["Organizacion"]
            )
async def modificar_organizacion(organizacion: ModeloOrganizacion | None = None):
    print("Modifico API ingresar_organizacion")
    brokerOrganizacion = BrokerOrganizacion()
    return brokerOrganizacion.modificar_organizacion(organizacion)


@app.post(
            "/retirarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Retirar Organizacion",
            description="API para Retirar Organizacion",
            tags=["Organizacion"]
            )
async def retirar_organizacion(organizacion: ModeloOrganizacion | None = None):
    brokerOrganizacion = BrokerOrganizacion()
    return brokerOrganizacion.retirar_organizacion(organizacion)


@app.post(
            "/consultarorganizacion",
            response_model=ModeloOrganizacion,
            summary="Consultar Organizacion",
            description="API para Consultar Organizacion",
            tags=["Organizacion"]
            )
async def consultar_organizacion(organizacion: ModeloOrganizacion | None = None):
    brokerOrganizacion = BrokerOrganizacion()
    return brokerOrganizacion.consultar_organizacion(organizacion)


@app.post(
            "/consultaridorganizacion",
            response_model=ModeloOrganizacion,
            summary="Consultar ID Organizacion",
            description="API para Consultar ID Organizacion",
            tags=["Organizacion"]
            )
async def consultarid_organizacion(organizacion: ModeloOrganizacion | None = None):
    brokerOrganizacion = BrokerOrganizacion()
    return brokerOrganizacion.consultarid_organizacion(organizacion)

###############################################################################

@app.post(
            "/ingresarservicio",
            response_model=ModeloServicio,
            summary="Ingresar Servicio",
            description="API para Ingresar Servicio",
            tags=["Servicio"]
            )
async def ingresar_servicio(servicio: ModeloServicio | None = None):
    print("Ingreso API ingresar_servicio")
    brokerServicio = BrokerServicio()
    return brokerServicio.ingresar_servicio(servicio)


@app.post(
            "/modificarservicio",
            response_model=ModeloServicio,
            summary="Modificar Servicio",
            description="API para Modificar Servicio",
            tags=["Servicio"]
            )
async def modificar_servicio(servicio: ModeloServicio | None = None):
    brokerServicio = BrokerServicio()
    return brokerServicio.modificar_servicio(servicio)


@app.post(
            "/retirarservicio",
            response_model=ModeloServicio,
            summary="Retirar Servicio",
            description="API para Retirar Servicio",
            tags=["Servicio"]
            )
async def retirar_servicio(servicio: ModeloServicio | None = None):
    brokerServicio = BrokerServicio()
    return brokerServicio.retirar_servicio(servicio)


@app.post(
            "/consultarservicio",
            response_model=ModeloServicio,
            summary="Consultar Servicio",
            description="API para Consultar Servicio",
            tags=["Servicio"]
            )
async def consultar_servicio(servicio: ModeloServicio | None = None):
    brokerServicio = BrokerServicio()
    return brokerServicio.consultar_servicio(servicio)


@app.post(
            "/consultaridservicio",
            response_model=ModeloServicio,
            summary="Consultar ID Servicio",
            description="API para Consultar ID Servicio",
            tags=["Servicio"]
            )
async def consultarid_servicio(servicio: ModeloServicio | None = None):
    brokerServicio = BrokerServicio()
    return brokerServicio.consultarid_servicio(servicio)

###############################################################################

@app.post(
            "/ingresartransaccion",
            response_model=ModeloTransaccion,
            summary="Ingresar Transaccion",
            description="API para Ingresar Transaccion",
            tags=["Transaccion"]
            )
async def ingresar_transaccion(transaccion: ModeloTransaccion | None = None):
    print("Ingreso API ingresar_transaccion")
    brokerTransaccion = BrokerTransaccion()
    return brokerTransaccion.ingresar_transaccion(transaccion)


@app.post(
            "/modificartransaccion",
            response_model=ModeloTransaccion,
            summary="Modificar Transaccion",
            description="API para Modificar Transaccion",
            tags=["Transaccion"]
            )
async def modificar_transaccion(transaccion: ModeloTransaccion | None = None):
    brokerTransaccion = BrokerTransaccion()
    return brokerTransaccion.modificar_transaccion(transaccion)


@app.post(
            "/retirartransaccion",
            response_model=ModeloTransaccion,
            summary="Retirar Transaccion",
            description="API para Retirar Transaccion",
            tags=["Transaccion"]
            )
async def retirar_transaccion(transaccion: ModeloTransaccion | None = None):
    brokerTransaccion = BrokerTransaccion()
    return brokerTransaccion.retirar_transaccion(transaccion)


@app.post(
            "/consultartransaccion",
            response_model=ModeloTransaccion,
            summary="Consultar Transaccion",
            description="API para Consultar Transaccion",
            tags=["Transaccion"]
            )
async def consultar_transaccion(transaccion: ModeloTransaccion | None = None):
    brokerTransaccion = BrokerTransaccion()
    return brokerTransaccion.consultar_transaccion(transaccion)


@app.post(
            "/consultaridtransaccion",
            response_model=ModeloTransaccion,
            summary="Consultar ID Transaccion",
            description="API para Consultar ID Transaccion",
            tags=["Transaccion"]
            )
async def consultarid_transaccion(transaccion: ModeloTransaccion | None = None):
    brokerTransaccion = BrokerTransaccion()
    return brokerTransaccion.consultarid_transaccion(transaccion)

###############################################################################

@app.post(
            "/ingresarusuario",
            response_model=ModeloUsuario,
            summary="Ingresar Usuario",
            description="API para Ingresar Usuario",
            tags=["Usuario"]
            )
async def ingresar_usuario(usuario: ModeloUsuario | None = None):
    print("Ingreso API ingresar_usuario")
    brokerUsuario = BrokerUsuario()
    return brokerUsuario.ingresar_usuario(usuario)


@app.post(
            "/modificarusuario",
            response_model=ModeloUsuario,
            summary="Modificar Usuario",
            description="API para Modificar Usuario",
            tags=["Usuario"]
            )
async def modificar_usuario(usuario: ModeloUsuario | None = None):
    brokerUsuario = BrokerUsuario()
    return brokerUsuario.modificar_usuario(usuario)


@app.post(
            "/retirarusuario",
            response_model=ModeloUsuario,
            summary="Retirar Usuario",
            description="API para Retirar Usuario",
            tags=["Usuario"]
            )
async def retirar_usuario(usuario: ModeloUsuario | None = None):
    brokerUsuario = BrokerUsuario()
    return brokerUsuario.retirar_usuario(usuario)


@app.post(
            "/consultarusuario",
            response_model=ModeloUsuario,
            summary="Consultar Usuario",
            description="API para Consultar Usuario",
            tags=["Usuario"]
            )
async def consultar_usuario(usuario: ModeloUsuario | None = None):
    brokerUsuario = BrokerUsuario()
    return brokerUsuario.consultar_usuario(usuario)


@app.post(
            "/consultaridusuario",
            response_model=ModeloUsuario,
            summary="Consultar ID Usuario",
            description="API para Consultar ID Usuario",
            tags=["Usuario"]
            )
async def consultarid_usuario(usuario: ModeloUsuario | None = None):
    brokerUsuario = BrokerUsuario()
    return brokerUsuario.consultarid_usuario(usuario)

###############################################################################

