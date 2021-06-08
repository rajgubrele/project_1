#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
np.set_printoptions(linewidth=np.inf) #Use to print row in single line

#The arguments of the gauss_siedel function are A, B, X, tolerance= T, maximum number of iterations =mx
def gauss_seidel(A,B,X,T,mx): #Defining a function The arguments of the gauss_siedel function should be A, B, X, tolerance, maximum number of iterations, parameter for printing of intermediate iterations

    out=open("gauss_seidel.out.txt","w") # For creating output file in txt format
    
    for f in range(len(A)): # This will check,and informed if the matrix is non diagonal dominant and break the matrix
        for g in range(len(A)):
            if ((A[f][f])**2)**(0.5)< ((A[f][g])**2)**(0.5):
                print("This matrix is non diagonal dominant matrix",file=out)
                break  
    A = np.matrix(A)     # Change Array into matrix

    print('A matrix : ','\n',A,'\n',file=out) #Printng matrix A, which is nothing but matrix of coefficient of variables
    print('B matrix : ','\n',B,'\n',file=out) #Printing matrix B, which is RHS values of equation
    U = np.triu(A, k = 1) # Use to find upper triangular matrix of A matrix
    print('Upper triangular matrix : ','\n',U,'\n',file=out)
    L = np.tril(A, k = 0) #Use to find lower triangular matrix of B matrix
    print('Lower triangular matrix : ','\n',L,'\n',file=out)
    I = np.linalg.inv(L) #Use to  fine the inverse of lower triangular matrix
    print('Inverse of Matrix : ','\n',I,'\n',file=out)
    ## By this we can add  appropriate titles to each column 
#     df=pd.DataFrame({"A0":A[:,0],   
#                  "A1":A[:,1],
#                  "A2":A[:,2],
#                  "A3":A[:,3],
#                  "A4":A[:,4],
#                  "A5":A[:,5],
#                  "A6":A[:,6],
#                 })
#     print("\nAny_Matrix a:\n")
#     print(df.round(3))
    for i in range(100): #For loop for geting the iteration
        X1 = I.dot(B-U.dot(X)) # Gauss seidel formula, which takes the value of I,B,U and Initial guess and update in X1
        print('Error = difference in Iteration No.{} - Iteration No.{}'.format(i+1,i),file=out) 
        print((((((X[:])**2)**0.5)-(((X1[:])**2)**0.5))**2)**0.5,'\n',file=out) # Error = difference between iterations
        pm = (((((X[:])**2)**0.5)-(((X1[:])**2)**0.5))**2)**0.5
        # This is used to stop the iteration when it reached the minimum error difference betweent two iteration, which is 0.001 here 
        if pm[0]<=0.001  and pm[1]<=0.001 and pm[2]<=0.001 and pm[3]<=0.001 and pm[4]<=0.001 and pm[5]<=0.001 and pm[6]<=0.001: 
            print('Number  of iteration : {}'.format(i+1),file=out)
            break
        # This is used to stop the iteration is it reached the maximum talrance limit, which is 100 here 

        if pm[0]>= 1000  and pm[1]>= 1000 and pm[2]>= 1000 and pm[3]>= 1000 and pm[4]>= 1000 and pm[5]>= 1000 and pm[6]>= 1000: 
            print('Error',file=out)
            break

                
        X=X1   # X is initial guess and X1 is updated value
        print('Iteration {}'.format(i+1),file=out) 
        print(X.round(3),'\n','\n',file=out)
        C = X.round(3)

    for i in range(len(C)): #Used for change printing format in X1 = Ans, X2 = Ans ..etc
        M ='x{}= {}'.format(i+1,C[i])
        print(M,file=out)
    out.close()     
    return ' '

