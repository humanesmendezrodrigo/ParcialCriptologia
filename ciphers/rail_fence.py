def cifrar(text: str, rails: int) -> str:
    if rails <= 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join("".join(row) for row in fence)


def descifrar(cipher_text: str, rails: int) -> str:
    if rails <= 1:
        return cipher_text

    pattern = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        pattern[rail].append(i)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    result = [''] * len(cipher_text)
    idx = 0
    for r in range(rails):
        for pos in pattern[r]:
            result[pos] = cipher_text[idx]
            idx += 1

    return "".join(result)
