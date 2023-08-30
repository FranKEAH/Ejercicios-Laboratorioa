def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            base = ord('a') if caracter.islower() else ord('A')
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter
    
    return mensaje_cifrado
mensaje_original = input("Ingrese el mensaje a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)