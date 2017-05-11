from math  import sqrt
from sympy import Matrix
from sympy.matrices import eye, zeros

def householder(x, k):
    """Implements Householder transformation.

    Args:
        *x* (list): n-dimensional vector
        *k* (int): integer in the range 1..n
    
    Returns:
        *H* (sympy.Matrix): nxn matrix such that the n-k last elements of Hx are zeroes
    """
    # Check input format
    if not isinstance(x, list):
        raise TypeError("x must be a vector(list)")
    if not isinstance(k, int):
        raise TypeError("k must be integer")

    n = len(x)  # size of x

    # Check input validity
    if n < k:
        raise ValueError("k larger than x dimensions")
    if x[k:] == [0] * (n-k):
        raise Exception("vector x has already the desired property")
    
    sgn = x[k-1]/abs(x[k-1])
    s = sqrt(sum([i*i for i in x[k-1:]]))
    t = sqrt(2*s*(s+abs(x[k-1])))

    u = zeros(n, 1)
    u[k-1] = (x[k-1] + sgn*s)/t
    for i in range(k, n):
        u[i] = 1/t*x[i]

    # Householdler tranformation matrix
    H = eye(n) - 2*u*u.T

    return H

def qrHouseholder(A):
    """Implements QR factorization using householder tranformation

    Given a mxn matrix A find an orthogonal matrix Q and an uppper tringular matrix R such that A = Q*R

    Args:
        A (sympy.Matrix): mxn matrix
    
    Returns:
        Q (sympy.Matrix): mxm orthogonal matrix
        R (sympy.Matrix): mxn upper triangular matrix
    """

    # Check input format
    if not isinstance(A, Matrix):
        raise AttributeError("A must be a sympy matrix")

    m, n = A.shape  # Get A dimensions

    Q, R = eye(m), A
    for k in range(n):
        Rcol = list(R.col(k))    # Get the k-th column

        # if k-th column of R has already the desired property do nothing
        if Rcol[k+1:] != [0] * (n-k-1):
            Hk = householder(Rcol, k+1)
            R = Hk*R
            Q = Q*Hk
    
    return Q, R

if __name__ == "__main__":
    """
    A = Matrix([[3, 0], [4, 5], [0, 4]])
    Q, R = qrHouseholder(A)
    print(Q)
    print(R)
    """

    array = input("Please enter vector x: ")
    x = [float(i) for i in array.split(" ")]
    k = int(input("Please enter k: "))

    H = householder(x, k)
    print("Householder tranformation is: ")
    print(str(H))
