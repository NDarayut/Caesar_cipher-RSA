import random
import math
from sympy import mod_inverse

def is_prime(n):
    """Check if a number is prime."""
    # Edge cases for numbers less than or equal to 1
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Eliminate even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility from 5 to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def key_generation(p, q):
    """
    Public key pair: n & e
    Private key pair: n & d
    """

    if(not is_prime(p)):
        return "Not a prime number!"
    if(not is_prime(q)):
        return "Not a prime number!"
    
    """Calculate public key n & e"""
    n = p * q # Calculate n public key
    phi = (p-1)*(q-1) # phi is used to calculate d and find suitable e
    e = random.randint(100, 1000000) # generate a random integer

    while(math.gcd(e, phi) != 1): # if e is divisible by phi, we generate it again
        e = random.randint(100, 1000000)

    """Calculate private key n & d"""
    d= mod_inverse(e, phi)

    return ((e, n), (d, n))

def rsa_encryption(public_key, text):
    e, n = public_key
    cipher_string = []
    for character in text:
        
        if character.isalpha():
            character = character.lower()
            character_number = ord(character) - ord('a')
            cipher_text = pow(character_number, e) % n
            
            cipher_string.append(cipher_text)
    return cipher_string

def rsa_decryption(private_key, cipher_text):
    d, n = private_key
    decrypt_text = []
    for character in cipher_text:
        character_number = (pow(character, d) % n) + ord('a')
        plain_text = chr(character_number)
        decrypt_text.append(plain_text)
    return decrypt_text


            





    
