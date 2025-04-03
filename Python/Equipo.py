def equipo_pokemon():
    EquipoP = ("Pikachu", "Gliscor", "Drapion", "Sharkpido", "Trevenant", "Melenaleteo")
    OrdenE = ("Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto")

    print("1. Ordenar el equipo alfabéticamente")
    print("2. Invertir el equipo")
    print("3. Mostrar cada Pokémon con su posición")

    opcion = int(input("Ingrese una opción: "))

    return opcion, EquipoP, OrdenE  

def procesar_opcion(opcion, EquipoP, OrdenE):
    if opcion == 1:

        EquipoOrdenado = tuple(sorted(EquipoP))  
        print("Equipo ordenado:")
        for orden, pokemon in zip(OrdenE, EquipoOrdenado):
            print(f"{orden}: {pokemon}")

    elif opcion == 2:

        EquipoInvertido = tuple(reversed(EquipoP))  
        print("Equipo invertido:")
        for orden, pokemon in zip(OrdenE, EquipoInvertido):
            print(f"{orden}: {pokemon}")

    elif opcion == 3:
        print("Posiciones del equipo:")
        for orden, pokemon in zip(OrdenE, EquipoP):
            print(f"{orden}: {pokemon}")

    else:
        print("Opción no válida")

opcion, EquipoP, OrdenE = equipo_pokemon()
procesar_opcion(opcion, EquipoP, OrdenE)