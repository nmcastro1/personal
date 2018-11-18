#Problem 58 - Number spiral, calculate the ratios of primes/total numebers in both diagonals
#What is the side-length of the square where the ratio first falls below 10%
import math

def is_prime(primes, n):
    sqr = int(math.ceil(math.sqrt(n)))
    isPrime = True
    for p in primes:
        if p > sqr: break
        if (n % p) == 0:
            isPrime = False
            break
    return isPrime

#Fill up the list with primes up to a bound
def bound_prime_list(primes, n):
    for i in xrange(primes[-1], n+1, 2):
        if is_prime(primes, i): primes.append(i)

#no need to calculate the square, just generate the number in each diagonal by the
#following algorithm
def problem_58():
    primes = [2,3]
    prime_count = 0
    n = 3
    step = 2
    ratio = 1.0
    while ratio >= 0.1:
        if primes[-1] <= n:
            #we expand the list of primes up to two new rings around the spiral
            bound_prime_list(primes, int(math.ceil(math.sqrt(n + 7 * step + 8))))
        for i in xrange(n, n + 4 * step, step):
            if is_prime(primes, i): prime_count += 1
        n += 4 * step + 2
        ratio = prime_count * 1.0 / (2 * step + 1)
        step += 2
    print prime_count, n
    print (step - 1)

if __name__ == '__main__':
    problem_58()