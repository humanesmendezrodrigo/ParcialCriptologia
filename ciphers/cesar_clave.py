# ==========================================
# CIFRADO CESAR CON CLAVE
# ==========================================

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar(mensaje, clave):
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
    resultado = ""

    for letra in mensaje.upper():

        if letra in ALFABETO:
            posicion = ALFABETO.index(letra)

            nueva_posicion = (posicion - clave) % len(ALFABETO)

            resultado += ALFABETO[nueva_posicion]

        else:
            resultado += letra

    return resultado