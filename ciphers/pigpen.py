SIMBOLOS_PIGPEN = {
    # Rejilla 1 (A-I): esquinas, bordes en U y el centro (cuadro completo)
    "A": "\u2518", "B": "\u2294", "C": "\u2514",
    "D": "\u2290", "E": "\u25a1", "F": "\u228f",
    "G": "\u2510", "H": "\u2293", "I": "\u250c",
    # Rejilla 2 (J-R): mismas formas + punto
    "J": "\u2518*", "K": "\u2294*", "L": "\u2514*",
    "M": "\u2290*", "N": "\u25a1*", "O": "\u228f*",
    "P": "\u2510*", "Q": "\u2293*", "R": "\u250c*",
    # X 1 (S-V): triangulos solidos
    "S": "\u25bc", "T": "\u25b6", "U": "\u25c0", "V": "\u25b2",
    # X 2 (W-Z): mismos triangulos + punto
    "W": "\u25bc*", "X": "\u25b6*", "Y": "\u25c0*", "Z": "\u25b2*",
}

SIMBOLOS_A_LETRAS = {simbolo: letra for letra, simbolo in SIMBOLOS_PIGPEN.items()}

SEPARADOR_PALABRA = "/"  # marca el espacio entre palabras en el texto cifrado


def cifrar(texto: str) -> str:
    """Cifra las letras A-Z de *texto*, con simbolos separados por espacios."""
    tokens = []
    for caracter in texto:
        if caracter == " ":
            tokens.append(SEPARADOR_PALABRA)
        else:
            simbolo = SIMBOLOS_PIGPEN.get(caracter.upper())
            tokens.append(simbolo if simbolo is not None else caracter)
    return " ".join(tokens)


def descifrar(texto: str) -> str:
    """Descifra un texto Pigpen con simbolos separados por espacios."""
    letras = []
    for token in texto.split():
        if token == SEPARADOR_PALABRA:
            letras.append(" ")
        else:
            letras.append(SIMBOLOS_A_LETRAS.get(token, token))
    return "".join(letras)


def main() -> None:
    """Interfaz de consola del cifrado Pigpen."""
    print("=== CIFRADO PIGPEN ===")
    print("Nota: solo se cifran las letras A-Z; la N y las tildes se conservan.")
    while True:
        opcion = input("\n1. Cifrar\n2. Descifrar\n3. Salir\nOpcion: ").strip()
        if opcion == "3":
            print("Hasta luego.")
            break
        if opcion not in {"1", "2"}:
            print("Opcion no valida.")
            continue

        texto = input("Texto: ")
        resultado = cifrar(texto) if opcion == "1" else descifrar(texto)
        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()

