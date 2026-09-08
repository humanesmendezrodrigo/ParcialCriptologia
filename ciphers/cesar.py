ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar(mensaje, clave):
    """Cifra un mensaje con un desplazamiento César."""
    resultado = ""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion = ALFABETO.index(letra)
            nueva_posicion = (posicion + clave) % len(ALFABETO)
            resultado += ALFABETO[nueva_posicion]
        else:
            resultado += letra

    return resultado


def descifrar(mensaje, clave):
    """Descifra un mensaje César con el mismo desplazamiento."""
    resultado = ""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion = ALFABETO.index(letra)
            nueva_posicion = (posicion - clave) % len(ALFABETO)
            resultado += ALFABETO[nueva_posicion]
        else:
            resultado += letra

    return resultado
