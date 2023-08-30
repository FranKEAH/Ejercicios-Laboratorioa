import random
import string

def generar_contraseña_segura(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    while not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial):
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        
        for char in contraseña:
            if char.isupper():
                tiene_mayuscula = True
            elif char.islower():
                tiene_minuscula = True
            elif char.isdigit():
                tiene_numero = True
            elif char in string.punctuation:
                tiene_caracter_especial = True

    return contraseña

longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))

contraseña_segura = generar_contraseña_segura(longitud_deseada)
print("Contraseña segura generada:", contraseña_segura)
