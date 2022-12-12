# importar fichas.py y usar las variables

from data.fichas import *

tablero = [fichas_negras, peones_negros,[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], peones_blancos, fichas_blancas]

def imprimir_tablero_inicial(tablero):
    print("    1 2 3 4 5 6 7 8")
    print(" ")
    for i in range(8):
        print(i+1, end='  ')
        for j in range(8):
            print(tablero[i][j], end=' ')
        print()
