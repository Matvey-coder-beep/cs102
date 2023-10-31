def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    space_counter = 0
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            space_counter += 1
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
        if plaintext[i].isupper():
            shift = ord(keyword[(i - space_counter) % len(keyword)].upper()) - 65
            ciphertext += chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        else:
            shift = ord(keyword[(i - space_counter) % len(keyword)].lower()) - 97
            ciphertext += chr((ord(plaintext[i]) - 97 + shift) % 26 + 97)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    space_counter = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            space_counter += 1
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
        if ciphertext[i].isupper():
            shift = ord(keyword[(i - space_counter) % len(keyword)].upper()) - 65
            plaintext += chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65)
        else:
            shift = ord(keyword[(i - space_counter) % len(keyword)].lower()) - 97
            plaintext += chr((ord(ciphertext[i]) - 97 - shift) % 26 + 97)
    return plaintext