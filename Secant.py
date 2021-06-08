import math
import numpy as np
import matplotlib.pyplot as plt
#Define Secant function
def secant(f, x1, x2, e, itr):
    q = open('Secant.txt', 'w') #command for creating Secant.txt file
    s = [0]
    n = 0;
    xm = 0;
    x0 = 0;
    c = 0;
#Chceck Zero is a root of given fuction
    if f(x1) * f(x2) == 0:
            print('0 is the root')
    else:
        print(' ' * (15 - len('Iteration')) + 'Iteration' + ' ' * (15 - len('x1')) + 'x1' + ' ' * (
                    15 - len('x2')) + 'x2' + ' ' * (15 - len('f(x1)')) + 'f(x1)' + ' ' * (15 - len('f(x2)')) + 'f(x2)',
              file=q)
        print('-' * 75, file=q)
        while n < itr:
            x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); #Calculate intermediate value according to secant rule
            c = f(x1) * f(x0);
            x1 = x2; #Update interval
            x2 = x0;
            n += 1; #update no. of iteration
            s.append(x0) #Store x0 value
            if (c == 0):
                break;
            xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); #check intermediate value after updating interval

            print('{:15d}{:15.5f}{:15.5f}{:15.5f}{:15.5f}'.format(n, x0, xm, f(x0), f(xm)), file=q)
            if (abs(xm - x0) < e): #check convergence
                break;

        print(' ' * 60)
        print('Final approximation of the root of the given equation = {: .5f} at {:d}th iteration'.format(x0, n));
        print('no of iteration =', n )
        print("Function value: {:f}".format(f(xm)))
#command for ploting xi vs i
        s.remove(0)
        t = np.linspace(x0, n , n)
        plt.plot(t, s, 'b--')
        plt.xlabel('ITERATION')
        plt.ylabel('x_i')
        plt.grid('on')
        plt.show()
    q.close()
