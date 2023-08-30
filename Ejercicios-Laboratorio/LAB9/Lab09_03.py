import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales):
    opciones = []

    if not any([incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales]):
        raise ValueError("Debes seleccionar al menos un conjunto de caracteres.")

    if incluir_mayusculas:
        opciones.extend(string.ascii_uppercase)
    if incluir_minusculas:
        opciones.extend(string.ascii_lowercase)
    if incluir_numeros:
        opciones.extend(string.digits)
    if incluir_especiales:
        opciones.extend(string.punctuation)

    if not opciones:
        raise ValueError("No hay opciones válidas para generar caracteres.")

    try:
        generador = lambda: random.choice(opciones)
        contraseña = ''.join(generador() for _ in range(longitud))
        return contraseña
    except ValueError:
        raise ValueError("La longitud debe ser un número entero positivo.")

def main():
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        incluir_mayusculas = input("Incluir letras mayúsculas (S/N): ").upper() == 'S'
        incluir_minusculas = input("Incluir letras minúsculas (S/N): ").upper() == 'S'
        incluir_numeros = input("Incluir números (S/N): ").upper() == 'S'
        incluir_especiales = input("Incluir caracteres especiales (S/N): ").upper() == 'S'

        contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales)
        print("Contraseña generada:", contraseña)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()