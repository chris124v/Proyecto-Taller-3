import random

# Inicialización del juego

def validacion_nombre(nombre):

    while len(nombre) > 15:
        print("\nEl nombre no puede tener más de 15 caracteres.\n")
        nombre = input("Ingrese su nombre (máximo 15 caracteres): ")

    return nombre

def nombre_usuario():

    nombre = input("\nIngrese su nombre (máximo 15 caracteres): ")
    nombre = validacion_nombre(nombre)
    print("\n¡Bienvenido a Topuria 3, un juego de estrategia!\n")
    return nombre

def no_al_alambrado():

    nombre = nombre_usuario()
    print("Bienvenido, {}!".format(nombre))

no_al_alambrado()

# Reglas del juego
def reglas_juego():

    print("\nReglas del juego:\n")
    print("1. El juego se desarrolla en un tablero de tamaño variable.")
    print("2. El juego tiene turnos de día y noche.")
    print("3. Durante el día, puedes hacer proyectos, iniciativas y actividades culturales.")
    print("4. Durante la noche, los usurpadores toman territorio de manera random en el tablero.")
    print("5. Ganas completando una fila o columna de proyectos.")
    print("6. Pierdes si los usurpadores toman una fila o columna entera.\n")

reglas_juego()

# Creación del tablero
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
        print("Tamaño erroneo")

    while True:
        tamaño = input("Ingrese el tamaño del tablero (i x j): ")
        if validacion(tamaño):
            tamaño_tablero = int(tamaño)
            if 1 <= tamaño_tablero <= 24:
                return tamaño_tablero
            else:
                print("\nEl tamaño del tablero debe ser entre 1 y 24.\n")
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

        
# Función para imprimir el tablero
def imprimir_tablero(tablero):

    i= 0
    j= 0

    leyenda = {
        0: " ",
        1: "I",
        2: "P",
        3: "A",
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

def menu_principal():

    while True:
        print("\nMenú principal:\n")
        print("1. ASCII Art de la comunidad")
        print("2. Ver las reglas")
        print("3. Entrada al tablero")
        print("4. Datos de Pueblos Originarios")
        print("5. Datos de Solar Punk")
        print("6. Datos de Cabagra")
        print("7. Salir del juego\n")
        opcion = int(input("Ingrese una opción:   "))
        print()

        if opcion == 3:
            break

        elif opcion == 7:
            print("\nGracias por jugar!\n")
            exit()

        else:
            print("\nOpción no válida. Intente de nuevo.\n")

menu_principal()
imprimir_tablero(tablero)

# Turnos
def turno_dia(tablero, tamaño_tablero):
    
    i = 0
    j = 0
    x = 0
    
    print("\nTurno de día\n")
    print("Menú turnos:\n")
    print("1. Iniciativa")
    print("2. Proyecto")
    print("3. Actividad cultural\n")

    # Validación de opción de turno
    while True:

        opcion_turno = input("Ingrese una opción: ")
        opcion_valida = True

        for numero in opcion_turno:
            if numero not in "0123456789":
                opcion_valida = False
                break

        if opcion_valida:
            opcion_turno = int(opcion_turno)
            
            if 1 <= opcion_turno <= 3:
                break

        print("\nError: El dígito que ingresó es incorrecto. Debe ser 1, 2 o 3.\n")

    # Validación de fila y columna
    while True:

        fila = input("\nIngrese la fila (A-{}): ".format(chr(64 + tamaño_tablero))).upper()
        columna = input("\nIngrese la columna (1-{}): ".format(tamaño_tablero))
        
        fila_valida = True
        columna_valida = True
        
        for letra in fila:
            if letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(fila) != 1 or not ('A' <= fila <= chr(64 + tamaño_tablero)):
                fila_valida = False
                break

        for numero in columna:
            if numero not in "0123456789":
                columna_valida = False
                break
        
        if fila_valida and columna_valida:
            columna = int(columna)
            if 1 <= columna <= tamaño_tablero:
                filitas = ord(fila) - 65
                columnitas = columna - 1
                break

        print("\nError: El dígito o letra que ingresó es incorrecto. Intente nuevamente.\n")

    if opcion_turno == 1:

        if tablero[filitas][columnitas] == 0 or tablero[filitas][columnitas] == 3:
            tablero[filitas][columnitas] = 1
        else:
            print("\nNo se puede establecer una iniciativa en ese espacio.")
            
    elif opcion_turno == 2:

        if tablero[filitas][columnitas] == 0 or tablero[filitas][columnitas] == 1 or tablero[filitas][columnitas] == 3:
            tablero[filitas][columnitas] = 2
        else:
            print("\nNo se puede establecer un proyecto en ese espacio.")

    elif opcion_turno == 3:

        if tablero[filitas][columnitas] == 0:
            tablero[filitas][columnitas] = 3

            while True:
                expansion = input("\nIngrese la expansión (filas o columnas): ").lower()
                if expansion in ["filas", "columnas"]:
                    break
                else:
                    print("Error: La expansión ingresada es incorrecta. Debe ser 'filas' o 'columnas'.")

            if expansion == "filas":
                for i in range(tamaño_tablero):
                    if tablero[filitas][i] == 0:
                        tablero[filitas][i] = 3
                    else:
                        break

            elif expansion == "columnas":
                for i in range(tamaño_tablero):
                    if tablero[i][columnitas] == 0:
                        tablero[i][columnitas] = 3
                    else:
                        break
        else:
            print("\nNo se puede establecer una actividad cultural en ese espacio.")

    print()
    imprimir_tablero(tablero)

    # Verificar ganador o perdedor
    for i in range(tamaño_tablero):
        fila_completa_proyectos = True
        fila_completa_usurpadores = True

        for x in tablero[i]:
            if x != 2:
                fila_completa_proyectos = False
            if x != 4:
                fila_completa_usurpadores = False

        if fila_completa_proyectos:
            print("¡Ganaste! Completaste una fila de proyectos.")
            exit()

        if fila_completa_usurpadores:
            print("¡Perdiste! Los usurpadores tomaron una fila entera.")
            exit()
    
    for i in range(tamaño_tablero):
        columna_completa_proyectos = True
        columna_completa_usurpadores = True

        for j in range(tamaño_tablero):
            if tablero[j][i] != 2:
                columna_completa_proyectos = False
            if tablero[j][i] != 4:
                columna_completa_usurpadores = False

        if columna_completa_proyectos:
            print("¡Ganaste! Completaste una columna de proyectos.")
            exit()

        if columna_completa_usurpadores:
            print("¡Perdiste! Los usurpadores tomaron una columna entera.")
            exit()


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

def turno_noche(tablero, tamaño_tablero):

    print("\nTurno de noche\n")
    usurpadores(tablero, tamaño_tablero)
    imprimir_tablero(tablero)

def turnos():

    turno = "día"
    while True:
        if turno == "día":
            turno_dia(tablero, tamaño_tablero)
            turno = "noche"
        else:
            turno_noche(tablero, tamaño_tablero)
            turno = "día"

turnos()