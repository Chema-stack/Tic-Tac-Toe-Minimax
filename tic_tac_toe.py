class Juego:

    def __init__(self):
        self.tablero = [["-" for _ in range(3)] for _ in range(3)]

    def normalizador(self, fila,columna): #Esta funcion normaliza los movimientos
        return fila - 1, columna - 1 #Le quita a la fila y a la columna uno
                                    #para que entre en los limites de la matriz

    def movimiento(self,jugador,fila,columna):
        
        fila, columna = self.normalizador(fila,columna)

        if self.tablero[fila][columna] == "-":
            self.tablero[fila][columna] = jugador
        else:
            raise ValueError("Jugada no valida")
        
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" | ".join(fila))
        print()

    

            