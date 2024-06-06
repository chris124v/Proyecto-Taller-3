#Funcion de creacion del territorio 
def validacion(valor):
    """
    Verifica si el valor es un número.
    """
    for caracter in valor:
        if caracter not in "0123456789":
            return False
    return True

def obtener_tamaño(tamaño=None):
    """
    Solicita y valida el tamaño del tablero.
    Si el parámetro tamaño es proporcionado, se ignora y se solicita nuevamente al usuario.
    """
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
            print("\nPor favor, ingrese un número válido.\n")


def crear_tablero(tamaño):
    """
    Crea un tablero de tamaño especificado.
    """
    tablero = [[0 for _ in range(tamaño)] for _ in range(tamaño)]
    return tablero


tamaño_tablero = obtener_tamaño()
tablero = crear_tablero(tamaño_tablero)
print("\nTablero creado con tamaño {} x {}".format(len(tablero), len(tablero)))


