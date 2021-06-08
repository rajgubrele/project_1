#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
def dydx(x,y):
    if y<= 4000.0:
        n1 = 0
    else:
        n1 = 0.2*8*(y-4000.0)**2
    return ((42.0*x*math.exp(-0.273*x))+(10.0*math.cos(2.0*math.pi*x))-n1);
#initial guess value of x
x0=0;
# initial function value
y=3900;
# final x value
x=10;

