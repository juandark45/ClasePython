def calcular_edad():
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    edad = 2024 - nacimiento
    print(f"Usted tiene {edad} años.")

if __name__ == "__main__":
    calcular_edad()