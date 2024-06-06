import random

def usurpadores(tablero, tamaño_tablero):

    i= 0

    fila_o_columna = random.choice(["fila", "columna"])

    if fila_o_columna == "fila":
        fila = random.randint(0, tamaño_tablero - 1)
        cantidad_espacios = random.randint(2, 6)

        for i in range(cantidad_espacios):

            if fila + i < tamaño_tablero:
                if tablero[fila][i] == 0 or tablero[fila][i] == 2:
                    tablero[fila][i] = 4
                else:
                    break

    else:
        columna = random.randint(0, tamaño_tablero - 1)
        cantidad_espacios = random.randint(2, 6)

        for i in range(cantidad_espacios):
            if columna + i < tamaño_tablero:
                if tablero[i][columna] == 0 or tablero[i][columna] == 2:
                    tablero[i][columna] = 4
                else:
                    break
