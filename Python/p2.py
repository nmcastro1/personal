#Problem 1: even fibonacci numbers below 4m

def fibonacci(cap):
  fibos = [1,2]

  while fibos[-1] < cap:
    fibos.append (fibos[-1] + fibos[-2])

  return fibos

def even_fibos_sum():
  fibos = fibonacci(4000000)
  fibo_sum = 0

  for fibo in fibos:
    if fibo % 2 == 0:
      fibo_sum += fibo

  return fibo_sum

def main():
  print even_fibos_sum ()

if __name__ == '__main__':
  main()