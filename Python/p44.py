#Problem 44 - Lowest difference between two pentagonal numbers 
#where both their sum and difference are pentagonal

#calculate pentagonal numbers with a bound
#a pentagonal number is a number of the form p(n) = n*(3n-1)/2
def pentagonal_set(n):
    pentagonals = set()
    pentagonal = 0
    i = 1
    while i < n:
        pentagonal = (i * (3*i - 1)) / 2
        pentagonals.add(pentagonal)
        i += 1
    return pentagonals


def problem_44():
    pentagonals = pentagonal_set(10000)
    d = float('inf')
    for i in pentagonals:
        for j in pentagonals:
            if i != j and (i+j) in pentagonals and (abs(i-j)) in pentagonals:
                d = min(d,abs(i-j))
    print d

if __name__ == '__main__':
    problem_44()
