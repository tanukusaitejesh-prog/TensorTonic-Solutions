import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    pass
    try:
        return np.linalg.eigvals(matrix)
    except:
        return None

    
