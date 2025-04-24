from Animal import Animal
from CLiente import Cliente

perro = Animal("pequeño", "2 años", "Labrador")
aux_accion = perro.comer()
print(aux_accion)

perro.imprimir_info()

obj_cliente = Cliente()
dato_nombre = obj_cliente.get_nombre()
print (dato_nombre)
obj_cliente.set_nombre("Juan")
print(obj_cliente.get_nombre())

