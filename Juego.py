import Minimax
import tic_tac_toe
import os

class Juego:

    def __init__(self):
         self.tres_en_raya = tic_tac_toe.tic_tac_toe()
         self.inteligencia_artificial = Minimax.Minimax()
         

    def jugar_con_IA(self):
            #inteligencia_artificial = Minimax()
            os.system('clear') #borra terminal por estetica
            ganador = False
            while(self.jugadas < 9): #mientras haya menos de 9 jugadas
                self.tres_en_raya.imprimir_tablero() #imprime el tablero
                jugador = self.tres_en_raya.turno() #selecciona el jugador que le toca jugar
                if jugador == 'x':
                    try:
                        self.tres_en_raya.seleccionar_jugada(jugador) #el jugador selecciona la jugada que hara
                        os.system('clear') #borra la terminal para imprimir la nueva jugada
                    except ValueError:
                        os.system('clear') #borra la terminal para imprimir el error
                        print("Jugada no valida, introduzca de nuevo su jugada.")
                else:
                    puntuacion,fila,columna = self.inteligencia_artificial.algoritmo(self.tablero,self.jugadas,False)
                    self.tres_en_raya.jugada_IA(fila,columna)
    
                
                if self.tres_en_raya.comprobar(jugador): #comprueba si hay un ganador
                    print("Gana el jugador " + jugador)
                    ganador = True
                    break
            if not ganador: #si se llega a 9 jugadas y no hay ganador, entonces hay empate
                print("Empate")

    def jugar_1_vs_1(self): #realiza el flujo de juego
            os.system('clear') #borra terminal por estetica
            ganador = False
            while(self.jugadas < 9): #mientras haya menos de 9 jugadas
                self.tres_en_raya.imprimir_tablero() #imprime el tablero
                jugador = self.tres_en_raya.turno() #selecciona el jugador que le toca jugar
                
                try:
                    self.tres_en_raya.seleccionar_jugada(jugador) #el jugador selecciona la jugada que hara
                    os.system('clear') #borra la terminal para imprimir la nueva jugada
                except ValueError:
                    os.system('clear') #borra la terminal para imprimir el error
                    print("Jugada no valida, introduzca de nuevo su jugada.")
                
    
                
                if self.tres_en_raya.comprobar(jugador): #comprueba si hay un ganador
                    print("Gana el jugador " + jugador)
                    ganador = True
                    break
            if not ganador: #si se llega a 9 jugadas y no hay ganador, entonces hay empate
                print("Empate")




prueba = Juego()
prueba.jugarjugar_1_vs_1()