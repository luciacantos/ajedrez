#Importar modulos

from data.fichas import *
from tablero_inicial import *

def movimientos(tablero):
#inicializamos la variable movimiento en 0
    movimiento = 0

    while True:
        print("¿Quiere realizar algún movimiento?: ")
        respuesta = input("1)Sí  2)No : ")
        if respuesta == "1":
            print("Ingrese la posición de la ficha que quiere mover.")
            fila_o = int(input("Fila: ")) #fila de origen de la ficha que mueve
            columna_o = int(input("Columna: "))#columna de origen de la ficha que mueve
            print("Ingrese la posición de la casilla a la que quiere mover la ficha. ")
            fila_d = int(input("Fila: "))#fila destino de la ficha
            columna_d = int(input("Columna: "))#columna destino de la ficha
            print(" ")
            #coloca la ficha que mueve en la casilla destino
            tablero[fila_d - 1][columna_d - 1] = tablero[fila_o - 1][columna_o - 1]
            #coloca un espacio en la casilla origen para que desaparezca la ficha
            tablero[fila_o - 1][columna_o - 1] = " "

            #sumamos un movimiento al contador
            movimiento = movimiento + 1

            print(imprimir_tablero(tablero))
            print(" ")
            print("Movimientos realizados: ", movimiento)
        elif respuesta == "2":
            print("El tablero se quedará igual.")
            break
        else:
            print("ingrese una opcion valida")
