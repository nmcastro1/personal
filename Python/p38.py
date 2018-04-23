#Problem 38 - Largest pandigital generated concatenating f(x) = xn, n > 1

def permute(xs, low=0):
  if low + 1 >= len(xs):
    yield xs
  else:
    for p in permute(xs, low + 1):
      yield p
    for i in range(low + 1, len(xs)):
      xs[low], xs[i] = xs[i], xs[low]
      for p in permute(xs, low + 1):
        yield p
      xs[low], xs[i] = xs[i], xs[low]

def number_of_digits_a(n):
  digits = 0
  while n:
    n //= 10
    digits += 1

  return digits
#More efficient. up to 5x on 10 digit long numbers
def number_of_digits(n):
  if n < 100000:
    if n < 100:
      if n < 10:
        return 1
      else:
        return 2
    elif n < 10000:
      if n < 1000:
        return 3
      else: 
        return 4
    else: return 5
  else:
    if n < 10000000:
      if n < 1000000:
        return 6
      else:
        return 7
    elif n < 1000000000:
      if n < 100000000:
        return 8
      else: 
        return 9
    else: return 10
    
def perm_test():
  for p in permute([5, 4, 3, 2, 1]):
    if p[0] != 5: break;
    print p

def problem_38():
  pandigitals = []
  for digits in permute([9,8,7,6,5,4,3,2,1]):
  #for digits in permute([1,2,3,4,5,6,7,8,9]):
    if digits[0] != 9: break
    pan = digits[0]
    for d in digits[1:]:
      pan = pan * 10 + d

    for l in xrange(1,5):
      seed = digits[0]
      for d in digits[1:l]:
        seed = seed * 10 + d
      concatd = seed
      n = 2
      while concatd < 100000000:
        t = seed * n
        concatd = concatd * (10**(number_of_digits(t))) + t
        n += 1
      if concatd == pan:
        pandigitals.append((pan, seed))
        break

  return pandigitals

def main():
  print problem_38()

  

if __name__ == '__main__':
  main()
