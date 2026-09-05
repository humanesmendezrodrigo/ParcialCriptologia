# transposicion_columnas.py

def cifrar(texto, clave):
    """Acomoda el texto en una matriz de n columnas (n = longitud de
    la clave) y lee las columnas en el orden alfabético de la clave."""
    texto = texto.upper().replace(" ", "")
    clave = clave.upper()
    n = len(clave)
    filas = -(-len(texto) // n)
    texto = texto.ljust(filas * n, "X")
    orden = sorted(range(n), key=lambda i: clave[i])
    resultado = ""
    for col in orden:
        for fila in range(filas):
            resultado += texto[fila * n + col]
    return resultado


def descifrar(texto, clave):
    """Revierte el cifrado por columnas: reconstruye la matriz
    original columna por columna y la lee por filas."""
    clave = clave.upper()
    n = len(clave)
    filas = len(texto) // n
    orden = sorted(range(n), key=lambda i: clave[i])
    matriz = [["" for _ in range(n)] for _ in range(filas)]
    idx = 0
    for col in orden:
        for fila in range(filas):
            matriz[fila][col] = texto[idx]
            idx += 1
    return "".join("".join(fila) for fila in matriz)


if __name__ == "__main__":
    texto = input("Ingresa el mensaje: ")
    clave = input("Ingresa la clave (ej. TRES): ")
    cifrado = cifrar(texto, clave)
    print("Mensaje cifrado:", cifrado)
    print("Mensaje descifrado:", descifrar(cifrado, clave))