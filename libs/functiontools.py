"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ functiontools.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is based on sympy module and is used to represent and handle one
variable mathematical functions.
"""

from sympy                      import *
from sympy.parsing.sympy_parser import parse_expr

class function():
    """One variable mathematical function.

    For example:
    f = function("x**2 + exp(x)")
    str(f) # Returns "x**2 + exp(x)"
    f(5) # Returns 5**2 + exp(5)
    """

    def __init__(self, str):
        """
        params:
            str (string): Contains the expression in string form
        """
        
        self.expr = parse_expr(str)         # sympy expression
        vars = list(self.expr.free_symbols) # symbols in epxr

        if len(vars) == 0:
            self.var = None
        elif len(vars) == 1:
            self.var = vars[0]
        else:
            raise AttributeError("Expression has more than one variables")

    def __str__(self):
        """Returns function as string"""

        return str(self.expr)

    def __call__(self, value):
        """Evaluates the function at a given point.
        
        params:
            value: the value in which function is evaluated

        e.g. f = function("x**2 + log(x)"); f(5)
        """

        return self.expr.evalf(subs={self.var: value})

    def isConstant(self):
        """
        Returns true is function is a constant, i.e. f(x) = 1
        """

        if self.expr.is_constant():
            return true
        return false

    def getSymbol(self):
        """Returns the symbols involved in the function as a character

        E.g. f = function("x**2 + log(x)"); f.getSymbol() # returns 'x' 
        """

        return str(self.var)

    def diff(self, n=1):
        """Returns the n-th derivative of the function
        
        params:
            n (int): rank of Derivative

        Raises error if n is not a positive integer        
        """

        if n <= 0 or type(n) != int:
            raise AttributeError("Invalid parameter n")

        """ If function is constant then we should return zero manually
        because sympy cant handle differentiation of constant functions """
        if self.isConstant():
            return function(str("0"))
        newExpr = diff(self.expr, self.var, n)

        return function(str(newExpr))

if __name__ == "__main__":
    print(str(function("0").diff(4)))