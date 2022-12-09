
from simpy import expand, symbols 
  
x, a, b, y, n= symbols('x a b y n') 
gfg_exp =  (ax b)^n
  
exp = sympy.expand((ax b)^n) 
  
print(exp)

