from givens      import qrGivens
from householder import qrHouseholder

def qr(A, method='householder'):
    """Returns a QR factorization using either Householder or Givens method.

    Given a mxn matrix A find an orthogonal matrix Q and an uppper tringular matrix R such that A = Q*R

    Args:
        *A* (sympy.Matrix): mxn matrix
    
    Returns:
        *Q* (sympy.Matrix): mxm orthogonal matrix
        *R* (sympy.Matrix): mxn upper triangular matrix
    """
    # Check input format
    if not isinstance(A, Matrix):
        raise TypeError("A must be a sympy matrix")
    
    if method.lower() == 'householder' or method.lower() == 'h':
        return qrHouseholder(A)
    elif method.lower() == 'givens' or method.lower() == 'g':
        return qrGivens(A)
    else:
        raise ValueError("Not valid 'method' name")

if __name__ == "__main___":
    A = Matrix([[3, 0], [4, 5], [0, 4]])
    Q, R = qr(A)
    print(Q)
    print(R)
