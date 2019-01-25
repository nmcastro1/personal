#Problem 100 - The problem can be re-stated as find the first number n 
#such that 2x(x-1) divides some y(y-1) and y > 10^12
#This equation is a diophantine equation of second degree, with a solution in the recurrence
#xn+1 = 3 xn + 2 yn + 2 
#yn+1 = 4 xn + 3 yn + 3, with x0 = 0 and y0 = 0
#Solution found with this calculator https://www.alpertron.com.ar/QUAD.HTM

import math

def diophantineRecurrence(bound):
    x = [0]
    y = [0]

    while y[-1] < bound:
        if len(x) % 100000 == 0: print len(x)/100000
        x.append(3 * x[-1] + 2 * y[-1] + 2)
        y.append(4 * x[-2] + 3 * y[-1] + 3)
    return (x[-1], y[-1])

def problem_100():
    bound = 10**12
    x, y = diophantineRecurrence(bound)
    print x, y - x
    print 2 * x * (x+1), y* (y + 1)

if __name__ == '__main__':
    problem_100()
