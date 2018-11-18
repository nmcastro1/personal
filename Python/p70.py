#Problem 70 - Totient permutation: find a number n < 10^7 for which o(n) is a permutation of n
#and the ratio n/o(n) produces a minimum

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

def is_permutation(n, m):
    digits = [0]*10

    while n > 0:
        digits[n % 10] += 1
        n /= 10
    while m > 0:
        digits[m % 10] -= 1
        m /= 10
    return digits.count(0) == 10

def is_permutatiom(n, m):
    digits = {}
    while n > 0:
        if (n % 10) in digits:
            digits[n % 10] += 1
        else:
            digits[n % 10] = 1
        n /= 10
    while m > 0:
        if (m % 10) in digits:
            digits[m % 10] -= 1
        else:
            return False
        m /= 10
    return list(digits.itervalues()).count(0) == len(digits)


#totient function, formula from https://en.wikipedia.org/wiki/Euler%27s_totient_function
def totient(primes, tots, n):
    k = n
    sqr = int(math.ceil(math.sqrt(n)))
    for p in primes:
        if k == 1: break
        if p > sqr and k == n: #n is prime
            tots[n] = n - 1
            return n - 1 
        if (k % p) == 0:
            while (k % p) == 0:
                k /= p
            if k == 1: #n = p^k
                tots[n] = n * (p-1) / p
                return tots[n]
            else:
                break
    tots[n] = tots[k] * tots[n/k]
    return tots[n]

def problem_70():
    min_ratio = 10000000.0
    min_n = 0
    primes = [2,3,5]

    tots = [0]*10000000
    bound_prime_list(primes, int(math.ceil(math.sqrt(10000000))))
    
    for n in xrange(2,10000000):
        tot = totient(primes, tots, n)
        #n is a digit-permutation of totient if n = tot (mod 9)
        if (n % 9) == (tot % 9): 
            if is_permutation(n, tot):
                ratio = n * 1.0 / tot
                if ratio < min_ratio:
                    min_n = n
                    min_ratio = ratio
    print min_n, min_ratio

if __name__ == '__main__':
    problem_70()
