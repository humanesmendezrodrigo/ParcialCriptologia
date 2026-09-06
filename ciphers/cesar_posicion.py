ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar(mensaje, posicion):
    resultado = ""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion_letra = ALFABETO.index(letra)
            nueva_posicion = (posicion_letra + posicion) % len(ALFABETO)
            resultado += ALFABETO[nueva_posicion]
        else:
            resultado += letra

    return resultado


def descifrar(mensaje, posicion):
    resultado = ""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion_letra = ALFABETO.index(letra)
            nueva_posicion = (posicion_letra - posicion) % len(ALFABETO)
            resultado += ALFABETO[nueva_posicion]
        else:
            resultado += letra

    return resultado