class Animal:
    # Metodo constructor  
    def __init__(self, dato_tamaño, dato_edad, dato_raza):
        #Todo lo que este en el constructor se combierten en atributos 
        self.tamaño = dato_tamaño
        self.edad = dato_edad
        self.raza = dato_raza
        self.estado = self.llorar()
        #metodos basicos 
    
    def llorar (self):
        Mensaje = "animal llora"
        print(Mensaje)

    def comer (self):
        Mensaje = "animal comiendo"
        return Mensaje
    
    def dormir (self):
        Mensaje = "animal durmiendo"
        return Mensaje
    
    def imprimir_info(self):
        mensaje =  "Tamaño: " +self.tamaño + "\n"+ "Edad: " +self.edad +"\n"+ "Raza: " +self.raza
        print(mensaje)