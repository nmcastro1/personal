#Problem 86 - Counting all the routes on a cubiod of dimensions up to M by M by M,
#where the shortest route from S to F is of integer length, 
#find the first M for which the number of solutions first exceeds one million

import math

#once we have found a value of i that works, we calculate all the ways we can generate
#i = y + z with the condition that y,z < x = m
def combinationsXY(i, m):
    if i <= m:
        return i / 2
    else:
        return (i / 2) - (i - m) + 1

#When drawing the shortest path you realize that the diagonal length on the triplet (x,y,z)
#with x>=y>=z is sqrt(x^2 + (y+z)^2). So we consolidate y+z as i and test in the range 2..2x
def problem_86():
    solutions = 0
    m = 1

    while solutions < 1000000:
        for i in xrange(2, 2*m+1):
            diagonal = math.sqrt(m**2 + (i)**2)
            if (diagonal - math.floor(diagonal)) < 0.0000001:
                solutions += combinationsXY(i, m)
        if m % 10 == 0: 
            print ("%d solutions for m=%d") % (solutions, m)
        m += 1

    print (m - 1)

if __name__ == '__main__':
    problem_86()
