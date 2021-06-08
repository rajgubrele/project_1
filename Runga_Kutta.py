#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import math
import matplotlib.pyplot as plt
import input2 

# import the input2.py module
#flag to examine the variation in the solution with different step size or a value at step size
hvar = input('Please enter 1 for different step sizes or 0 for the default step size')
hvar = int(hvar)
if hvar == 1:                            
    h=[]
    for j in range(1,5):                # for 4 different values of the step size
        d =input('Enter the four different step size');
        d = float(d);
        h.append(d)
        j = j+1;

if hvar == 0:
    h=[]
    d = input("Enter the default step_size");
    d = float(d);
    h.append(d)
    
z=['r--','g--','b--','y--']                  #string for different colours in the chart

#Function to solve the differential equation by using second order rungekutta method
fig , ax=plt.subplots(nrows = 2, ncols = 2, figsize=(12,10))
for g in range(0,len(h)):
    a=[]
    b=[]
    def rungekutta(x0,y0,x,h):
        # number of iterations
        n = round ((x-x0)/h);
        y = y0;
        for i in range(1,n+1):
            #next value of y
            k1 = h*input2.dydx(x0,y);
            k2 = h*input2.dydx(x0+h,y+k1);
            k = (k1+k2)/2
            # update the next value of x
            x0 = x0 + h;
            # update the value of y
            y = y + k;
            a.append(x0)
            b.append(y)
            print(f'{x0:15}               {y:15}')
        return y;
    g=g+1;
   
    print(rungekutta(input2.x0,input2.y,input2.x,h[g-1]))
    
    if g == 1 or g == 2:
        ax[0][g-1].plot(a,b,z[g-1])
        ax[0][g-1].set_title('Approximate Solution Runge-Kutta Method')
        
    else:
        ax[1][g-3].plot(a,b,z[g-1])
        ax[1][g-3].set_title('Approximate Solution with Runge-Kutta Method')
import sys
f = open("output.txt", 'w')
sys.stdout = f
print(rungekutta(input2.x0,input2.y,input2.x,h[g-1]))
f.close()
#plt.show()
 
    

    
        
    
           


# In[ ]:





# 1# 1
# # 
