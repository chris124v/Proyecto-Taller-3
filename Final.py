#Proyecto Programado 3
#Juego de Tablero en la region de Topuria
#Jervis Fabricio Esquivel Solano y Christopher Daniel Vargas Villalta
#Este es un juego por turnos de tablero cuyo objetivo se reduce a intentar completar filas o columnas con proyectos para ganar
import random

# Inicialización del juego

def validacion_nombre(nombre): 
    '''Funcion que utiliza while para hacer ciclos sobre el recorrido del len para asegurarse que no tenga mas de 15 caracteres'''

    while len(nombre) > 15:
        print("\nEl nombre no puede tener más de 15 caracteres.\n")
        nombre = input("Ingrese su nombre (máximo 15 caracteres): ")

        """input para agregar el nombre del jugador"""

    """retorna el nombre como dato"""
    return nombre

"""Funcion para agregar el nombre"""
def nombre_usuario():

    """Se agrega el nombre y se enlaza a validacion nombre"""
    nombre = input("\nIngrese su nombre (máximo 15 caracteres): ")
    nombre = validacion_nombre(nombre)
    print("\n¡Bienvenido a Topuria 3, un juego de estrategia!\n")
    """Print de bienvenida"""
    return nombre

"""Funcion para evitar el alambrado agregando variables dentro"""
def no_al_alambrado():

    nombre = nombre_usuario()
    """Se genera una relacion entre nombre y nombre usuario"""
    print("Bienvenido, {}!".format(nombre))

no_al_alambrado()

"""Funcion para mostrar las reglas del juego"""
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
        """Salida de validacion"""

    while True:
        tamaño = input("Ingrese el tamaño del tablero (i x j): ")
        """Se ingresa el tamaño del tablero"""

        if validacion(tamaño):
            tamaño_tablero = int(tamaño)
            if 1 <= tamaño_tablero <= 24:
                return tamaño_tablero
            else:
                print("\nEl tamaño del tablero debe ser entre 1 y 24.\n")
                """Se verifica que el tamaño no sea mayor a 24"""
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
print("\nTablero creado con tamaño {} x {}".format(len(tablero), len(tablero))) #se usa un .format para mostrar los len del tablero en columna y filas

        
"""Función para imprimir el tablero"""
def imprimir_tablero(tablero):

    i= 0
    j= 0
    """Asigna un tipo de nombre a cada valor dentro de la matriz"""

    leyenda = {
        0: " ", #Vacio
        1: "I", #Iniciativa
        2: "P", #Proyectos
        3: "A", #Actividades culturales
        4: "U" #Usurpadores
    }

    print("  ", end=" ")
    """Recorre el tablero"""
    for i in range(len(tablero)):
        print(i + 1, end="  ")
    print()
    for i in range(len(tablero)):
        print(chr(65 + i), end="  ")
        for j in range(len(tablero)):
            print(leyenda[tablero[i][j]], end="  ")
        print()

"""Funcion para hacer un menu principal con opciones"""
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

