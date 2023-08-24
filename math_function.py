from sympy import *
import numpy as np

class Function:
    def _init_(self):
        self.x = Symbol('x')
        self.function = self.x**2 + cos(5*self.x) + self.x**3 + 1
        self.derivative = self.function.diff(self.x)
    def value(self, point):
        f = lambdify(self.x, self.function, 'numpy')
        return f(point)
    def deri(self, point):
        f = lambdify(self.x, self.derivative, 'numpy')
        return f(point)
        
    
        


    