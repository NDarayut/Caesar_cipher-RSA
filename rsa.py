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
    e = 7 #random.randint(100, 1000000) # generate a random integer

    while(math.gcd(e, phi) != 1): # if e is divisible by phi, we generate it again
        e = random.randint(100, 10000)

    """Calculate private key n & d"""
    d= mod_inverse(e, phi)

    return ((e, n), (d, n))

def determine_step(n):
    if 0 < n < 25:
        raise ValueError("n should be greater than 25.")
    elif 25 < n < 2525:
        return 2
    elif 2525 < n < 252525:
        return 4
    elif 252525 < n < 25252525:
        return 6
    elif 25252525 < n < 2525252525:
        return 8
    else:
        raise ValueError("n is out of the supported range.")
    
def rsa_encryption(public_key, text):
    e, n = public_key
    steps = determine_step(n)
    cipher_string = []
    mapped_numbers = ""

    for character in text:
        
        if character.isalpha():
            character = character.lower()
            character_number = ord(character) - ord('a')
            mapped_numbers += str(character_number).zfill(2)

    for i in range(0, len(mapped_numbers), steps):
        segment = int(mapped_numbers[i:i + steps])
        cipher_text = pow(segment, e, n)
        cipher_string.append(cipher_text)

    return cipher_string

def rsa_decryption(private_key, cipher_text):
    """Decrypt the ciphertext using the RSA algorithm."""
    d, n = private_key
    steps = determine_step(n)
    mapped_numbers = ""

    for cipher_value in cipher_text:
        segment = pow(cipher_value, d, n)
        mapped_numbers += str(segment).zfill(steps)

    decrypt_text = []
    for i in range(0, len(mapped_numbers), 2):  # Each character is represented by 2 digits
        num = int(mapped_numbers[i:i + 2])
        if 0 <= num <= 25:
            decrypt_text.append(chr(num + ord('a')))

    return decrypt_text

public_key, private_key = key_generation(191, 23)
encrypted_text = rsa_encryption(public_key, "love")
print(f"Public key: {public_key}")
print(f"Encrypted message: {encrypted_text}")

decrypted_text = rsa_decryption(private_key, encrypted_text)
print(f"Private key: {private_key}")
print(f"Decrypted message: {decrypted_text}")




    
