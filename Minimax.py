import tic_tac_toe

class Minimax:


    def __init__(self):
        self.tres_en_raya = tic_tac_toe.tic_tac_toe()        

    def algoritmo(self,tablero,jugador_max):

        if self.tres_en_raya.comprobar_minimax(tablero,'x'):
            return -10, None, None
        elif self.tres_en_raya.comprobar_minimax(tablero,'o'):
            return 10, None, None

        hay_casillas_libres = any('-' in fila for fila in tablero)
        if not hay_casillas_libres:
            return 0, None, None
        
        mejor_columna = None
        mejor_fila = None

        if jugador_max:
            evaluacion_maxima = float('-inf')
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == '-':
                        
                        tablero[i][j] = 'o'
                        evaluacion, _,_ = self.algoritmo(tablero,False)
                        tablero[i][j] = '-'
                        
                        if evaluacion > evaluacion_maxima:
                            evaluacion_maxima = evaluacion
                            mejor_fila = i
                            mejor_columna = j

                        
            return evaluacion_maxima, mejor_fila, mejor_columna
        else:
            evaluacion_minima = float('inf')
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == '-':
                        
                        tablero[i][j] = 'x'
                        evaluacion,_,_ = self.algoritmo(tablero,True)
                        tablero[i][j] = '-'

                        if evaluacion < evaluacion_minima:
                            evaluacion_minima = evaluacion
                            mejor_fila = i
                            mejor_columna = j
            return evaluacion_minima,mejor_fila, mejor_columna
        

        