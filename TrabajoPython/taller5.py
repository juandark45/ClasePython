def conversion_dolares_euros():
    dolares = float(input("Ingrese la cantidad en dólares: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio (dólares por euro): "))
    euros = dolares / tasa_cambio
    print(f"{dolares} dólares equivalen a {euros} euros.")

if __name__ == "__main__":
    conversion_dolares_euros()