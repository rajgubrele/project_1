# -*- coding: utf-8 -*-
"""input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vYnuo2LT0KLd1qzEqSSfKExqalEcHo0z
"""

############################## Input File #############################################
##### Solution of Problem given for project stage 3 using simpson.py module############ 
from simpson import * # Import the module
def f(x):             # Define the function to be integrated
  return (2/(m.pi*x))*np.sin(x*n-x*x*x)

n = 1                 # n is an additional parameter used in f(x), Assigning n = 1
a = 1                 # Lower limit of the interval
b = 5                 # Upper limit of the interval
h = 0.01              # Stepsize
hvar = 1              # Condition to print Integral for varying stepsize
pltn = 1              # Condition to generate plot
Simpson(f,a,b,h,hvar,pltn) # Calling the Simpson function
## The output for these inputs is submitted in Simpson.txt file #############

# Generating the default output
def f(x):             # Define the function to be integrated
  return (2/(m.pi*x))*np.sin(x*n-x*x*x)

n = 1                 # n is an additional parameter used in f(x), Assigning n = 1
a = 1                 # Lower limit of the interval
b = 5                 # Upper limit of the interval
h = 0.01              # Stepsize
hvar = 0            
pltn = 0              
Simpson(f,a,b,h,hvar,pltn) # Calling the Simpson function

# Calling the Inbuilt function 
Inbuilt(f,a,b)

# Some additional application
n = 10      # Taking a different value of n
a = 0.0001 # Since function gives zero division error, so we take a value close to 0
b = 2
h = 0.01
hvar = 0
pltn = 1
Ans1 = Simpson(f,a,b,h,hvar,pltn)
print(Ans1)

# The Answer obtained from Inbuilt function for n = 10
Inbuilt(f,a,b)