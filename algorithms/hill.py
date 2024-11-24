from sympy import Matrix
import numpy as np

def hill_encrypt(text, key):
    encrypted_text = ""
    prepared_text = ""
    for char in text:
        if char.isalpha():
            prepared_text += char

    prepared_text += 'Z' * (len(prepared_text) % key.shape[1])
    
    text_array_as_nums = []

    for char in prepared_text:
        if char.isupper():
            x = ord(char) - ord('A')
            text_array_as_nums.append(x)
        else:
            x = ord(char) - ord('a')
            text_array_as_nums.append(x)
    text_array_as_nums = np.array(text_array_as_nums).reshape(key.shape[1], len(text_array_as_nums) // key.shape[1])
    result = key @ text_array_as_nums % 26
    for i in range(len(prepared_text)):
        if prepared_text[i].isalpha():
            if prepared_text[i].isupper():
                encrypted_text += chr(result[i // result.shape[1]][i % result.shape[1]] + ord('A'))
            else:
                encrypted_text += chr(result[i // result.shape[1]][i % result.shape[1]] + ord('a'))
    for i in range(len(text)):
        if not text[i].isalpha():
            encrypted_text = encrypted_text[:i] + text[i] + encrypted_text[i:]
    return encrypted_text


    
    

def hill_decrypt(text : str, key):
    decrypted_text = ""
    prepared_text = ""
    for char in text:
        if char.isalpha():
            prepared_text += char

    prepared_text += 'Z' * (len(prepared_text) % key.shape[1])
    
    text_array_as_nums = []

    for char in prepared_text:
        if char.isupper():
            x = ord(char) - ord('A')
            text_array_as_nums.append(x)
        else:
            x = ord(char) - ord('a')
            text_array_as_nums.append(x)
    text_array_as_nums = np.array(text_array_as_nums).reshape(key.shape[1], len(text_array_as_nums) // key.shape[1])

    inverse_key = mod_inverse_matrix(key, 26)

    result = inverse_key @ text_array_as_nums % 26
    for i in range(len(prepared_text)):
        if prepared_text[i].isalpha():
            if prepared_text[i].isupper():
                decrypted_text += chr(result[i // result.shape[1]][i % result.shape[1]] + ord('A'))
            else:
                decrypted_text += chr(result[i // result.shape[1]][i % result.shape[1]] + ord('a'))
    for i in range(len(text)):
        if not text[i].isalpha():
            decrypted_text = decrypted_text[:i] + text[i] + decrypted_text[i:]
    return decrypted_text




def mod_inverse_matrix(matrix, mod):

    sympy_matrix = Matrix(matrix)  
    det = int(sympy_matrix.det())
    det_mod_inv = pow(det, -1, mod) 
    
    if det_mod_inv is None:
        print(f"Matrix determinant ({det}) is not invertible modulo {mod}.")
        return None
    
    inverse_matrix = det_mod_inv * sympy_matrix.adjugate()
    
    inverse_matrix_mod = np.array(inverse_matrix % mod)
    
    return inverse_matrix_mod