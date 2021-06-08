# -*- coding: utf-8 -*-
"""Simpson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zd_s9_ZeglqET03CQ1D72Ll6w2UmLRrb
"""

##############################################################################################################
########################### Simpson's 3/8 rule for Integration of a function #################################
##############################################################################################################
# The module contains the definition of the function: 1. Simpson(f,a,b,h,hvar,pltn), 2. Inbuilt(f,a,b)
# 1.1. Arguments of Simpson:
      # f   : Function for which the integral needs to be calculated
      # a,b : Initial and final values of interval in which integration is to be done
      # h   : Stepsize of the intervals used for estimation of integral
      # hvar: If hvar = 1, Integration is estimated for different step sizes (0.0001,0.001,0.01.0.1)
      # pltn: If pltn = 1, Plot of the function f is generated with points used for integration.
# 1.2. Default Output (Assign hvar = 0, pltn = 0):
      # The value of integration is printed as the default output.
# 1.3. Conditional Outputs (Assign hvar = 1 or pltn = 1 or both):
      # If pltn = 1, Matplotlib.pyplot is used to generate the plot of f with respect to xi.
      # If hvar = 1, Integration is carried out for different stepsizes (h).
# 1.4. Some important points:
      # Modules Matplotlib.pyplot, numpy, math are already imported as plt, np and m.
      # This can be used to input symbols like Pi (m.pi) or define trigonometric functions (np.sin(x)).
# 2.1. Inbuilt(f,a,b) function
      # Inbuilt function uses quad function from scipy.integrate to evaluate the integral.
      # It gives an idea of how close the value is to the Simpson's 3/8 method used in this module.
##############################################################################################################
######################### Steps to use the module to carry out the integration ###############################
##############################################################################################################
  # 1. Import the module simpson.py
  # 2. Define the function whose integration is to be estimated.
  # 3. Assign the values to a, b and h.
  # 4. For default output: Assign hvar = 0, pltn = 0.
  #    For conditional outputs:
  # 5. Assign hvar = 1 for the integration for different stepsizes (h).
  # 6. Assign pltn = 1 to get the plot of the function with respect to points used to evaluate the integral.
  # 7. Call the function Simpson(f,a,b,h,hvar,pltn) to estimate the integral.
  # 8. Call the function Inbuilt(f,a,b) to evaluate the integral using inbuilt function.
##############################################################################################################
################################ A sample example for using the module #######################################
##############################################################################################################
# from simpson import *
# def f(x):
#   return x**2
# a = -1
# b =  1 
# h =  0.01
# hvar = 0
# pltn = 0
# Simpson(f,a,b,h,hvar,pltn)
##############################################################################################################
##############################################################################################################   
import matplotlib.pyplot as plt 
import math as m 
import numpy as np
def Simpson(f,a,b,h,hvar,pltn): # This function estimates the integral
  try:
    z =[0]                                   # Stores the xi appended from for loop as list
    sum = 0                                  # Initial sum 
    N = int((b-a)/h)                         # Points in which the interval is divided
    out = open("Simpson.txt", "w")           # Generates output file
    for i in range (1,N):                    # Calculates xi and f(xi) for all the points and sums all f(xi)
      x = a + h*i
      z.append(x)
      if i%3==0:
        sum = sum+2*f(x)
      else:
        sum = sum+3*f(x)
    sum = sum + f(a) + f(b)                  
    Answer = (3*h/8)*sum                     # Final Answer or value of integral
    z.remove(0)
    w = np.array(z)                          # Converting list z to array w
    if pltn == 1:                            # Plot condition
      plt.plot(w,f(w))
      plt.xlabel('x') 
      plt.ylabel('f(x)')
      plt.title('Plot of given funtion for integration')
      plt.grid('on')
      plt.show()
    print('The value of Integration is {:f}'.format(Answer),file=out) # default output command
    if hvar == 1:                            # Condition for variation in h and the integration
      print(' '*(15-len('Stepsize'))+'Stepsize' + ' ' * (15-len('Integration')) + ' Integration',file = out)
      for i in range(5):                     # This loop prints different stepsizes and the integral 
        sum = 0
        N = int((b-a)/h)
        for i in range (1,N):
          x = a + h*i
          if i%3==0:
            sum = sum+2*f(x)
          else:
            sum = sum+3*f(x)
        sum = sum + f(a) + f(b)
        Ans = (3*h/8)*sum
        print('{:15.5f}{:15.7f}'.format((100*h),Ans,),file = out)
        h = h/10 
    out.close()
  except ZeroDivisionError:     # When f is such that it gives indefinite value for any point in interval
    print('Zero Division Error Encountered. Please check the input values')



# Computing the integral using Inbuilt command #
from scipy.integrate import quad
def Inbuilt(f,a,b):
  out = open("Simpson.txt", "w")
  print('Answer using inbuilt function is',quad(f,a,b),file = out)
  out.close()

################################################################################################################