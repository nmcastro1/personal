#Problem 23 - Abundant if the sum of his proper divisors exeeds n. Sum of non-abundant positive integers
import math

def abundant_numbers(n):
  prime_list = [2]
  abundant_list = []

  for i in xrange(3,n + 1):
    factors = {}
    cap = math.trunc (math.sqrt (i))
    j = 0
    k = i
    #calculate factors
    while k != 1 and (k != i or prime_list[j] <= cap):
      if k % prime_list[j] == 0:
        if prime_list[j] in factors:
          factors[prime_list[j]] += 1
        else:
          factors[prime_list[j]] = 1

        k = k // prime_list[j]
        continue
      else:
        j += 1
    #new prime number found
    if k == i:
      prime_list.append(i)
      del factors
      continue
    #calculate divisor sum
    divisor_sum = 1
    for p, e in factors.items():
      divisor_sum *= (p**(e + 1) - 1) // (p - 1)
    #add new abundant
    if (divisor_sum - i) > i:
      abundant_list.append(i)

    del factors

  return abundant_list

def sum_of_two(n):
  abundant_list = abundant_numbers(n)
  #A 1 means it can't be expressed as the sum of two abundant
  sum_of_abundants = [1 for x in xrange(n + 1)]
  abundant_sum = 0
  i = 0

  while i < len(abundant_list):
    j = i
    while j < len(abundant_list):
      x = abundant_list[i] + abundant_list[j] 
      if x <= n and sum_of_abundants[x]:
        sum_of_abundants[x] = 0
      j += 1
    i += 1

  i = 1
  while i < len(sum_of_abundants):
    if sum_of_abundants[i]: abundant_sum += i
    i += 1

  return abundant_sum


def main():
  print sum_of_two(28122)

if __name__ == '__main__':
  main()
