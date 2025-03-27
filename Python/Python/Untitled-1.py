def hacer_menu():
    print("1. Registrar nuevo cliente.")
    print("2. Eliminar cliente.")
    print("0. Salir del sistema.")
    print("...seleccione una opcion...")
    opcion = int(input())

    return opcion
def tomar_cliente():
    nombre_cliente = input("Digite nombre: ")
    apellido_cliente = input("Digigte apellido: ")
    cedula_cliente = input("Dijite la cedula: ")
    info_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return info_cliente

def guardar_cliente(info_cliente, bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente
    
def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad nueva de clientes: "))
    for i in range(cantidad_nuevas):
        aux = tomar_cliente()
        aux_lista.append(aux)
    print(aux_lista)
    #return aux_lista

#*** zona de codigo principal ***
incluir_nueva_lista()

""""
while True:
    aux_opcion = hacer_menu()
    match aux_opcion:
        case 1:
            aux_info_cliente = tomar_cliente()
        case 2:
        aux_lista = incluir_nueva_lista()
        base_datos_cliente.extend(aux_lista)

base_datos_cliente = []
aux_opcion = hacer_menu()
aux_info_cliente = tomar_cliente()

aux_basedatos = guardar_cliente(aux_info_cliente, base_datos_cliente)
base_datos_cliente = aux_basedatos
print (base_datos_cliente)

aux_info_cliente = tomar_cliente()
aux_basedatos = guardar_cliente(aux_info_cliente, base_datos_cliente)
base_datos_cliente = aux_basedatos
print (base_datos_cliente)

aux_info_cliente = tomar_cliente()
aux_basedatos = guardar_cliente(aux_info_cliente, base_datos_cliente)
base_datos_cliente = aux_basedatos
print (base_datos_cliente)

aux_info_cliente = tomar_cliente()
aux_basedatos = guardar_cliente(aux_info_cliente, base_datos_cliente)
base_datos_cliente = aux_basedatos
print (base_datos_cliente)
"""
