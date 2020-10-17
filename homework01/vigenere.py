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
    # PUT YOUR CODE HERE
    shift=[]
    for kw in keyword:
        if 64<ord(kw)<91:
            new_kw=ord(kw)-65
        elif 96<ord(kw)<123:
            new_kw=ord(kw)-97
        shift.append(new_kw)

    for word in plaintext:
        if 64<ord(word)<91:
            new=ord(word)+shift[0]
            if new>90:
                new=64+new-90
        elif 96<ord(word)<123:
            new=ord(word)+shift[0]
            if new>122:
                new=96+new-122
        else:
            new=ord(word)

        shift.append(shift[0])
        shift.pop(0)

        ciphertext+=chr(new)

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
    # PUT YOUR CODE HERE
    shift=[]
    for kw in keyword:
        if 64<ord(kw)<91:
            new_kw=ord(kw)-65
        elif 96<ord(kw)<123:
            new_kw=ord(kw)-97
        shift.append(new_kw)

    for word in ciphertext:
        if 64<ord(word)<91:
            new=ord(word)-shift[0]
            if new<65:
                new=90-(64-new)
        elif 96<ord(word)<123:
            new=ord(word)-shift[0]
            if new<97:
                new=122-(96-new)
        else:
            new=ord(word)

        shift.append(shift[0])
        shift.pop(0)

        plaintext+=chr(new)

    return plaintext