from cesar_clave import cifrar as cifrar_clave
from cesar_clave import descifrar as descifrar_clave

from cesar_posicion import cifrar as cifrar_posicion
from cesar_posicion import descifrar as descifrar_posicion


print("================================")
print("       CIFRADO CESAR")
print("================================")

mensaje = input("Ingrese el mensaje: ")

print("\nSeleccione el método:")
print("1. César con clave")
print("2. César con posición")

opcion = int(input("Ingrese una opción: "))

if opcion == 1:

    clave = int(input("Ingrese la clave: "))

    cifrado = cifrar_clave(mensaje, clave)
    descifrado = descifrar_clave(cifrado, clave)

    print("\n===== CÉSAR CON CLAVE =====")
    print("Mensaje original:", mensaje)
    print("Clave:", clave)
    print("Mensaje cifrado:", cifrado)
    print("Mensaje descifrado:", descifrado)


elif opcion == 2:

    posicion = int(input("Ingrese la posición: "))

    cifrado = cifrar_posicion(mensaje, posicion)
    descifrado = descifrar_posicion(cifrado, posicion)

    print("\n===== CÉSAR CON POSICIÓN =====")
    print("Mensaje original:", mensaje)
    print("Posición:", posicion)
    print("Mensaje cifrado:", cifrado)
    print("Mensaje descifrado:", descifrado)


else:
    print("Opción no válida")