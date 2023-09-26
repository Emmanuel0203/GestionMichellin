

# main:

##########################################

import uvicorn

####################################

def webapi_gestionmichellin():
    uvicorn.run(
                "aplication.WebAPIGestionMichellin:app",
                host="127.0.0.1",
                port=8060,
                reload=True
            )

##########################################

if __name__ == '__main__':
    webapi_gestionmichellin()
    
##############################################

