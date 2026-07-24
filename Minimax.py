import tic_tac_toe
class Minimax:

    def __init__(self):
        self.juego = tic_tac_toe()

    def algoritmo(self,tablero,jugador_max):

        if self.juego.comprobar('x'):
            return -10
        elif self.juego.comprobar('o'):
            return 10
        elif self.juego.jugadas == 9:
            return 0

        
        if jugador_max:
            evaluacion_maxima = float('-inf')
            for jugada in tablero:
                evaluacion = self.algoritmo(jugada,False)
                evaluacion_maxima = max(evaluacion_maxima,evaluacion)
            return evaluacion_maxima
        else:
            evaluacion_minima = float('inf')
            for jugada in tablero:
                evaluacion = self.algoritmo(jugada,True)
                evaluacion_minima = min(evaluacion_minima,evaluacion)
            return evaluacion_minima
        

        