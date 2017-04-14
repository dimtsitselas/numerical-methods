"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ polynomials.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module has classes for some elementary polynomial representations such as 
exponential form, center form, newton form, and lagrange form.
"""

class ExponetialPolynomial():
    """Polynomial of exponential form

    The form of these polynomials is: ** a0 + a1 \* x + ... + an \* x^n **
    """

    def __init__(self, coeffs):
        """Initialization of the polynomial.

        args:
            coeffs (list): list of coefficients

        e.g. p = ExponetialPolynomial([1, 2, 1]) # p = 1 + 2*x + x^2
        """

        self.degree = len(coeffs)-1
        self.coeffs = coeffs

    def __call__(self, point):
        """Returns the value at the given point
        
        e.g. p(5) # returns 1 + 2*5 + 5^2
        """

        value, pow = 0, 1

        for i in range(self.degree+1):
            value += self.coeffs[i]*pow
            pow *= point # point^i

        return value


class CenterPolynomial():
    """Polynomial of centers form.

    The form of the polynomials is:
           ** a0 + a1 \* (x-c) + a2 \* (x-c)^2 + ... + an \* (x-c)^n **
    """

    def __init__(self, coeffs, center):
        """Initialization of the polynomial.

        args:
            coeffs (list): list of coefficients
            center (int): center of the polynomial

        e.g. p = CenterPolynomial([1, 2, 1], 3) # p = 1 + 2*(x-3) + (x-3)^2
        """

        self.degree = len(coeffs)-1
        self.coeffs = coeffs
        self.center = center

    def __call__(self, point):
        """Returns the value at the given point
        
        e.g. p(5) # returns 1 + 2*(5-3) + (5-3)^2
        """

        value, pow = 0, 1

        for i in range(self.degree+1):
            value += self.coeffs[i]*pow
            pow *= point-self.center # (point-self.center)^i

        return value


class NewtonPolynomial():
    """Polynomial of newton form.

    The form of the polynomials is:
    ** a0 + a1\*(x-c1) + a2\*(x-c1)\*(x-c2) + ... + an\*(x-c1)\*...*(x-cn) **
    """

    def __init__(self, coeffs, centers):
        """Initialization of the polynomial.

        args:
            coeffs (list): list of coefficients
            centers (list): centers of the polynomial

        e.g. p = NewtonPolynomial([1, 2, 1], [3, -7])
        # p = 1 + 2*(x-3) + (x-3)(x+7)
        """

        self.degree = len(coeffs)-1
        self.coeffs = coeffs
        self.center = centers

    def __call__(self, point):
        """Returns the value at the given point
        
        e.g. p(5) # returns 1 + (5-3)*(2 + 1*(5+7))
        """

        value = self.coeffs[self.degree] # value = an

        for i in range(self.degree-1, -1, -1):  
            value = value*(point-self.center[i]) + self.coeffs[i]

        return value


class _LagrangePolynomials():
    """Lagrange Polynomials.

    Given n+1 points the j-th Lagrange polynomial is:
            (x-x0)/(xj-x0) *...* (x-x(j-1))/(xj-x(j-1)) *
            (x-x(j+1))/(xj-x(j+1)) *...* (x-xn)/(xj-xn)
    """

    def __init__(self, points):
        """Initialization of the lagrange polynomial.

        args:
            points (list): list of points (reals)

        e.g. p = _LagrangePolynomials([1, 2, 5])
        # L1 = (x-1)/(2-1) * (x-5)/(2-5)
        """
        self.degree = len(points)-1
        self.point = points

        # precomputing the denomerators of the polynomials
        self.denominator = [1]*(self.degree+1)
        
        for i in range(self.degree+1):
            for j in range(self.degree+1):
                if i != j:
                    self.denominator[i] *= points[i]-points[j]

    def __call__(self, j, point):
        """Returns the value of the j-th Langrage polynomial at the given point
        
        e.g. p(1, 5) # returns (5-1)/(2-1) * (5-5)/(2-5)
        """

        numerator = 1
        for i in range(self.degree+1):
            if i != j:
                numerator *= point-self.point[i]
        
        return numerator/self.denominator[j]


class LagrangePolynomial():
    """Lagrange Polynomial form.

    Given n+1 coefficients and n+1 points, the polynomial is:
            a0*l0(x) + a1*l1(x) + ... + an*ln(x)
    """

    def __init__(self, coeffs, points):
        """Initialization of the lagrange polynomial.

        args:
            coeffs (list): list of coefficients (reals)
            points (list): list of points (reals)

        e.g. p = LagrangePolynomial([3, 2, 7], [1, 2, 5])
        # p = 3*l0(x) + 2*l1(x) + 7*l2(x)
        """
        self.degree = len(points)-1
        self.coeffs = coeffs
        self.l = _LagrangePolynomials(points)        

    def __call__(self, point):
        """Returns the value of the polynomial at the given point"""
        value = 0

        for i in range(self.degree+1):
            value += self.coeffs[i]*self.l(i, point)

        return value
