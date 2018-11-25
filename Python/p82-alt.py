#Problem 83 - Minimal path sum in a 80 by 80 matrix, from the left column to the right column
#can only move up, down or right

#Alternative solution using dinamic programming instead of path-finding algorithms
def min_sum(grid):
    min_sums = [([0]*len(grid)) for i in xrange(len(grid))]

    #initialize left column
    for i in xrange(len(grid)):
        min_sums[i][0] = grid[i][0]

    for col in xrange(1, len(grid)):
        for row in xrange(len(grid)):
            temp_col = [0]*len(grid)

            #calculate the sum of a path through rows above current square
            ssum = 0
            for i in xrange(row - 1, -1, -1):
                ssum += grid[i][col]
                temp_col[i] = ssum

            #calculate the sum of a path through rows below current square
            ssum = 0
            for i in xrange(row + 1, len(grid)):
                ssum += grid[i][col]
                temp_col[i] = ssum

            #the min path to [row][col] is the shortest path between the square to its left
            #and the shortest paths moving up or down through its column
            curren_min = min_sums[row][col - 1]
            for i in xrange(len(grid)):
                if temp_col > 0:
                    curren_min = min(curren_min, temp_col[i] + min_sums[i][col - 1])

            min_sums[row][col] = curren_min + grid[row][col]

    return min_sums


def problem_82():

    fp = open("problem files/p082_matrix.txt")

    '''grid = [[131,673,234,103,18],
            [201,96,342,965,150],
            [630,803,746,422,111],
            [537,699,497,121,956],
            [805,732,524,37,331]]'''

    grid = map(lambda line: map(int, line.split(',')), fp.read().splitlines())

    fp.close()

    min_sums = min_sum(grid)
    min_dist = min_sums[0][-1]
    for i in xrange(1, len(grid)):
        min_dist = min(min_dist, min_sums[i][-1])

    print min_dist


if __name__ == '__main__':
    problem_82()
