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
     
    for char in plaintext:
        if ord('A') <= ord(char) <= ord('Z'):
            offset_first_letter = ord('A')
            length_of_alphabet  = ord('Z') - ord('A') + 1
        elif ord('a') <= ord(char) <= ord('z'):
            offset_first_letter = ord('a')
            length_of_alphabet  = ord('z') - ord('a') + 1
        elif ord('А') <= ord(char) <= ord('Я'):
            offset_first_letter = ord('А')
            length_of_alphabet  = ord('Я') - ord('А') + 1
        elif ord('а') <= ord(char) <= ord('я'):
            offset_first_letter = ord('а')
            length_of_alphabet  = ord('я') - ord('а') + 1
        else:
            offset_first_letter = None
        if offset_first_letter is not None:
            new_ord = (ord(char) - offset_first_letter + shift) % length_of_alphabet + offset_first_letter
            new_char = chr(new_ord)
        else:
            new_char = char
        ciphertext += new_char

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
    # PUT YOUR CODE HERE
    
    for char in ciphertext:
        if ord('A') <= ord(char) <= ord('Z'):
            offset_first_letter = ord('A')
            length_of_alphabet  = ord('Z') - ord('A') + 1
        elif ord('a') <= ord(char) <= ord('z'):
            offset_first_letter = ord('a')
            length_of_alphabet  = ord('z') - ord('a') + 1
        elif ord('А') <= ord(char) <= ord('Я'):
            offset_first_letter = ord('А')
            length_of_alphabet  = ord('Я') - ord('А') + 1
        elif ord('а') <= ord(char) <= ord('я'):
            offset_first_letter = ord('а')
            length_of_alphabet  = ord('я') - ord('а') + 1
        else:
            offset_first_letter = None
        if offset_first_letter is not None:
            new_ord = (ord(char) - offset_first_letter - shift) % length_of_alphabet + offset_first_letter
            new_char = chr(new_ord)
        else:
            new_char = char
        plaintext += new_char

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE

    dictLower = ([])
    for m in dictionary:
        dictLower.append(m.lower())

    isBreak = False
    length_of_alphabet  = ord('Z') - ord('A')
    while best_shift <= length_of_alphabet:
        plaintext = decrypt_caesar(ciphertext, best_shift)
        if plaintext.lower() in dictLower:
            isBreak = True
            break
        best_shift += 1
    if isBreak == False:
        best_shift = -1

    return best_shift


def main() -> None:
    print("Hello, World!")
    print(caesar_breaker_brute_force('Sbwkrq', {"c","Pascal","Delphi","Python","basic","1c","sql","fortran","pl","bash"}))


if __name__ == "__main__":
    main()
