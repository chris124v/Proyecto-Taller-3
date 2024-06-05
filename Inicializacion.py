# Inicialización del juego
def nombre_usuario(nombre):

    if len(nombre) <= 15:
        print("Bienvenido a Topuria 3, un juego de estrategia")
        return nombre
    
    else:
        while len(nombre) > 15:
            print("El nombre no puede tener más de 15 caracteres.")
            nombre = input("Ingrese su nombre (máximo 15 caracteres): ")
            
        print("¡Bienvenido a Topuria 3, un juego de estrategia!")
        return nombre

nombre = input("Ingrese su nombre (máximo 15 caracteres): ")
nombre = nombre_usuario(nombre)
print("Bienvenido, {}!".format(nombre))



# Reglas del juego
print("Reglas del juego:")
print("1. El juego se desarrolla en un tablero de 30x30.")
print("2. El juego tiene turnos de día y noche.")
print("3. Durante el día, puedes hacer proyectos, iniciativas y actividades culturales.")
print("4. Durante la noche, los usurpadores toman territorio de manera random en el tablero.")
print("5. Ganas completando una fila o columna de proyectos.")
print("6. Pierdes si los usurpadores toman una fila o columna entera.")