"""Funcion del turno del día (Turno del jugador para hacer proyectos, inciativas y actividades culturales)"""
def turno_dia(tablero, tamaño_tablero):

    """
    Esta funcion lo que hace es que mediante un ciclo while realiza las validaciones para la digitacion de numeros y letras incorrectas
    Posterior a esto en otro ciclo while basandose en un menu de 1 a 3 podra escoger si quiere hacer una actividad cultural, iniciativa y proyecto
    Tambien posee una forma de recorrer la matriz en cada turno para que en caso de que el jugador haya completado la columna o lista ganas
    y si el usurpador completa una fila o una columna pierde.

    """
    
    i = 0   #Inicializacion de variables para recorrer la matriz
    j = 0
    x = 0
    
    """Opciones de escogencia del tipo de actividad que quiere hacer el jugador"""

    print("\nTurno de día\n") 
    print("Menú turnos:\n")
    print("1. Iniciativa")
    print("2. Proyecto")
    print("3. Actividad cultural\n")

    """Validación de opción de turno"""
    while True:

        opcion_turno = input("Ingrese una opción: ")
        opcion_valida = True

        """Se itera sobre cada carácter de la opción ingresada"""
        for numero in opcion_turno: 

            """Primera validacion si el digito dado esta fuera del rango de 1 a 9"""
            if numero not in "0123456789": 
                opcion_valida = False 
                """Si no esta pasa a opcion valida dando un mensaje de incorrecto."""
                break
        
        """Si la opción es válida, se sale del bucle"""
        if opcion_valida:
            opcion_turno = int(opcion_turno)
            
            if 1 <= opcion_turno <= 3:  
                break

        print("\nError: El dígito que ingresó es incorrecto. Debe ser 1, 2 o 3.\n") #Aqui estaria el mensaje de error 

    """Validación de fila y columna"""
    while True:

        """Se solicita al usuario que ingrese una fila y una columna usamos chr para simplificar el uso de letras y numeros para ubicar la posicion"""
        fila = input("\nIngrese la fila (A-{}): ".format(chr(64 + tamaño_tablero))).upper() 
        columna = input("\nIngrese la columna (1-{}): ".format(tamaño_tablero))
        
        fila_valida = True
        columna_valida = True
        
        """Validaciones de la fila ingresada segun el tamaño del tablero, si o si"""

        for letra in fila:
            if letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(fila) != 1 or not ('A' <= fila <= chr(64 + tamaño_tablero)):
                """Si no cumple con las condiciones, se marca la fila como inválida"""
                fila_valida = False
                break

        """Validaciones de columna, esto tomando en cuenta que letras son filas y columnas son los numeros"""
        for numero in columna:
            if numero not in "0123456789":
                columna_valida = False
                break
        
        """Si la fila y la columna son válidas, se calculan los índices correspondientes y se sale del bucle"""
        if fila_valida and columna_valida:
            columna = int(columna)
            if 1 <= columna <= tamaño_tablero:
                """Si la fila y la columna son válidas, se calculan los índices correspondientes""" 
                filitas = ord(fila) - 65
                columnitas = columna - 1
                break

        print("\nError: El dígito o letra que ingresó es incorrecto. Intente nuevamente.\n")

    """En caso de que escoga iniciativas"""
    if opcion_turno == 1: 

        """Si hay un espacio vacio o una actividad cultural"""
        if tablero[filitas][columnitas] == 0 or tablero[filitas][columnitas] == 3: 
            tablero[filitas][columnitas] = 1 
            """Lo reemplzara por iniciativa"""

        else:
            print("\nNo se puede establecer una iniciativa en ese espacio.") 
            """Si hay un usurpador o un proyecto no puede reemplazarlo"""
            
    elif opcion_turno == 2: 
        """En caso de que escoga 2 que es proyecto podra reemplazarlo por todo"""

        if tablero[filitas][columnitas] == 0 or tablero[filitas][columnitas] == 1 or tablero[filitas][columnitas] == 3 or tablero[filitas][columnitas] == 4:
            tablero[filitas][columnitas] = 2 
            """Aqui cambia el valor en el tablero"""

        else:
            print("\nNo se puede establecer un proyecto en ese espacio.")

    elif opcion_turno == 3: 
        """Este seria la opcion de actividades culturales y su expansion"""

        if tablero[filitas][columnitas] == 0: 
            """Aqui define que solo puede cambiarlo en espacios vacios"""

            tablero[filitas][columnitas] = 3 
            """Reemplaza el espacio vacio para añadir la expansion de las actividades culturales"""

            """Aqui inicia el bucle while si es verdadero"""
            while True: 
                expansion = input("\nIngrese la expansión (filas o columnas): ").lower() 
                """Permite el uso de minusculas y mayusculas"""

                """Pasa al siguiente if"""
                if expansion in ["filas", "columnas"]:
                    break 

        
                else:
                    print("Error: La expansión ingresada es incorrecta. Debe ser 'filas' o 'columnas'.")

            """En caso de filas aumenta el indice y recorre la matriz poniendo en las filas la A de actividad cultural"""
            if expansion == "filas": 

                for i in range(tamaño_tablero):
                    
                    """Si es espacio vacio va asignar la actividad cultural en la matriz"""
                    if tablero[filitas][i] == 0: 
                        tablero[filitas][i] = 3

                    else:
                        break 
                    """Pasa a la siguiente funcion"""

            elif expansion == "columnas":
                """En caso de que se escoga columna recorre las columnas de la misma forma que las filas"""

                """Utiliza range para tomar en cuenta el tamaño del tablero"""
                for i in range(tamaño_tablero): 
                    if tablero[i][columnitas] == 0:
                        tablero[i][columnitas] = 3
                    else:
                        break
        else:
            print("\nNo se puede establecer una actividad cultural en ese espacio.") 
            """En caso de que intente poner una actividad cultural en un espacio que no sea vacio"""

    print()
    imprimir_tablero(tablero)

    """Verificar ganador o perdedor"""
    for i in range(tamaño_tablero):
        fila_completa_proyectos = True
        fila_completa_usurpadores = True

        """En caso de que sean diferentes de 2 o 4 para determinar el ganar o perder no se realiza la funcion de exit"""
        for x in tablero[i]: 
            """Utiliza la variable x para recorrer los espacios del tablero"""

            if x != 2:
                fila_completa_proyectos = False
            if x != 4:
                fila_completa_usurpadores = False

        if fila_completa_proyectos: 
            """Si se comprueba que es true entonces da el print de finalizacion"""

            print("¡Ganaste! Completaste una fila de proyectos.")
            exit()

        if fila_completa_usurpadores: 
            """Si se comprueba que es true que los usurpadores tomaron toda la fila entonces se da el mensaje de perdiste."""
            print("¡Perdiste! Los usurpadores tomaron una fila entera.")
            exit()
    
    """Es la misma funcion que la anterior solo que en este caso lo realiza con las columnas"""
    for i in range(tamaño_tablero):
        columna_completa_proyectos = True
        columna_completa_usurpadores = True

        for j in range(tamaño_tablero):

            if tablero[j][i] != 2:
                columna_completa_proyectos = False
            if tablero[j][i] != 4:
                columna_completa_usurpadores = False

        if columna_completa_proyectos: 
            """Se comprueba que si es True da el mesaje de ganaste"""

            print("¡Ganaste! Completaste una columna de proyectos.")
            exit()

        if columna_completa_usurpadores: 
            """Si se comprueba que es true que los usurpadores tomaron toda la columna entonces se da el mensaje de perdiste."""

            print("¡Perdiste! Los usurpadores tomaron una columna entera.")
            exit()

