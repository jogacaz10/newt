import unittest
import math
import sympy as sp
from newton_rhapson.newton import ne
class TestRhapson(unittest.TestCase):

    def test_t1(self):
        x=sp.symbols('x')
        fx= math.e**x-3*x**2
        res=0.02
        Ni=100
        a=0
        b=1 
        result=ne(Ni,a,b,res,fx,x) 
        print(result)
        self.assertEqual(result[0], 0.9103966648720174) 
        self.assertEqual(result[1], 0.028372547577672876) 


