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

    def getSymbol(self):
        """Returns the symbols involved in the function as a character

        E.g. f = function("x**2 + log(x)"); f.getSymbol() # returns 'x' 
        """

        return str(self.var)

    def eval(self, value):
        """Evaluates the function at a given point.
        
        params:
            value: the value in which function is evaluated

        e.g. f = function("x**2 + log(x)"); f(5)
        """

        return self.expr.evalf(subs={self.var: value})

    def diff(self, n):
        """Returns the n-th derivative of the function
        
        params:
            n (int): rank of Derivative

        Raises error if n is not a positive integer        
        """

        if n <= 0 or type(n) != int:
            raise AttributeError("Invalid parameter n")

        newExpr = diff(self.expr, self.var, n)

        return function(str(newExpr))