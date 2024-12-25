import numpy as np




def exist_inlist(elem,l):
    """This function checks if an element exists in a list."""
    for i in range(len(l)):
        if (elem==l[i]):
            return True
    return False
def pca_svd(matrix, n_components):
    """
    Using SVD to perform PCA on the input matrix making it into a n_components-dimensional matrix.
    """
    # make sure it's a numpy array
    matrix = np.array(matrix)
    
    # center the matrix
    matrix_mean = np.mean(matrix, axis=0)
    centered_matrix = matrix - matrix_mean
    
    # SVD
    U, S, Vt = np.linalg.svd(centered_matrix, full_matrices=False)
    
    # Choose the first n_components columns of U and the first n_components rows of Vt
    U_reduced = U[:, :n_components]
    S_reduced = S[:n_components]
    Vt_reduced = Vt[:n_components, :]
    reduced_matrix = np.dot(U_reduced, np.diag(S_reduced))
    
    return reduced_matrix