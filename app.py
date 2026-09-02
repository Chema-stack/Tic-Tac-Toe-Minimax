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


class SolicitudJugada(BaseModel):
    tablero: list[list[str]]
    columna_jugador: int



@app.get("/")
def estado_api():
    """Ruta básica para comprobar que la API está viva."""
    return {"mensaje": "API de Conecta 4 activa y funcionando"}




@app.post("/api/movimiento-ia")
def jugar(solicitud: SolicitudJugada):

    tablero = solicitud.tablero
    columna_jugador = solicitud.columna_jugador

    mecanicas.movimiento(columna_jugador,"x")
    
    alpha = float('-inf')
    beta = float('inf')

    puntuacion, columna = ia.algoritmo(solicitud.tablero,True,7,alpha,beta)
    
    return {
        "columna": columna
    }
