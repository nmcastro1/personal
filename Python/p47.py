#Problem 47 - First four consecutive integers to have four distinct prime factors
import math

#extends prime list up to a bound by checking against the current list's contents
def bound_prime_list(primes, n):
    for i in xrange(primes[-1], n+1):
        sqr = int(math.sqrt(i))
        isPrime = True
        for p in primes:
            if p > sqr: break
            if (i % p) == 0:
                isPrime = False
                break
        if isPrime: primes.append(i)

#returns true if the number n has exactly 4 distinct prime factors
def has_four_prime_factors(primes, n):
    factors = set()
    for p in primes:
        if n == 1 or len(factors) > 4: break
        if (n % p) == 0:
            while n % p == 0:
                n /= p
            factors.add(p)
    return len(factors) == 4

#We iterate until we find 4 consecutive numbers that have 4 distinct prime factors
def problem_47():
    streak = 0
    primes = [2,3]
    for n in xrange(2,1000000):
        if n > primes[-1]:
            bound_prime_list(primes, primes[-1]*10)
        if has_four_prime_factors(primes,n):
            streak += 1
        else:
            streak = 0
        if streak == 4:
            print (n-3)
            break

if __name__ == '__main__':
    problem_47()
