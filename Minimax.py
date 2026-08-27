import tic_tac_toe

class Minimax:


    def __init__(self):
        self.tres_en_raya = tic_tac_toe.tic_tac_toe()        

    def algoritmo(self,tablero,jugador_max,profundidad): 

        if self.tres_en_raya.comprobar_minimax(tablero,'x') or profundidad == 0: #si ganan las x
            return self.heuristica(tablero), None
        elif self.tres_en_raya.comprobar_minimax(tablero,'o'): #si ganan las o
            return self.heuristica(tablero), None
            

        casillas_libres = any('-' in fila for fila in tablero) #si hay empate
        if not casillas_libres:
            return self.heuristica(tablero), None
        
        mejor_columna = None
        #mejor_fila = None

        if jugador_max: #si es el turno de max
            evaluacion_maxima = float('-inf')

            
            for col in range(len(tablero[0])): #recorre todo el tablero hasta encontrar una casilla en blanco
                fila_disponible = -1
                for fila in range(len(tablero) - 1, -1, -1):
                    if tablero[fila][col] == '-':
                        fila_disponible = fila
                        break

                    if fila_disponible == -1:
                        continue

                    tablero[fila_disponible][col] = 'o' #hace jugada
                    evaluacion, _ = self.algoritmo(tablero,False,profundidad - 1) #simula el juego con dicha jugada
                        
                    
                    tablero[fila_disponible][col] = '-' #"Deshacemos jugada para seguir buscando en el espectro de busqueda (Backtracking)"
                        
                    if evaluacion > evaluacion_maxima: #Si conseguimos una mejor jugada nos quedamos con la jugada
                        evaluacion_maxima = evaluacion
                        
                        mejor_columna = col

                        
            return evaluacion_maxima, mejor_columna #devolvemos la mejor jugada
        else: #si es el turno de min
            evaluacion_minima = float('inf')
            for col in range(len(tablero[0])): #recorre todo el tablero hasta encontrar una casilla en blanco
                fila_disponible = -1
                for fila in range(len(tablero) - 1, -1, -1):
                    if tablero[fila][col] == '-':
                        fila_disponible = fila
                        break

                    if fila_disponible == -1:
                        continue

                    tablero[fila_disponible][col] = 'o' #hace jugada
                    evaluacion, _ = self.algoritmo(tablero,False,profundidad - 1) #simula el juego con dicha jugada
                        
                    
                    tablero[fila_disponible][col] = '-' #"Deshacemos jugada para seguir buscando en el espectro de busqueda (Backtracking)"

                    if evaluacion < evaluacion_minima: #Si conseguimos una mejor jugada nos quedamos con la jugada
                        evaluacion_minima = evaluacion
                        
                        mejor_columna = col
            return evaluacion_minima, mejor_columna #devolvemos la mejor jugada
        

    def evaluar_ventana(self, ventana):
        puntuacion = 0
        

        count_ia = ventana.count('o')
        count_op = ventana.count('x')
        count_vacias = ventana.count("-")

        if count_ia == 4:
            puntuacion += 100000
        elif count_ia == 3 and count_vacias == 1:
            puntuacion += 5
        elif count_ia == 2 and count_vacias == 2:
            puntuacion += 2

        if count_op == 3 and count_vacias == 1:
            puntuacion -= 4 # Penaliza dejar al rival a una ficha de ganar

        return puntuacion

    def heuristica(self, tablero):
        ficha_ia = 'o'
        ficha_oponente = 'x'
        puntuacion = 0
        
        FILAS = 6
        COLUMNAS = 7

        # 1. Puntos por control del centro (Columna índice 3)
        columna_central = [tablero[r][3] for r in range(FILAS)]
        puntuacion += columna_central.count(ficha_ia) * 3

        # 2. Evaluación HORIZONTAL
        for f in range(FILAS):
            for c in range(COLUMNAS - 3):
                ventana = [tablero[f][c + i] for i in range(4)]
                puntuacion += self.evaluar_ventana(ventana)

        # 3. Evaluación VERTICAL
        for f in range(FILAS - 3):
            for c in range(COLUMNAS):
                ventana = [tablero[f + i][c] for i in range(4)]
                puntuacion += self.evaluar_ventana(ventana)
        # 4. Evaluación DIAGONAL DESCENDENTE (\)
        for f in range(FILAS - 3):
            for c in range(COLUMNAS - 3):
                ventana = [tablero[f + i][c + i] for i in range(4)]
                puntuacion += self.evaluar_ventana(ventana)

        # 5. Evaluación DIAGONAL ASCENDENTE (/)
        for f in range(3, FILAS):
            for c in range(COLUMNAS - 3):
                ventana = [tablero[f - i][c + i] for i in range(4)]
                puntuacion += self.evaluar_ventana(ventana)

        return puntuacion