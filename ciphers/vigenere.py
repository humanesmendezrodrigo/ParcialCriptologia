ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validar_clave(clave):
    clave = clave.upper().replace(" ", "")

    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    if not clave.isalpha():
        raise ValueError("La clave debe contener solamente letras.")

    return clave


def cifrar(texto, clave):
    clave = validar_clave(clave)

    resultado = ""
    indice_clave = 0

    for caracter in texto.upper():

        if caracter in ALFABETO:
            posicion_texto = ALFABETO.index(caracter)
            posicion_clave = ALFABETO.index(
                clave[indice_clave % len(clave)]
            )

            nueva_posicion = (
                posicion_texto + posicion_clave
            ) % len(ALFABETO)

            resultado += ALFABETO[nueva_posicion]

            indice_clave += 1

        else:
            resultado += caracter

    return resultado


def descifrar(texto, clave):
    clave = validar_clave(clave)

    resultado = ""
    indice_clave = 0

    for caracter in texto.upper():

        if caracter in ALFABETO:
            posicion_texto = ALFABETO.index(caracter)
            posicion_clave = ALFABETO.index(
                clave[indice_clave % len(clave)]
            )

            nueva_posicion = (
                posicion_texto - posicion_clave
            ) % len(ALFABETO)

            resultado += ALFABETO[nueva_posicion]

            indice_clave += 1

        else:
            resultado += caracter

    return resultado