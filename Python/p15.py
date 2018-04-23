#Problem 15 - Lattice paths from (0,0) to (20,20)

def lattice_paths(n):
  num_paths = [[0 for l in xrange(n + 1)] for k in xrange(n + 1)]

  for x in xrange(n + 1):
    num_paths[0][x] = 1

  for x in xrange(n + 1):
    num_paths[x][0] = 1

  for i in xrange(n):
    for j in xrange(n):
      num_paths[i + 1][j + 1] = num_paths[i + 1][j] + num_paths[i][j + 1]

  return num_paths[-1][-1]


def main():
  print lattice_paths(20)

if __name__ == '__main__':
  main()
