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

def main():
    print()
    nombre = nombre_usuario()
    print("Bienvenido, {}!".format(nombre))

main()

# Reglas del juego
def reglas_juego():

    print("\nReglas del juego:\n")
    print("1. El juego se desarrolla en un tablero de 30x30.")
    print("2. El juego tiene turnos de día y noche.")
    print("3. Durante el día, puedes hacer proyectos, iniciativas y actividades culturales.")
    print("4. Durante la noche, los usurpadores toman territorio de manera random en el tablero.")
    print("5. Ganas completando una fila o columna de proyectos.")
    print("6. Pierdes si los usurpadores toman una fila o columna entera.")
    print()

reglas_juego()