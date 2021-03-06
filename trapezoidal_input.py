# -*- coding: utf-8 -*-
"""input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HHlcEmCdIcmgcZFwdiK_U1pYKc9wm02A
"""

###   Input file   ####

from trapezoidal import *
def f(x):                             # definition of given function
        return (2/(m.pi*x))*np.sin(x*n-x*x*x)
a=0.001                           # can not take zero
b=10
h=0.01
hvar=1
pltn=1                           # plot will be generated
n=1
trapezoidal(f,a,b,h,hvar,pltn)

Test(f,a,b)