#!/usr/bin/env python
# coding: utf-8

# In[5]:


from gauss_siedel import*
while True: #Loop for start the programe again if user gives invalid input, it'll stop untill user give valid input
    try: #If user give correct input this code will run and give the result
        A = np.array([[9,3,-1,1,0,2,-2],[0,12,4,1,-1,0,3],[1,-1,10,1,3,-2,2],[1,0,0,6,2,-1,0],[5,-1,0,1,8,0,-1],[-2,0,0,1,-1,4,0],[3,1,0,-2,6,0,15]])
        B = np.array([[-9],[5],[0],[7],[1],[-10],[2]])
        x1 =  int(input('Initial iteration of x1= '))
        x2 =  int(input('Initial iteration of x2= '))
        x3 =  int(input('Initial iteration of x3= '))
        x4 =  int(input('Initial iteration of x4= '))
        x5 =  int(input('Initial iteration of x5= '))
        x6 =  int(input('Initial iteration of x6= '))
        x7 =  int(input('Initial iteration of x7= '))
        T = 0.001
        mx = 100
        X = np.array([[x1],[x2],[x3],[x4],[x5],[x6],[x7]]) # Taking iteration for solving the equation 
        #print(gauss_seidel(A,B,X))
        gauss_seidel(A,B,X,T,mx)#output once user give correct input
        break #break the loop once user get the correct answer
    except ValueError:# if user give invalid input it give the feedback and ask user to give input again untill user gives the correct input
        print('You have entered "invalid iteration" instead of int, you have entered string or float,  while you are taking input for iteration')
        print('Enter any any integer number ex- -1,-2,-5,-100,-405, 0,1,2,100,450,4650 etc')
        print('not enter string, float exaple- "s", "d", "ffe", "fsdf", or 0.15, 0.54')
        print('Now you have to start entering iteration again from x1')

