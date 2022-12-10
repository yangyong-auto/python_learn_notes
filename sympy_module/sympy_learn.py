from sympy.plotting import plot3d
from sympy import *
x, y = symbols('x y')

I = integrate(atan(x))

plot3d(x*y, (x, -5, 5), (y, -5, 5))