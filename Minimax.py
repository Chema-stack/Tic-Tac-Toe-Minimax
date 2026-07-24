import tic_tac_toe
class Minimax:
        

    def algoritmo(self,tablero,jugadas,jugador_max):

        if self.juego.comprobar('x'):
            return -10
        elif self.juego.comprobar('o'):
            return 10
        elif jugadas == 9:
            return 0

        
        if jugador_max:
            evaluacion_maxima = float('-inf')
            for i in range(tablero):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == '-':
                        tablero[i][j] = 'o'
                        jugadas += 1
                        evaluacion = self.algoritmo(tablero,jugadas,False)
                        evaluacion_maxima = max(evaluacion_maxima,evaluacion)
            return evaluacion_maxima
        else:
            evaluacion_minima = float('inf')
            for i in range(tablero):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == '-':
                        tablero[i][j] = 'x'
                        jugadas += 1
                        evaluacion = self.algoritmo(tablero,jugadas,True)
                        evaluacion_minima = min(evaluacion_minima,evaluacion)
            return evaluacion_minima
        

        