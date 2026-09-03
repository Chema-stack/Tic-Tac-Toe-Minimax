import os
import Minimax


class tic_tac_toe:

    def __init__(self):
        self.tablero = [["-" for _ in range(7)] for _ in range(6)]
        self.jugadas = 0

    def normalizador(self,columna): #Esta funcion normaliza los movimientos
        return columna - 1 #Le quita a la fila y a la columna uno
                                    #para que entre en los limites de la matriz

    def movimiento(self,jugador,columna): #realiza un movimiento del juego
        
        columna = self.normalizador(columna) #normalizamos la entrada


        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] == "-":  # si encuentra un espacio libre en la columna coloca
                self.tablero[fila][columna] = jugador
                return

        
        raise ValueError("Jugada no valida") #si la columna esta ocupada salta excepcion

    
        
    def imprimir_tablero(self): #imprime tablero
        for fila in self.tablero:
            print(" | ".join(fila))
        print()

    def comprobar_minimax(self,tablero,jugador): #comprueba si hay 3 en raya para el algoritmo

        FILAS = 6
        COLUMNAS = 7

        # 1. Comprobación HORIZONTAL (--)
        for f in range(FILAS):
            for c in range(COLUMNAS - 3):  # c va de 0 a 3 para no salirse del borde
                if (tablero[f][c] == jugador and 
                    tablero[f][c + 1] == jugador and 
                    tablero[f][c + 2] == jugador and 
                    tablero[f][c + 3] == jugador):
                    return True

        # 2. Comprobación VERTICAL (|)
        for f in range(FILAS - 3):  # f va de 0 a 2 para no salirse por abajo
            for c in range(COLUMNAS):
                if (tablero[f][c] == jugador and 
                    tablero[f + 1][c] == jugador and 
                    tablero[f + 2][c] == jugador and 
                    tablero[f + 3][c] == jugador):
                    return True

        # 3. Comprobación DIAGONAL DESCENDENTE (\)
        for f in range(FILAS - 3):
            for c in range(COLUMNAS - 3):
                if (tablero[f][c] == jugador and 
                    tablero[f + 1][c + 1] == jugador and 
                    tablero[f + 2][c + 2] == jugador and 
                    tablero[f + 3][c + 3] == jugador):
                    return True

        # 4. Comprobación DIAGONAL ASCENDENTE (/)
        for f in range(3, FILAS):  # f empieza en 3 para poder subir 3 casillas
            for c in range(COLUMNAS - 3):
                if (tablero[f][c] == jugador and 
                    tablero[f - 1][c + 1] == jugador and 
                    tablero[f - 2][c + 2] == jugador and 
                    tablero[f - 3][c + 3] == jugador):
                    return True

        return False

    def comprobar(self, jugador): #comprueba si hay 3 en raya
        FILAS = 6
        COLUMNAS = 7

        # 1. Comprobación HORIZONTAL (--)
        for f in range(FILAS):
            for c in range(COLUMNAS - 3):  # c va de 0 a 3 para no salirse del borde
                if (self.tablero[f][c] == jugador and 
                    self.tablero[f][c + 1] == jugador and 
                    self.tablero[f][c + 2] == jugador and 
                    self.tablero[f][c + 3] == jugador):
                    return True

        # 2. Comprobación VERTICAL (|)
        for f in range(FILAS - 3):  # f va de 0 a 2 para no salirse por abajo
            for c in range(COLUMNAS):
                if (self.tablero[f][c] == jugador and 
                    self.tablero[f + 1][c] == jugador and 
                    self.tablero[f + 2][c] == jugador and 
                    self.tablero[f + 3][c] == jugador):
                    return True

        # 3. Comprobación DIAGONAL DESCENDENTE (\)
        for f in range(FILAS - 3):
            for c in range(COLUMNAS - 3):
                if (self.tablero[f][c] == jugador and 
                    self.tablero[f + 1][c + 1] == jugador and 
                    self.tablero[f + 2][c + 2] == jugador and 
                    self.tablero[f + 3][c + 3] == jugador):
                    return True

        # 4. Comprobación DIAGONAL ASCENDENTE (/)
        for f in range(3, FILAS):  # f empieza en 3 para poder subir 3 casillas
            for c in range(COLUMNAS - 3):
                if (self.tablero[f][c] == jugador and 
                    self.tablero[f - 1][c + 1] == jugador and 
                    self.tablero[f - 2][c + 2] == jugador and 
                    self.tablero[f - 3][c + 3] == jugador):
                    return True

        return False    

    def turno(self): #Alterna entre uno y otro

        
        if self.jugadas % 2 == 0: #si la jugada es par o 0 es el turno de x
            
            return "x"
        else: #si la jugada es impar es el turno de y
            
            return "o"
        
    def seleccionar_jugada(self,jugador): #pide al jugador la fila y columna y realiza movimiento
        columna = int(input("Seleccione columna:"))
        try:
            self.movimiento(jugador,columna) #se realiza el movimiento
            self.jugadas += 1 #jugada realizada con exito
        except ValueError:
            raise ValueError("Jugada no valida")
        

    def contar_fichas(self):
        
    

    def jugada_IA(self,columna): #Realiza una jugada de la IA
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] == "-":  # si encuentra un espacio libre en la columna coloca
                self.tablero[fila][columna] = "o"
                self.jugadas += 1
                return
          