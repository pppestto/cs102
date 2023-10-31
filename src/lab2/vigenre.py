import string

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
    alphabet = string.ascii_lowercase
    space_count = 0
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            space_count += 1
        if plaintext[i].lower() not in alphabet:
            ciphertext += plaintext[i]
            continue
        if plaintext[i].islower():
            shift = (ord(keyword[(i - space_count) % len(keyword)].lower()) - 97)
            ciphertext += chr(((ord(plaintext[i]) + shift - 97) % 26) + 97)
        else:
            shift = (ord(keyword[(i - space_count) % len(keyword)].upper()) - 65)
            ciphertext += chr(((ord(plaintext[i]) + shift - 65) % 26) + 65)
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
    alphabet = string.ascii_lowercase
    space_count = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            space_count += 1
        if ciphertext[i].lower() not in alphabet:
            plaintext += ciphertext[i]
            continue
        if ciphertext[i].islower():
            shift = (ord(keyword[(i - space_count) % len(keyword)].lower()) - 97)
            plaintext += chr(((ord(ciphertext[i]) - shift - 97) % 26) + 97)
        else:
            shift = (ord(keyword[(i - space_count) % len(keyword)].upper()) - 65)
            plaintext += chr(((ord(ciphertext[i]) - shift - 65) % 26) + 65)
    return plaintext