from fastapi import FastAPI
from pydantic import BaseModel
from Minimax import Minimax
from tic_tac_toe import tic_tac_toe

app = FastAPI(title="Conecta 4 AI API")
ia = Minimax()
mecanicas = tic_tac_toe()

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

    mecanicas.tablero = solicitud.tablero
    columna_jugador = solicitud.columna_jugador

    #El jugador realiza su movimiento
    mecanicas.movimiento(columna_jugador,"x")
    mecanicas.jugadas +=1

    if mecanicas.comprobar("x"): #comprueba si gana el jugador
        return {"tablero": mecanicas.tablero, "estado": "GANA_x"}

    if mecanicas.jugadas == 42: #comprueba si hay empate
        return {"tablero": mecanicas.tablero, "estado": "EMPATE"}
    
    alpha = float('-inf')
    beta = float('inf')

    copia_tablero = [fila[:] for fila in mecanicas.tablero] #copia profunda del tablero
    puntuacion, columna = ia.algoritmo(copia_tablero,True,7,alpha,beta) #El algoritmo piensa su jugada
    mecanicas.jugada_IA(columna) #El algoritmo realiza su jugada
    mecanicas.jugadas +=1
    if mecanicas.comprobar("o"): #se comprueba si gana el algoritmo
        return {"tablero": mecanicas.tablero, "estado": "GANA_o"}


    if mecanicas.jugadas == 42: #comprueba si hay empate
        return {"tablero": mecanicas.tablero, "estado": "EMPATE"}
    
    #si no hay empate y nadie gana la partida sigue
    return{"tablero": mecanicas.tablero, "estado": "EN_PROCESO", "columna_ia": columna}
    
