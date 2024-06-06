#Turno de dia 
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

        print("Error: El dígito que ingresó es incorrecto. Debe ser 1, 2 o 3.")

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

        print("Error: El dígito o letra que ingresó es incorrecto. Intente nuevamente.")

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

def turno_noche(tablero, tamaño_tablero):

    print("\nTurno de noche\n")

def turnos(tablero, tamaño_tablero):
    turno = "día"
    while True:
        if turno == "día":
            turno_dia(tablero, tamaño_tablero)
            turno = "noche"
        else:
            turno_noche(tablero, tamaño_tablero)
            turno = "día"

turnos()