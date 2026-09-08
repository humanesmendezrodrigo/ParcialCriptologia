
# ==========================================
# CIFRADO PIGPEN
# ==========================================

import re

SIMBOLOS_PIGPEN = {
    "A": "\u2518", "B": "\u2294", "C": "\u2514",
    "D": "\u2290", "E": "\u25a1", "F": "\u228f",
    "G": "\u2510", "H": "\u2293", "I": "\u250c",
    "J": "\u2518*", "K": "\u2294*", "L": "\u2514*",
    "M": "\u2290*", "N": "\u25a1*", "O": "\u228f*",
    "P": "\u2510*", "Q": "\u2293*", "R": "\u250c*",
    "S": "\u25bc", "T": "\u25b6", "U": "\u25c0", "V": "\u25b2",
    "W": "\u25bc*", "X": "\u25b6*", "Y": "\u25c0*", "Z": "\u25b2*",
}

SIMBOLOS_A_LETRAS = {simbolo: letra for letra, simbolo in SIMBOLOS_PIGPEN.items()}


def cifrar(texto):
    """Cifra las letras A-Z de *texto*, con simbolos separados por un espacio."""
    tokens = []
    for caracter in texto:
        if caracter == " ":
            tokens.append(" ")
        else:
            simbolo = SIMBOLOS_PIGPEN.get(caracter.upper())
            tokens.append(simbolo if simbolo is not None else caracter)
    return " ".join(tokens)


def descifrar(texto):
    """Descifra un texto Pigpen (un espacio separa cada simbolo)."""
    letras = []
    for parte in re.findall(r"\S+|\s+", texto):
        if parte.isspace():
            espacios_reales = (len(parte) - 1) // 2
            letras.append(" " * espacios_reales)
        else:
            letras.append(SIMBOLOS_A_LETRAS.get(parte, parte))
    return "".join(letras)

