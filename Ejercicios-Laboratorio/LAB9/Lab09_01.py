def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    try:
        temperatura_str = input("Ingrese la temperatura: ")
        temperatura = float(temperatura_str)
        unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()
        if unidad == 'C':
            fahrenheit = celsius_to_fahrenheit(temperatura)
            print(f"{temperatura}°C es igual a {fahrenheit:.2f}°F")
        elif unidad == 'F':
            celsius = fahrenheit_to_celsius(temperatura)
            print(f"{temperatura}°F es igual a {celsius:.2f}°C")
        else:
            print("Unidad de temperatura no válida. Por favor, ingrese 'C' o 'F'.")
    except ValueError:
        print("Entrada incorrecta. Asegúrate de ingresar un número válido para la temperatura.")
if __name__ == "__main__":main()
