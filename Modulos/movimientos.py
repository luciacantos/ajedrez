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

