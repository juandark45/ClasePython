def hacer_menu():
    print("1. Registrar nuevo cliente.")
    print("2. Eliminar cliente.")
    print("0. Salir del sistema.")
    print("...seleccione una opcion...")
    opcion = int(input())

    return opcion

#*** zona de codigo principal ***
aux_opcion = hacer_menu()