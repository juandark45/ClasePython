def celsius_a_fahrenheit():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

if __name__ == "__main__":
    celsius_a_fahrenheit()