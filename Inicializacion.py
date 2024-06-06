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