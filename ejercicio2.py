
from sympy import expand, symbols #uso simpy para que el codigo sea mas legible ya que es un algoritmo matematico
  
x, a, b, n = symbols('x a b n')
gfg_exp =  (a*x*b)^n
  
# uasamos expand para el metodo simpy
exp = expand(gfg_exp**1000)
print(exp)
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
 


