class Cliente: 
    #Metodo constructor
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.cedula = ""

    #Metodos basicos
    def set_nombre (self, dato_nombre):
        self.nombre = dato_nombre
    

    def get_nombre(self):
        return self.nombre
    
    def pagar(self):
        return "Cliente no tiene efectivo"
    
    def imprimir_datos(self):
        mensaje = "Nombre: " + self.nombre 
        print(mensaje)
