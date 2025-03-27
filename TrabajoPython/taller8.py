import math


def volumenes_figuras():
    lado = float(input("Ingrese el lado del cubo: "))
    radio = float(input("Ingrese el radio de la esfera: "))
    volumen_cubo = lado**3
    volumen_esfera = (4/3) * math.pi * radio**3
    print(f"Volumen del cubo: {volumen_cubo}")
    print(f"Volumen de la esfera: {volumen_esfera}")

if __name__ == "__main__":
    volumenes_figuras()