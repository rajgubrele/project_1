import numpy as np
import Secant #import Secant.py

def f(x):
    w0 = 15
    L = 3
    E = 70
    I = 52.9 * (10 ** (-6))
    pi = np.pi
    f = ((w0 * L) / (3 * E * I * (pi ** 4))) * (
            (48 * (L ** 3) * np.cos((pi * x) / (2 * L))) - (48 * (L ** 3)) + (3 * (pi ** 3) * L * (x ** 2)) - (
            (pi ** 3) * (x ** 3)))
    return f
e=1e-5
x1 = 4
x2 = 12
q=open('secant.txt', 'w')
print("Left end of the interval: {:f}".format(x1), file = q)
print("Right end of the interval: {:f}".format(x2), file = q)
print("Tolerance level: {:f}\n".format(e), file = q)
q.close()
itr=1000
e=1e-5
Secant.secant(f, x1, x2, e, itr)