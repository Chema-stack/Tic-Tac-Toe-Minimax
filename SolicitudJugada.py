from pydantic import BaseModel

class SolicitudJugada(BaseModel): #consigue la columnna en la que hace click el usuario
    tablero: list[list[str]] 
    columna_jugador: int
