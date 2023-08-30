def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("No es posible dividir por cero.")
    return x / y
def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        operacion = input("Seleccione el número de operación: ")
        
        if operacion in ('1', '2', '3', '4'):
            if operacion == '1':
                result = add(num1, num2)
                operator = "+"
            elif operacion == '2':
                result = subtract(num1, num2)
                operator = "-"
            elif operacion == '3':
                result = multiply(num1, num2)
                operator = "*"
            else:
                result = divide(num1, num2)
                operator = "/"
            print(f"{num1} {operator} {num2} = {result}")
        else:
            print("Operación no válida. Por favor, seleccione una operación del 1 al 4.")
    except ValueError:
        print("Entrada incorrecta. Asegúrate de ingresar números válidos.")
if __name__ == "__main__":
    main()