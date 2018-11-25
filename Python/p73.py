#Problem 73 - Counting reduced proper fractions in a range (n/d where HCF(n,d)=1)
#Count the fractions between 1/3 and 1/2 for d<=12000

import fractions


def problem_73():
    proper_fractions = 0

    for i in xrange(2,12001):
        for j in xrange(i/3 + 1, i / 2 if (i%2)==0 else (i+1) / 2):
            if fractions.gcd(i,j) == 1:
                proper_fractions += 1

    print proper_fractions
    

if __name__ == '__main__':
    problem_73()
