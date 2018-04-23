#Problem 10: sum of all primes below 2m

import math

def primes(n):
  prime_list = [2]
  i = 3

  while i < n:
    cap = math.trunc (math.sqrt (i))
    j = 0
    is_prime = True

    while prime_list[j] <= cap:
      if i % prime_list[j] == 0:
        is_prime = False
        break
      else:
        j += 1

    if is_prime:
      prime_list.append(i)

    i += 1

  return prime_list

def prime_sum():
  p_sum = 0

  for p in primes(2000000):
    p_sum += p

  return p_sum

def main():
  print prime_sum()

if __name__ == '__main__':
  main()
