from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Minimax import Minimax
from tic_tac_toe import tic_tac_toe

app = FastAPI(title="Conecta 4 AI API")
ia = Minimax()


# @app.get('/')
# async def read_root():
#     return{"message": "Hola"}


class SolicitudJugada(BaseModel): #consigue la columnna en la que hace click el usuario
    tablero: list[list[str]] 
    columna_jugador: int



@app.get("/")
def estado_api():
    """Ruta básica para comprobar que la API está viva."""
    return {"mensaje": "API de Conecta 4 activa y funcionando"}




@app.post("/api/movimiento-ia")
def jugar_IA(solicitud: SolicitudJugada):
    mecanicas = tic_tac_toe()
    mecanicas.tablero = solicitud.tablero
    columna_jugador = int(solicitud.columna_jugador)

    #El jugador realiza su movimiento
    try:
        mecanicas.movimiento( "x", columna_jugador)
    except Exception as e:
        # Devuelve un HTTP 400 con el mensaje de error que lanza tu método
        raise HTTPException(status_code=400, detail=str(e))
    

    if mecanicas.comprobar("x"): #comprueba si gana el jugador
        return {"tablero": mecanicas.tablero, "estado": "GANA_x","columna_ia":None}

    if mecanicas.contar_fichas() == 42: #comprueba si hay empate
        return {"tablero": mecanicas.tablero, "estado": "EMPATE","columna_ia":None}
    
    alpha = float('-inf')
    beta = float('inf')

    copia_tablero = [fila[:] for fila in mecanicas.tablero] #copia profunda del tablero
    puntuacion, columna = ia.algoritmo(copia_tablero,True,7,alpha,beta) #El algoritmo piensa su jugada
    mecanicas.jugada_IA(columna) #El algoritmo realiza su jugada
    
    if mecanicas.comprobar("o"): #se comprueba si gana el algoritmo
        return {"tablero": mecanicas.tablero, "estado": "GANA_o", "columna_ia": columna}


    if mecanicas.contar_fichas() == 42: #comprueba si hay empate
        return {"tablero": mecanicas.tablero, "estado": "EMPATE", "columna_ia": columna}
    
    #si no hay empate y nadie gana la partida sigue
    return{"tablero": mecanicas.tablero, "estado": "EN_PROCESO", "columna_ia": columna}
    
