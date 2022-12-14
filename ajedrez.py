##from Modulos import tablero_inicial

fichas_negras = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
peones_negros = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
fichas_blancas = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
peones_blancos = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']

tablero = [fichas_negras, peones_negros,[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], peones_blancos, fichas_blancas]

def imprimir_tablero(tablero):
    print("    1 2 3 4 5 6 7 8")
    print(" ")
    for i in range(8):
        print(i+1, end='  ')
        for j in range(8):
            print(tablero[i][j], end=' ')
        print()

if __name__ == '__main__':
    imprimir_tablero(tablero)

def movimientos(tablero):

    movimiento = 0

    while True:
        print("¿Quiere realizar algún movimiento?: ")
        respuesta = input("1)Sí  2)No : ")
        if respuesta == "1":
            print("Ingrese la posición de la ficha que quiere mover.")
            fila_o = int(input("Fila: "))
            columna_o = int(input("Columna: "))
            print("Ingrese la posición de la casilla a la que quiere mover la ficha. ")
            fila_d = int(input("Fila: "))
            columna_d = int(input("Columna: "))
            print(" ")
            tablero[fila_d - 1][columna_d - 1] = tablero[fila_o - 1][columna_o - 1]
            tablero[fila_o - 1][columna_o - 1] = " "

            movimiento = movimiento + 1

            print(imprimir_tablero(tablero))
            print("Movimiento N°", movimiento)
        elif respuesta == "2":
            print("El tablero se quedará igual.")
            print("Ha realizado", movimiento, " movimientos.")
            break
        else:
            print("ingrese una opcion valida")

if __name__ == '__main__':
    movimientos(tablero)
