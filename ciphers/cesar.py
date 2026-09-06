ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar(texto: str, desplazamiento: int) -> str:
    if not isinstance(desplazamiento, int):
        raise TypeError("El desplazamiento debe ser un número entero.")

    resultado = []
    for caracter in texto:
        mayuscula = caracter.upper()
        if mayuscula in ALFABETO:
            posicion = ALFABETO.index(mayuscula)
            nueva_letra = ALFABETO[(posicion + desplazamiento) % len(ALFABETO)]
            resultado.append(nueva_letra if caracter.isupper() else nueva_letra.lower())
        else:
            resultado.append(caracter)
    return "".join(resultado)


def descifrar(texto: str, desplazamiento: int) -> str:
    """Devuelve un texto César a su forma original."""
    return cifrar(texto, -desplazamiento)


def _leer_desplazamiento() -> int:
    """Solicita un desplazamiento entero hasta que sea válido."""
    while True:
        try:
            return int(input("Desplazamiento (por ejemplo, 3): "))
        except ValueError:
            print("Ingresa un número entero.")


def main() -> None:
    """Interfaz de consola del cifrado César."""
    print("=== CIFRADO CÉSAR ===")
    while True:
        opcion = input("\n1. Cifrar\n2. Descifrar\n3. Salir\nOpción: ").strip()
        if opcion == "3":
            print("Hasta luego.")
            break
        if opcion not in {"1", "2"}:
            print("Opción no válida.")
            continue

        texto = input("Texto: ")
        desplazamiento = _leer_desplazamiento()
        resultado = cifrar(texto, desplazamiento) if opcion == "1" else descifrar(texto, desplazamiento)
        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
