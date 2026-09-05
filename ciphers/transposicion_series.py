# transposicion_series.py

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def _orden_series(n):
    primos = [i for i in range(1, n + 1) if es_primo(i)]
    pares = [i for i in range(1, n + 1) if i % 2 == 0 and i not in primos]
    impares = [i for i in range(1, n + 1) if i % 2 != 0 and i not in primos]
    return primos + pares + impares


def cifrar(texto):
    """Reordena el texto agrupando primero las posiciones primas,
    luego las pares restantes y por último las impares restantes."""
    texto = texto.upper().replace(" ", "")
    orden = _orden_series(len(texto))
    return "".join(texto[i - 1] for i in orden)


def descifrar(texto):
    """Revierte el cifrado por series: coloca cada carácter de
    vuelta en su posición original según el mismo criterio."""
    n = len(texto)
    orden = _orden_series(n)
    original = [""] * n
    for j, pos in enumerate(orden):
        original[pos - 1] = texto[j]
    return "".join(original)


if __name__ == "__main__":
    texto = input("Ingresa el mensaje: ")
    cifrado = cifrar(texto)
    print("Mensaje cifrado:", cifrado)
    print("Mensaje descifrado:", descifrar(cifrado))