import os
import Minimax

class tic_tac_toe:

    def __init__(self):
        self.tablero = [["-" for _ in range(3)] for _ in range(3)]
        self.jugadas = 0

    def normalizador(self, fila,columna): #Esta funcion normaliza los movimientos
        return fila - 1, columna - 1 #Le quita a la fila y a la columna uno
                                    #para que entre en los limites de la matriz

    def movimiento(self,jugador,fila,columna): #realiza un movimiento del juego
        
        fila, columna = self.normalizador(fila,columna) #normalizamos la entrada

        if self.tablero[fila][columna] == "-": #si no hay nada en dicha posicion
            self.tablero[fila][columna] = jugador #colocamos la ficha
        else:
            raise ValueError("Jugada no valida") #si la casilla esta ocupada salta excepcion

    
        
    def imprimir_tablero(self): #imprime tablero
        for fila in self.tablero:
            print(" | ".join(fila))
        print()

    def comprobar_minimax(self,tablero,jugador):
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

    def comprobar(self, jugador): #comprueba si hay 3 en raya
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
    
    def turno(self): #Alterna entre uno y otro

        
        if self.jugadas % 2 == 0: #si la jugada es par o 0 es el turno de x
            
            return "x"
        else: #si la jugada es impar es el turno de y
            
            return "o"
        
    def seleccionar_jugada(self,jugador): #pide al jugador la fila y columna y realiza movimiento
        fila = int(input("Seleccione fila:"))
        columna = int(input("Seleccione columna:"))
        try:
            self.movimiento(jugador,fila,columna) #se realiza el movimiento
            self.jugadas += 1 #jugada realizada con exito
        except ValueError:
            raise ValueError("Jugada no valida")
        

    
    

    def jugada_IA(self,fila,columna):
        self.tablero[fila][columna] = 'o'
        self.jugadas += 1

      


        
        






            