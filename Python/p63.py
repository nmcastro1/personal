#Problem 63 - How many n-digit positive integers are also a nth power

def count_digits(n):
    digits = 0
    while n > 0:
        n /= 10
        digits += 1
    return digits

#10^n has n+1 digits, so we clearly only have to check bases below 10
#if 9^n has less than n digits, it means from that point on there wont be any more solutions. so we exit
def problem_63():
    ncount = 0
    for n in xrange(1,1000):
        for base in xrange(1,10):
            if count_digits(base**n) == n:
                ncount += 1

        if count_digits(9**n) < n:
            break
    print ncount

    
if __name__ == '__main__':
    problem_63()