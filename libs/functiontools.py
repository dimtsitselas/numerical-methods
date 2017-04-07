"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ functiontools.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is based on sympy module and is used to represent and handle one
variable functions.
"""

from sympy                      import *
from sympy.parsing.sympy_parser import parse_expr

class function():
    """ One variable mathematical function """

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

    def str(self):
        """
        Returns function as string
        """

        return str(self.expr)

    def getSymbol(self):
        """
        Returns the symbols involved in the function as a character
        """

        return str(self.var)

    def eval(self, value):
        """
        Evaluates the function at a given point.
        
        params:
            value: the value in which function is evaluated        
        """

        return self.expr.evalf(subs={self.var: value})

    def diff(self, n):
        """
        params:
            n (int): rank of derivative
        
        Returns the n-th derivative of the function
        """

        if n <= 0:
            raise AttributeError("Invalid parameter n")

        newExpr = diff(self.expr, self.var, n)

        return function(str(newExpr))