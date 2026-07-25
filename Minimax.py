import tic_tac_toe

class Minimax:


    def __init__(self):
        self.tres_en_raya = tic_tac_toe.tic_tac_toe()        

    def algoritmo(self,tablero,jugadas,jugador_max):

        if self.tres_en_raya.comprobar_minimax(tablero,'x'):
            return -10, None, None
        elif self.tres_en_raya.comprobar_minimax(tablero,'o'):
            return 10, None, None
        elif jugadas == 9:
            return 0, None, None

        mejor_columna = None
        mejor_fila = None

        if jugador_max:
            evaluacion_maxima = float('-inf')
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == '-':
                        
                        tablero[i][j] = 'o'
                        jugadas += 1
                        evaluacion, _,_ = self.algoritmo(tablero,jugadas,False)
                        tablero[i][j] = '-'
                        jugadas -= 1
                        
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
                        jugadas += 1
                        evaluacion,_,_ = self.algoritmo(tablero,jugadas,True)
                        tablero[i][j] = '-'
                        jugadas -= 1

                        if evaluacion < evaluacion_minima:
                            evaluacion_minima = evaluacion
                            mejor_fila = i
                            mejor_columna = j
            return evaluacion_minima,mejor_fila, mejor_columna
        

        