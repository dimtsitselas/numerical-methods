from math  import sqrt
from sympy import Matrix
from sympy.matrices import eye

def givens(x, i, j):
    """Implements Givens tranformation.

    Args:
        *x* (list): a n-dimensional vector
        *i* (int): an integer in the range (0,.., n-1)
        *j* (int): an integer in the range (0,.., n-1)

    Returns:
        *Gij* (sympy.Matrix): a nxn matrix
    """
    # Check input format
    if not isinstance(x, list):
        raise TypeError("'x' must be a vector(list)")
    if not isinstance(i, int):
        raise TypeError("'i' must be integer")
    if not isinstance(j, int):
        raise TypeError("'j' must be integer")
    
    n = len(x)  # size of x    
    
    # Check input validity
    if i >= n or i < 0:
        raise ValueError("'i' out of bounds")
    if j >= n or j < 0:
        raise ValueError("'j' out of bounds")
    
    r = sqrt(x[i]*x[i] + x[j]*x[j])
    c = x[i] / r
    s = -x[j] / r

    G = eye(n)
    G[i, i] = c
    G[j, j] = c
    G[i, j] = -s
    G[j, i] = s

    return G

def qrGivens(A):
    """Implements QR factorization using Givens tranformation

    Given a mxn matrix A find an orthogonal matrix Q and an uppper tringular matrix R such that A = Q*R

    Args:
        A (sympy.Matrix): mxn matrix
    
    Returns:
        Q (sympy.Matrix): mxm orthogonal matrix
        R (sympy.Matrix): mxn upper triangular matrix
    """

    # Check input format
    if not isinstance(A, Matrix):
        raise TypeError("A must be a sympy matrix")

    m, n = A.shape  # Get A dimensions

    Q, R = eye(m), A

    for i in range(n):
        for j in range(i+1, m):
            Rcol = list(R.col(i)) # Get the i-th column

            Gij = givens(Rcol, i, j)
            R = Gij*R
            Q = Q*Gij.T
    
    return Q, R

if __name__ == "__main__":
    """
    A = Matrix([[10, 9, 18], [20, -15, -15], [20, -12, 51]])
    Q, R = qrGivens(A)
    print(Q)
    print(R)
    """

    array = input("Please enter vector x: ")
    x = [float(i) for i in array.split(" ")]
    j = int(input("Please enter j: "))

    G = givens(x, 0, j-1)
    print("Givens tranformation is: ")
    print(str(G))
