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
    for i in plaintext:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if i == 'x' or i == 'X' or i == 'y' or i == 'Y' or i == 'z' or i == 'Z':
                ciphertext += chr(ord(i) - 23)
            else:
                ciphertext += chr(ord(i) + 3)
        else:
            ciphertext += i
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
    for i in ciphertext:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if i == 'a' or i == 'A' or i == 'b' or i == 'B' or i == 'c' or i == 'C':
                plaintext += chr(ord(i) + 23)
            else:
                plaintext += chr(ord(i) - 3)
        else:
            plaintext += i

    return plaintext