# #########################################################################################################
# Newton-Raphson method approximates the root of any real polynomial function
# .........................................................................................................
# f: Arbitary function to be approximated
# df: Derivative of the function f
# H: List with oly zero element to append all the approximations of the root of the function f
# N: Output file
# h: limit to define derivative of a function f
# y: Approximation of either the initial guess or the previous approximation
# c: Iteration number
# ...................................Method................................................................
# After an initial guess approximations are calculated by the formula y=x-((f(x))/(f'(x)))
# If the derivative of any approximation is equal to zero then user have to make an initial guess again
# After calculating the approximations the approximations are stored in the list, H
# At the end of storing all the approximations in the list the first element(0) is deleted
# #########################################################################################################

import numpy as np
import matplotlib.pyplot as plt


def Newton(f, x, tol, itr, choice):                                                   # Defining of 'Newton-Raphson' function
    N = open("Newton_raphson.txt", "w")

    def df(x):                                                                        # Defination of differentiation  of function
        h = tol
        return (f(x + h) - f(x - h)) / h                                              # Retun function value for ceratin x value

    print(' ' * 70)
    H = np.array([0])                                                                 # Creating array
    c = 0                                                                             # Initializing iteration at zero
    if f(x) == 0:
        print('{:0.4f} is the root of the function.'.format(x),
              file=N)                                                                 # Print exact value of root if function vanishes
    else:
        if df(x) != 0:
            y = x - ((f(x)) / (df(x)))                                                # Approximation of initial guess
            if (choice == 1) or (choice == 3):
                print(' ' * (15 - len('iteration')) + 'iteration' + ' ' * (
                        14 - len('xi')) + 'xi' + ' ' * (
                              15 - len('f(xi)')) + ' f(xi)', file=N)                  # Column names
                print('-' * 45, file=N)
            while abs(f(y)) >= tol and itr < 150:                                     # condition of convergence
                x = y                                                                 # Taking approxiamtion as a inital
                y = x - ((f(x)) / (df(x)))                                            # Approximation if the absolute value of function is greater than tolerance
                c = c + 1                                                             # counting iteration number
                H = np.append(H, y)                                                   # Appending approximation of initial guess in the list
                if (choice == 1) or (choice == 3):
                    print('{:15d}{:14.5f} {:15.5f}'.format(c, y, f(y)), file=N)       # Iteration number, aproximation, function value of approximation and iteration number

        else:
            print('Assign a new value of initial guess', file=N)                      # Initial guess is wrong if derivative of initial guess vanishes

        itr=c
        if (choice == 0) or (choice == 1) or (choice == 3) or (choice == 2):
            print('\n{:0.7f} is the final approximation of the root.'.format(y))      # Printing final approximation
            print("Iteration number= {:d}".format(c))                                 # Printing iteration number
            print('Function value at the final approximation is {:0.7f}'.format(f(y)))

        H = np.delete(H, 0)                                                           # Removing first element from the list
        if (choice == 2) or (choice == 3):
            x = np.linspace(0, c, c)                                                  # listing the approximations
            plt.plot(x, H, 'r')                                                       # Plotting approximation vs iteration
            plt.xlabel('iteration')                                                   # Labelling x-axis as 'ITERATION'
            plt.ylabel('x_i')                                                         # Labelling y axis as 'APPROXIMATION'
            plt.grid('on')
            plt.show()                                                                # Plotting of approximate values with iteration values
    N.close()                                                                         # Closing txt file
