#Problem 32 - Pandigital multiples

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

#generates compositions of n into k parts
def weak_compositions(boxes, balls, parent=tuple()):
  if boxes > 1:
    for i in xrange(balls + 1):
      for x in weak_compositions(boxes - 1, i, parent + (balls - i,)):
        yield x
  else:
    yield parent + (balls,)

#generates compositions of n into k parts, with each part being at least 1
def weaker_compositions(boxes, balls, parent=tuple()):
  if boxes > 1:
    for i in xrange(boxes - 1, balls):
      for x in weaker_compositions(boxes - 1, i, parent + (balls - i,)):
        yield x
  else:
    yield parent + (balls,)

def int_from_digits(digits):
  n = digits[0]
  for d in digits[1:]:
    n = n * 10 + d
  return n

def split_list(a,b):
  return lambda digits: int_from_digits(digits[a:b])

#each element is a lambda that takes a list, splits it, and returns the constructed digit
def range_generators():
  range_gens = []
  for a,b,c in weaker_compositions(3,9):
    range_gens.append((split_list(0,a), split_list(a, a + b), split_list(a + b, a + b + c)))
  return range_gens

def problem_32():
  products = set()
  range_gens = range_generators()

  for digits in permute([1,2,3,4,5,6,7,8,9]):
    for fmun, fmult, fprod in range_gens:
      multiplicand = fmun (digits)
      multiplier = fmult(digits)
      product = fprod(digits)

      if multiplicand * multiplier == product:
        products.add(product)

  return sum(products)

def main():
  print problem_32()

if __name__ == '__main__':
  main()