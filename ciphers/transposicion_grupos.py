# transposicion_grupos.py

def cifrar(texto, clave):
    """Divide el texto en bloques del tamaño de la clave y reordena
    cada bloque según el orden numérico de la clave."""
    texto = texto.upper().replace(" ", "")
    n = len(clave)
    resultado = ""
    for i in range(0, len(texto), n):
        bloque = texto[i:i + n].ljust(n, "X")
        for digito in clave:
            resultado += bloque[int(digito) - 1]
    return resultado


def descifrar(texto, clave):
    """Revierte el cifrado por grupos: reconstruye cada bloque
    original a partir del orden indicado por la clave."""
    n = len(clave)
    resultado = ""
    for i in range(0, len(texto), n):
        bloque_cifrado = texto[i:i + n]
        bloque_original = [""] * n
        for k, digito in enumerate(clave):
            bloque_original[int(digito) - 1] = bloque_cifrado[k]
        resultado += "".join(bloque_original)
    return resultado


if __name__ == "__main__":
    texto = input("Ingresa el mensaje: ")
    clave = input("Ingresa la clave (ej. 43521): ")
    cifrado = cifrar(texto, clave)
    print("Mensaje cifrado:", cifrado)
    print("Mensaje descifrado:", descifrar(cifrado, clave))