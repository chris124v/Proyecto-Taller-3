#Menu principal que lleva al tablero y a los lugares con datos de pueblos originarios
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