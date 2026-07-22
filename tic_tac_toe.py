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

    def comprobar(self, jugador):
            # 1. Comprobar Filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] == jugador:
                return True

        # 2. Comprobar Columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] == jugador:
                return True

        # 3. Comprobar Diagonal Principal (de izquierda a derecha)
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
            return True

        # 4. Comprobar Diagonal Secundaria (de derecha a izquierda)
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
            return True

        return False


            