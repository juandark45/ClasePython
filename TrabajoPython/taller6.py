def calcular_imc():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc}")

if __name__ == "__main__":
    calcular_imc()
