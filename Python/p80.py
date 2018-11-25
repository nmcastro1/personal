#Problem 80 - Sum of the digital sum of the first one hundred digits of the sqrt
#of the first one hundred natural numbers whose square root is irrational

import decimal

def problem_80():
    exclude = set([x**2 for x in range(1,10)])
    total = 0

    decimal.getcontext().prec = 110

    for i in xrange(1,100):
        if i not in exclude:
            n = decimal.Decimal(str(i)).sqrt().as_tuple()
            total += sum(n[1][:100])

    print total

if __name__ == '__main__':
    problem_80()
