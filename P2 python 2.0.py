# Empresa de logística

# Estructuras para almacenar datos
clientes = {}  # Diccionario para almacenar clientes (clave: ID, valor: tupla con datos del cliente)
bienes = {}    # Diccionario para almacenar bienes (clave: ID del cliente, valor: lista de bienes)

def menu_principal():
    while True:
        print("\nBienvenido a la empresa de logística")
        print("1. Gestión de clientes")
        print("2. Gestión de bienes")
        print("3. Salir")
        opcion = int(input("Escoja una opción: "))

        if opcion == 1:
            menu_de_los_clientes()
        elif opcion == 2:
            menu_de_bienes()
        elif opcion == 3:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_de_los_clientes():
    while True:
        print("\nMenú de Clientes")
        print("1. Ingresar un nuevo cliente")
        print("2. Modificar un cliente existente")
        print("3. Eliminar un cliente")
        print("4. Mostrar la información de todos los clientes")
        print("5. Mostrar la información de un cliente específico")
        print("6. Volver al menú principal")
        opcion = int(input("Escoja una opción: "))

        if opcion == 1:
            ingresar_cliente()
        elif opcion == 2:
            modificar_cliente()
        elif opcion == 3:
            eliminar_cliente()
        elif opcion == 4:
            mostrar_todos_los_clientes()
        elif opcion == 5:
            mostrar_cliente_especifico()
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def ingresar_cliente():
    print("\nIngrese los datos del cliente:")
    id_cliente = input("Identificación: ")
    if id_cliente in clientes:
        print("El cliente ya existe.")
        return
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    clientes[id_cliente] = (nombre, apellido, telefono, direccion)
    bienes[id_cliente] = []  # Inicializar lista de bienes para el cliente
    print("Cliente agregado exitosamente.")

def modificar_cliente():
    id_cliente = input("\nIngrese la identificación del cliente a modificar: ")
    if id_cliente not in clientes:
        print("El cliente no existe.")
        return
    print("Ingrese los nuevos datos del cliente (deje en blanco para no modificar):")
    nombre = input(f"Nombre ({clientes[id_cliente][0]}): ") or clientes[id_cliente][0]
    apellido = input(f"Apellido ({clientes[id_cliente][1]}): ") or clientes[id_cliente][1]
    telefono = input(f"Teléfono ({clientes[id_cliente][2]}): ") or clientes[id_cliente][2]
    direccion = input(f"Dirección ({clientes[id_cliente][3]}): ") or clientes[id_cliente][3]
    clientes[id_cliente] = (nombre, apellido, telefono, direccion)
    print("Cliente modificado exitosamente.")

def eliminar_cliente():
    id_cliente = input("\nIngrese la identificación del cliente a eliminar: ")
    if id_cliente not in clientes:
        print("El cliente no existe.")
        return
    del clientes[id_cliente]
    del bienes[id_cliente]
    print("Cliente eliminado exitosamente.")

def mostrar_todos_los_clientes():
    print("\nLista de todos los clientes:")
    for id_cliente, datos in clientes.items():
        print(f"ID: {id_cliente}, Nombre: {datos[0]} {datos[1]}, Teléfono: {datos[2]}, Dirección: {datos[3]}")

def mostrar_cliente_especifico():
    id_cliente = input("\nIngrese la identificación del cliente: ")
    if id_cliente not in clientes:
        print("El cliente no existe.")
        return
    datos = clientes[id_cliente]
    print(f"ID: {id_cliente}, Nombre: {datos[0]} {datos[1]}, Teléfono: {datos[2]}, Dirección: {datos[3]}")

def menu_de_bienes():
    while True:
        print("\nMenú de Bienes")
        print("1. Registrar un artículo nuevo")
        print("2. Modificar un artículo existente")
        print("3. Eliminar un artículo")
        print("4. Listar bienes por cliente")
        print("5. Listar bienes disponibles")
        print("6. Volver al menú principal")
        opcion = int(input("Escoja una opción: "))

        if opcion == 1:
            registrar_bien()
        elif opcion == 2:
            modificar_bien()
        elif opcion == 3:
            eliminar_bien()
        elif opcion == 4:
            listar_bienes_por_cliente()
        elif opcion == 5:
            listar_bienes_disponibles()
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_bien():
    id_cliente = input("\nIngrese la identificación del cliente: ")
    if id_cliente not in clientes:
        print("El cliente no existe.")
        return
    print("Ingrese los datos del bien:")
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad: "))
    disponibilidad = input("¿Está disponible? (sí/no): ").lower() == "sí"
    bienes[id_cliente].append({"nombre": nombre, "cantidad": cantidad, "disponibilidad": disponibilidad})
    print("Artículo registrado exitosamente.")

def modificar_bien():
    id_cliente = input("\nIngrese la identificación del cliente: ")
    if id_cliente not in bienes or not bienes[id_cliente]:
        print("El cliente no tiene bienes registrados.")
        return
    listar_bienes_por_cliente(id_cliente)
    indice = int(input("Ingrese el índice del bien a modificar: "))
    if indice < 0 or indice >= len(bienes[id_cliente]):
        print("Índice no válido.")
        return
    bien = bienes[id_cliente][indice]
    print("Ingrese los nuevos datos del bien (deje en blanco para no modificar):")
    nombre = input(f"Nombre ({bien['nombre']}): ") or bien['nombre']
    cantidad = input(f"Cantidad ({bien['cantidad']}): ")
    cantidad = int(cantidad) if cantidad else bien['cantidad']
    disponibilidad = input(f"Disponibilidad ({'sí' if bien['disponibilidad'] else 'no'}): ").lower()
    disponibilidad = disponibilidad == "sí" if disponibilidad else bien['disponibilidad']
    bienes[id_cliente][indice] = {"nombre": nombre, "cantidad": cantidad, "disponibilidad": disponibilidad}
    print("Artículo modificado exitosamente.")

def eliminar_bien():
    id_cliente = input("\nIngrese la identificación del cliente: ")
    if id_cliente not in bienes or not bienes[id_cliente]:
        print("El cliente no tiene bienes registrados.")
        return
    listar_bienes_por_cliente(id_cliente)
    indice = int(input("Ingrese el índice del bien a eliminar: "))
    if indice < 0 or indice >= len(bienes[id_cliente]):
        print("Índice no válido.")
        return
    bienes[id_cliente].pop(indice)
    print("Artículo eliminado exitosamente.")

def listar_bienes_por_cliente(id_cliente=None):
    if not id_cliente:
        id_cliente = input("\nIngrese la identificación del cliente: ")
    if id_cliente not in bienes or not bienes[id_cliente]:
        print("El cliente no tiene bienes registrados.")
        return
    print(f"\nBienes del cliente {id_cliente}:")
    for i, bien in enumerate(bienes[id_cliente]):
        print(f"{i}. Nombre: {bien['nombre']}, Cantidad: {bien['cantidad']}, Disponibilidad: {'sí' if bien['disponibilidad'] else 'no'}")

def listar_bienes_disponibles():
    print("\nLista de bienes disponibles:")
    for id_cliente, lista_bienes in bienes.items():
        for bien in lista_bienes:
            if bien["disponibilidad"]:
                print(f"Cliente {id_cliente}: Nombre: {bien['nombre']}, Cantidad: {bien['cantidad']}")

# Ejecutar el programa
menu_principal()