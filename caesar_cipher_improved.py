def caesar_cipher_encrypt(text, shift, case_sensitive=True, foreign_char=True):
    """
    Encryption technique that uses modular and a base to determine the shifted letters.
    """
    # If user doesnt want case sentitive we convert it to lower
    if not case_sensitive:
        text = text.lower()
    # string to concatonate all the character
    encrypt_text = ''
    # loop through every character in string 'text' and check if it's an alphabet
    for character in text:
        if character.isalpha():
            # check whether is it upper or lower case to determine the base
            base = ord('A') if character.isupper() else ord('a')
            encrypted_char = chr(((ord(character) - base) + shift) % 26 + base)
            encrypt_text = encrypt_text + encrypted_char
        else:
            if(foreign_char and (character != " ")):
                encrypted_char = chr((ord(character) + shift))
                encrypt_text = encrypt_text + encrypted_char
            else:
                
                encrypt_text = encrypt_text + character
                

    return encrypt_text

def caesar_cipher_decrypt(text, shift, case_sensitive=True, foreign_char=True):
    return caesar_cipher_encrypt(text, -shift, case_sensitive, foreign_char)


