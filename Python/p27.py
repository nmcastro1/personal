#Problem 27 - Product of coefficients n^2 + an + b that spawns longest prime streak

import math

def primes(n):
  prime_list = [2]
  i = 3

  for i in xrange(3,n):
    cap = math.trunc (math.sqrt (i))
    is_prime = True
    j = 0

    while prime_list[j] <= cap:
      if i % prime_list[j] == 0:
        is_prime = False
        break
      else:
        j += 1

    if is_prime:
      prime_list.append(i)

  return prime_list

def is_prime(n, ps):
  cap = math.trunc (math.sqrt (n))
  i = 0

  while ps[i] <= cap:
    if n % ps[i] == 0:
      return False
    else:
      i += 1

  return True

def find_coefficients():
  max_chain = 0
  a = 2000
  b = 2000
  prime_list = primes(1000000)
  prime_check = [False for i in xrange(0,1000001)]

  for p in prime_list:
    prime_check[p] = True

  for i in xrange(-1000, 1001):
    for j in xrange(-1000, 1001):
      n = 0
      chain = True

      while chain:
        fn = n*n + i*n + j
        if fn > 0 and prime_check[fn]:
          n += 1
        else:
          chain = False

      if n > max_chain:
        a = i
        b = j
        max_chain = n

  return a * b

def main():
  print find_coefficients()

if __name__ == '__main__':
  main()

