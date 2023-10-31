


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if not letter.isalpha():
            ciphertext += letter
            continue
        if letter.isupper():
            ciphertext += chr((ord(letter) - 65 + shift) % 26 + 65)
        else:
            ciphertext += chr((ord(letter) - 97 + shift) % 26 + 97)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if not letter.isalpha():
            plaintext += letter
            continue
        if letter.isupper():
            plaintext += chr((ord(letter) - 65 - shift) % 26 + 65)
        else:
            plaintext += chr((ord(letter) - 97 - shift) % 26 + 97)
    return plaintext