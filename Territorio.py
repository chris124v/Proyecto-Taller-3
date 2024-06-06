#Funcion de creacion del territorio 

def validacion(valor):

    for caracter in valor:
        if caracter not in "0123456789":
            return False
    return True

def obtener_tamaño(tamaño=None):

    if tamaño is not None:
        print("Ignorando el tamaño proporcionado...")
    while True:
        tamaño = input("Ingrese el tamaño del tablero (i x j): ")
        if validacion(tamaño):
            tamaño_tablero = int(tamaño)
            if 1 <= tamaño_tablero <= 24:
                return tamaño_tablero
            else:
                print("El tamaño del tablero debe ser entre 1 y 24.")
        else:
            print("Por favor, ingrese un número válido.")


def crear_tablero(tamano):
    tablero = [[0 for _ in range(tamano)] for _ in range(tamano)]
    return tablero


def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)


tamaño_tablero = obtener_tamaño()
tablero = crear_tablero(tamaño_tablero)
print("Tablero creado con tamaño {} x {}".format(len(tablero), len(tablero)))
imprimir_tablero(tablero)

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    leyenda = {
        0: " ",
        1: "I",
        2: "P",
        3: "AC",
        4: "U"
    }

    print("  ", end=" ")
    for i in range(len(tablero)):
        print(i + 1, end="  ")
    print()
    for i in range(len(tablero)):
        print(chr(65 + i), end="  ")
        for j in range(len(tablero)):
            print(leyenda[tablero[i][j]], end="  ")
        print()

imprimir_tablero(tablero)


