def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    """Encrypt the text using the Affine cipher."""
    m = 26  # Size of the alphabet
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                x = ord(char) - ord('A')
                encrypted_char = (a * x + b) % m
                result += chr(encrypted_char + ord('A'))
            # Handle lowercase letters
            elif char.islower():
                x = ord(char) - ord('a')
                encrypted_char = (a * x + b) % m
                result += chr(encrypted_char + ord('a'))
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

def affine_decrypt(ciphertext, a, b):
    """Decrypt the text using the Affine cipher."""
    m = 26  # Size of the alphabet
    a_inv = mod_inverse(a, m)
    
    if a_inv is None:
        raise ValueError("Modular inverse does not exist for the given 'a'.")
    
    result = ""

    for char in ciphertext:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                y = ord(char) - ord('A')
                decrypted_char = (a_inv * (y - b)) % m
                result += chr(decrypted_char + ord('A'))
            # Handle lowercase letters
            elif char.islower():
                y = ord(char) - ord('a')
                decrypted_char = (a_inv * (y - b)) % m
                result += chr(decrypted_char + ord('a'))
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result