"""Funcion de los usurpadores"""
def usurpadores(tablero, tamaño_tablero):

    """
    Función que crea usurpadores en el tablero de juego.
    Tablero: Una matriz que representa el tablero de juego.
    Tamaño_tablero: El tamaño del tablero de juego.

    """

    i= 0 
    """Inicializacion del recorrido de la matriz"""

    fila_o_columna = random.choice(["fila", "columna"]) 
    """Variable de la fila o columna para la expansion de los usurpadores"""

    """Esto es en caso de escoga fila"""

    if fila_o_columna == "fila":
        fila = random.randint(0, tamaño_tablero - 1) 
        """Elimina la posicion 0"""
        cantidad_espacios = random.randint(2, 6) 
        """Puede poner espacios de 2 a 6"""

        for i in range(cantidad_espacios):

            """Se recorre la cantidad de espacios elegida para colocar usurpadores en la fila"""
            if fila + i < tamaño_tablero:

                """Si la posición actual está dentro del tamaño del tablero cambia 0 o 2 por 4 que son los usurpadores"""
                if tablero[fila][i] == 0 or tablero[fila][i] == 2:
                    tablero[fila][i] = 4
                else:
                    break
    
        """El else lo que logra es cuando la maquina escoge columna"""
    else:
        columna = random.randint(0, tamaño_tablero - 1)
        cantidad_espacios = random.randint(2, 6)

        for i in range(cantidad_espacios):

            if columna + i < tamaño_tablero:
                if tablero[i][columna] == 0 or tablero[i][columna] == 2:
                    tablero[i][columna] = 4
                else:
                    break

"""Funcion que realiza el turno de noche, simplemente llama a las funciones ya realizadas para hacer el print del tablero con los usurpadores"""
def turno_noche(tablero, tamaño_tablero):

    print("\nTurno de noche\n")
    usurpadores(tablero, tamaño_tablero)
    imprimir_tablero(tablero)

"""Funcion de los turnos, toma las dos funciones anteriormente realizadas y despues de hacer una hace la otra"""
def turnos():
    turno = "día" 
    """Se inicializa el primer turno como "día"""

    while True:
        if turno == "día":
            turno_dia(tablero, tamaño_tablero)
            turno = "noche" 
            """Se cambia a noche para cuando termine el turno del dia"""
            
        else:
            turno_noche(tablero, tamaño_tablero)
            turno = "día"

turnos()