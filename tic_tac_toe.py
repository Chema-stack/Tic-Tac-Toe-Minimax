class Juego:
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    def normalizador(fila,columna): #Esta funcion normaliza los movimientos
        return fila - 1, columna - 1 #Le quita a la fila y a la columna uno
                                    #para que entre en los limites de la matriz

    