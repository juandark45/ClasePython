import math


def areas_figuras():
    radio = float(input("Ingrese el radio del círculo: "))
    lado = float(input("Ingrese el lado del cuadrado: "))
    area_circulo = math.pi * radio**2
    area_cuadrado = lado**2
    print(f"Área del círculo: {area_circulo}")
    print(f"Área del cuadrado: {area_cuadrado}")

if __name__ == "__main__":
    areas_figuras()
