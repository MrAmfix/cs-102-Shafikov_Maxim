from math import ceil
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
    keyword = keyword * ceil(len(plaintext) / len(keyword))
    bias = []
    bias_index = 0
    for i in keyword.lower():
        bias.append(ord(i) - ord('a'))
    for i in range(0, len(plaintext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            if (plaintext[i] <= 'Z' < chr(ord(plaintext[i]) + bias[bias_index])) or (chr(ord(plaintext[i]) + bias[bias_index]) > 'z'):
                ciphertext += chr(ord(plaintext[i]) - 26 + bias[bias_index])
            else:
                ciphertext += chr(ord(plaintext[i]) + bias[bias_index])
            bias_index += 1
        else:
            ciphertext += plaintext[i]
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
    keyword = keyword * ceil(len(ciphertext) / len(keyword))
    bias = []
    bias_index = 0
    for i in keyword.lower():
        bias.append(ord('a') - ord(i))
    for i in range(0, len(ciphertext)):
        if ('A' <= ciphertext[i] <= 'Z') or ('a' <= ciphertext[i] <= 'z'):
            if (ciphertext[i] <= 'Z' and chr(ord(ciphertext[i]) + bias[bias_index]) < 'A') or (ciphertext[i] >= 'a' > chr(ord(ciphertext[i]) + bias[bias_index])):
                plaintext += chr(ord(ciphertext[i]) + 26 + bias[bias_index])
            else:
                plaintext += chr(ord(ciphertext[i]) + bias[bias_index])
            bias_index += 1
        else:
            plaintext += ciphertext[i]
    return plaintext