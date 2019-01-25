#Problem 105 - Identify all the special sum sets Ai and calculate the sum of the S(Ai)

import math
from itertools import chain, combinations

def powerset(baseSet):
    return chain.from_iterable(combinations(baseSet,n) for n in range(len(baseSet)+1))

def isSpecialSumSet(baseSet):
    setSums = set()
    baseSet.sort()
    minSums = []
    maxSums = []

    #Rule ii, two disjoint subsets should have different element sums
    for subset in powerset(baseSet):
        subsetSum = sum(subset)
        if subsetSum not in setSums:
            setSums.add(subsetSum)
        else:
            return False

    #Rule i, if B has more elements than C, S(B) > S(C)
    #If the elements are sorted, we can easily find the subsets which will have the min and max sums
    for i in xrange(1,len(baseSet)):
        minSums.append(sum(baseSet[:i]))
        maxSums.append(sum(baseSet[-i:]))

    #For rule i, the max sum for subsets of i elements have to be less than the min sum
    #for subsets with i+1 elements
    for i in xrange(len(maxSums) - 1):
        if maxSums[i] >= minSums[i+1]:
            return False

    return True

def problem_105():
    specialSums = 0
    '''
    nonSpecialTestSet = [81, 88, 75, 42, 87, 84, 86, 65]
    specialTestSet = [157, 150, 164, 119, 79, 159, 161, 139, 158]

    print "Testing non special set with result %r" % isSpecialSumSet(nonSpecialTestSet)
    print "Testing special set with result %r, and S(A) = %d" % (isSpecialSumSet(specialTestSet), sum(specialTestSet))
    '''
    fp = open("problem files/p105_sets.txt")

    sets = map(lambda line: map(int, line.split(',')), fp.read().splitlines())

    fp.close()

    for aset in sets:
        if isSpecialSumSet(aset):
            specialSums += sum(aset)

    print specialSums

if __name__ == '__main__':
    problem_105()
