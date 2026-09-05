def encrypt(text: str, key: str) -> list[int]:
    """
    Cifra un texto plano usando una clave mediante adición letra a letra (A=0, B=1, ...).
    Retorna una lista de enteros con el resultado de las sumas.
    """
    text = text.upper()
    key = key.upper()
    cipher_numbers = []

    for i in range(len(text)):
        char_text = text[i]
        # Repite la clave si el texto es más largo que la clave
        char_key = key[i % len(key)]

        # Convertir caracteres A-Z a valores 0-25
        val_text = ord(char_text) - ord('A') if 'A' <= char_text <= 'Z' else 0
        val_key = ord(char_key) - ord('A') if 'A' <= char_key <= 'Z' else 0

        # Suma aditiva exacta
        cipher_numbers.append(val_text + val_key)

    return cipher_numbers


def decrypt(cipher_numbers: list[int], key: str) -> str:
    """
    Descifra una lista de números restando los valores de la clave.
    Retorna el texto plano en mayúsculas.
    """
    key = key.upper()
    plain_chars = []

    for i in range(len(cipher_numbers)):
        char_key = key[i % len(key)]
        val_key = ord(char_key) - ord('A') if 'A' <= char_key <= 'Z' else 0

        # Resta aditiva para recuperar el valor original
        val_text = cipher_numbers[i] - val_key
        plain_chars.append(chr(val_text + ord('A')))

    return "".join(plain_chars)
