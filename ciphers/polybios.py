CUADRADO = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "K"],
    ["L", "M", "N", "O", "P"],
    ["Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z"]
]


def cifrar(texto):
    resultado = ""

    for caracter in texto.upper():

        if caracter == "J":
            caracter = "I"

        if caracter == " ":
            resultado += " "
            continue

        encontrado = False

        for fila in range(5):
            for columna in range(5):

                if CUADRADO[fila][columna] == caracter:
                    resultado += str(fila + 1)
                    resultado += str(columna + 1)

                    encontrado = True
                    break

            if encontrado:
                break

    return resultado


def descifrar(texto):
    resultado = ""

    numeros = ""

    for caracter in texto:

        if caracter.isdigit():

            numeros += caracter

            if len(numeros) == 2:

                fila = int(numeros[0]) - 1
                columna = int(numeros[1]) - 1

                if 0 <= fila < 5 and 0 <= columna < 5:
                    resultado += CUADRADO[fila][columna]

                numeros = ""

        elif caracter == " ":

            resultado += " "

    return resultado