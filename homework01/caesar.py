import typing as tp


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
    # PUT YOUR CODE HERE
    for symbol in plaintext:
        if 64<ord(symbol)<91:
            new=ord(symbol)+shift
            if new>90:
                new=64+new-90
        elif 96<ord(symbol)<123:
            new=ord(symbol)+shift
            if new>122:
                new=96+new-122
        else:
            new=ord(symbol)

        ciphertext+=chr(new)

    return ciphertext

# print(encrypt_caesar("python PYTHON Python3.6"))

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
    # PUT YOUR CODE HERE

    for symbol in ciphertext:
        if 64<ord(symbol)<91:
            new=ord(symbol)-shift
            if new<65:
                new=90-new+62
        elif 96<ord(symbol)<123:
            new=ord(symbol)-shift
            if new<97:
                new=122-new+94
        else:
            new=ord(symbol)

        plaintext+=chr(new)

    return plaintext

# print(decrypt_caesar(encrypt_caesar("python PYTHON Python3.6 abcdefjhijklmnopqrstuwvxyz123 ABCDEFGHIJKLMNOPQRSTUWVXYZ123")))

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
