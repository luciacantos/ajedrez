# importar fichas.py y usar las variables

from data.fichas import fichas_negras, peones_negros, fichas_blancas, peones_blancos

#tablero inicial
tablero = [fichas_negras, peones_negros,[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], peones_blancos, fichas_blancas]

#imprimir por pantalla con forma de tablero y los numeros de las filas y columnas
def imprimir_tablero(tablero):
    print("    1 2 3 4 5 6 7 8")
    print(" ")
    for i in range(8):
        print(i+1, end='  ')
        for j in range(8):
            print(tablero[i][j], end=' ')
        print()
