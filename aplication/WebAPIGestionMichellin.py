
#WebAPIGestionMichellin

#####################################

from fastapi import FastAPI

from core.domain.geografia.GeografiaModel import Geografia


app: FastAPI = FastAPI(
                        title='Web API Gestion Michellin',
                        description='UUSBGS - 202302'
                        )

###########################################

@app.post(
            "/ingresargeografia",
            response_model=Geografia,
            summary="Ingresar Geografia",
            description="API para Ingresar Geografia",
            tags=["Geografia"]
            )
async def ingresar_geografia(geografia: Geografia | None = None):
    return geografia


@app.post(
            "/modificargeografia",
            response_model=Geografia,
            summary="Modificar Geografia",
            description="API para Modificar Geografia",
            tags=["Geografia"]
            )
async def modificar_geografia(geografia: Geografia | None = None):
    return geografia


@app.post(
            "/retirargeografia",
            response_model=Geografia,
            summary="Retirar Geografia",
            description="API para Retirar Geografia",
            tags=["Geografia"]
            )
async def retirar_geografia(geografia: Geografia | None = None):
    return geografia


@app.post(
            "/consultargeografia",
            response_model=Geografia,
            summary="Consultar Geografia",
            description="API para Consultar Geografia",
            tags=["Geografia"]
            )
async def consultar_geografia(geografia: Geografia | None = None):
    return geografia


@app.post(
            "/consultaridgeografia",
            response_model=Geografia,
            summary="Consultar ID Geografia",
            description="API para Consultar ID Geografia",
            tags=["Geografia"]
            )
async def consultarid_geografia(geografia: Geografia | None = None):
    return geografia

#####################################################

