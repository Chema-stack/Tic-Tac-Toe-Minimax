import Minimax
import tic_tac_toe
import os
import platform
import time

class Juego:

    def __init__(self):
         self.tres_en_raya = tic_tac_toe.tic_tac_toe()
         self.inteligencia_artificial = Minimax.Minimax()


    def borrar_pantalla(self): #borra la consola, teniendo en cuenta el SO en el que te encuentras
         system_name = platform.system()

         if system_name == "Windows":
            os.system('cls')
         else:
            os.system('clear')
               

    def jugar_con_IA(self): #flujo de juego contra la IA
            #inteligencia_artificial = Minimax()
            self.borrar_pantalla() #borra terminal por estetica
            ganador = False
            while(self.tres_en_raya.jugadas < 42): #mientras haya menos de 42 jugadas
                self.tres_en_raya.imprimir_tablero() #imprime el tablero
                jugador = self.tres_en_raya.turno() #selecciona el jugador que le toca jugar
                if jugador == 'x':
                    try:
                        self.tres_en_raya.seleccionar_jugada(jugador) #el jugador selecciona la jugada que hara
                        self.borrar_pantalla()
                    except ValueError:
                        self.borrar_pantalla() #borra la terminal para imprimir el error
                        print("Jugada no valida, introduzca de nuevo su jugada.")
                else: #si la jugada es impar juega la IA
                    puntuacion,columna = self.inteligencia_artificial.algoritmo(self.tres_en_raya.tablero,True,4) #La IA piensa su jugada
                    print(columna)
                    self.tres_en_raya.jugada_IA(columna) #La IA realiza su jugada
                    self.borrar_pantalla()
    
                
                if self.tres_en_raya.comprobar(jugador): #comprueba si hay un ganador
                    print("Gana el jugador " + jugador)
                    ganador = True
                    break
            if not ganador: #si se llega a 9 jugadas y no hay ganador, entonces hay empate
                print("Empate")

    def jugar_1_vs_1(self): #realiza el flujo de juego
            self.borrar_pantalla() #borra terminal por estetica
            ganador = False
            while(self.tres_en_raya.jugadas < 42): #mientras haya menos de 42 jugadas
                self.tres_en_raya.imprimir_tablero() #imprime el tablero
                jugador = self.tres_en_raya.turno() #selecciona el jugador que le toca jugar
                print("turno de "+jugador)
                
                try:
                    self.tres_en_raya.seleccionar_jugada(jugador) #el jugador selecciona la jugada que hara
                    self.borrar_pantalla() #borra la terminal para imprimir la nueva jugada
                except ValueError:
                    self.borrar_pantalla() #borra la terminal para imprimir el error
                    
                    print("Jugada no valida, introduzca de nuevo su jugada.")
                    time.sleep(1)
                
    
                
                if self.tres_en_raya.comprobar(jugador): #comprueba si hay un ganador
                    print("Gana el jugador " + jugador)
                    ganador = True
                    break
            if not ganador: #si se llega a 9 jugadas y no hay ganador, entonces hay empate
                print("Empate")


