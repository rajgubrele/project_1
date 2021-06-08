#############################################################################################################################
# Sample function is defined here for approximating the root at a certain level of tolerance
# x: Initial guess
# tol: Tolerance level
# itr: Iteration number
# .................................... CHOICES ..............................................................................
# Choice 0: Print the solution, function value and iteration number
# Choice 1: Generate Output file and print solution, function value, iteration
# Choice 2: Print solution, function value, iteration and generate the plot appoximation vs iteration
# Choice 3: Generate Output file and print solution, function value, iteration and plot appoximation vs iteration

# Example: 2 is taken as user's choice hence solution, iteration number, function value and the plot will be generated
#####################################################################################################################


import numpy as np                                                              # Importing numpy as np
import newton_raphson                                                           # Importing newton_raphson for finding roots


def f(x):                                                                       # Function defination
    w0 = 15
    L = 3
    E = 70
    I = 52.9 * (10 ** (-6))
    pi = np.pi
    f = ((w0 * L) / (3 * E * I * (pi ** 4))) * (
            (48 * (L ** 3) * np.cos((pi * x) / (2 * L))) - (48 * (L ** 3)) + (3 * (pi ** 3) * L * (x ** 2)) - (
            (pi ** 3) * (x ** 3)))                                              # Function expression
    return f                                                                    # Return function value


x = 4                                                                           # Initial guess                                                                     
tol = 1e-6                                                                      # Tolerance
itr = 100                                                                       # Iteartion number                                                                                                    

choice = 2                                                                      # Choice of user                                            

if (choice == 0) or (choice == 2):                                              
    newton_raphson.Newton(f, x, tol, itr, choice)                               # Calling function for Newton-Raphson method
    N = open("Newton_raphson.txt", "a")                                         # Opening file
    print("Initial guess: {:0.3f}".format(x), file =N)                          # Printing initial guess in output file
    print("Tolerance: {:0.7f}".format(tol), file =N)                            # Printing tolerance in output file
    N.close()                                                                   # Closing file
elif (choice == 3) or (choice == 1):                                            
    N = open("Newton_raphson.txt", "a")                                         # Opening file
    print("Initial guess: {:0.3f}".format(x), file =N)                          # Printing initial guess in output file
    print("Tolerance: {:0.7f}".format(tol), file =N)                            # Printing tolerance in output file
    newton_raphson.Newton(f, x, tol, itr, choice)                               # Function call for execution of Newton-Raphson method
    N.close()                                                                   # Closing file
