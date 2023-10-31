shift = 3
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
        if 65 <= ord(letter) < 88 or 97 <= ord(letter) <= 119:
            ciphertext += chr(ord(letter) + shift)
        elif 91 > ord(letter) > 87 or 123 > ord(letter) > 119:
            ciphertext += chr(ord(letter) - (26 - shift))
        else:
            ciphertext += letter
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
        if 68 <= ord(letter) < 91 or 100 <= ord(letter) <= 122:
            plaintext += chr(ord(letter) - shift)
        elif 68 > ord(letter) > 64 or 100 > ord(letter) > 96:
            plaintext += chr(ord(letter) + (26 - shift))
        else:
            plaintext += letter
    return plaintext

if __name__ == "__main__":
    while True:
        choice = input('Введите операцию (Шифровать или дешифровать): ')
        if choice.lower() == 'шифровать':
            plaintext = input('Введите слово которые вы хотите зашифровать: ')
            print(encrypt_caesar(plaintext, shift))
        elif choice.lower() == 'дешифровать':
            ciphertext = input('Write word you want to decode: ')
            print(decrypt_caesar(ciphertext, shift))
        else:
            print('Error')