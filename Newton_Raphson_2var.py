import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

# Created by Raviv Herrera #

x = sy.Symbol('x')
y = sy.Symbol('y')
# System equations of 2 variables x , y #

f1 = x**2 + y
f2 = 5*x + 4 * y + 7

######################

FM = sy.Matrix(2, 1, (f1, f2))
first_guess = sy.Matrix(2, 1, [1, -1])


def newton_r_2var(Iter, func, x0):
    print(FM)
    for i in range(Iter):
        jac = sy.Matrix.jacobian(func, (x, y))
        rev_jac = jac.subs({x: x0[0], y: x0[1]})
        rev_jac = rev_jac.inv()
        next_x0 = x0 - rev_jac * func.subs({x: x0[0], y: x0[1]})
        x0 = next_x0
        print(f"The next Iteration : {next_x0.evalf()}")
    print(f"The Root of function {func} is  : {x0.evalf()}")


newton_r_2var(6, FM, first_guess)
