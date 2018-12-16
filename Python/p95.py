#Problem 95 - Amicable chains - find the sum of the proper divisors of a number
#then find the sum of the proper divisors of the previous result, and so on
#if the result produces the first number again, this is considered an amicable chain
#Find the longest amicable chain with all members being lower than 1 million

import math

#Slight variation of Erathostenes' sieve, instead of marking a number that it is divisible
#by a prime p, we add that prime factor's contribution to n's divisor sum
def divisorSumSieve(divsums, bound):
    for n in xrange(2,bound):
        if divsums[n] == 1:
            #n is prime
            primepower = n
            while primepower < bound:
                factor = (primepower * n - 1) / (n - 1)
                nextpower = primepower*n
                for i in xrange(primepower, bound, primepower):
                    #We multiply by the factor only if this number i is divisible by p^k
                    #but not by p^(k+1). We handle the latter case on the next iteration of the outer loop
                    if i % (nextpower) == 0: continue
                    divsums[i] *= factor
                primepower *= n
        divsums[n] -= n

def problem_95():
    bound = 10**6
    divsums = [1]*(bound +1)
    looptests = [False]*(bound + 1)
    looptests[1] = True
    maxChainLength = 0
    minElement = 0

    divisorSumSieve(divsums, bound)

    for i in xrange(2, bound):
        #Entering this if only if this number hasn't been checked yet
        if not looptests[i]:
            chain = []
            haveChain = True
            k = i
            while k not in chain:
                #The new chain is invalid if the number has been previously visited or greater than 10^6
                if k > bound or looptests[k]:
                    haveChain = False
                    break
                else:
                    chain.append(k)
                    k = divsums[k]

            #The actual loop starts where k first appears, so we calculate the correct index
            if haveChain:
                index = chain.index(k)
                if len(chain[index:]) > maxChainLength:
                    maxChainLength = len(chain[index:])
                    minElement = min(chain[index:])

    print minElement, maxChainLength

if __name__ == '__main__':
    problem_95()
