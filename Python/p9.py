#Problem 10: pythagorean triplets that add up to 1000

import math

def triplets():
  for a in xrange(1,998):
    for b in xrange(1, 998):
      c = 1000 - a - b
      if (a*a + b*b) == (c*c):
        return (a,b,c)
  return (0,0,0)

def main():
  print triplets ()

if __name__ == '__main__':
  main()
