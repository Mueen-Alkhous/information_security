import numpy as np
from sympy import Matrix

def affine_hill_encrypt(text, A, B):
    pass

def affine_hill_decrypt(text, A, B):
    pass

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

