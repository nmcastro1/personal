#Problem 83 - Minimal path sum in a 80 by 80 matrix, from the top left to the bottom right
#can move in any non-diagonal direction

from itertools import chain

#This solution is similar to the one used for problem 82. The difference is that
#we can move in one more direction and we only have one starting node instead of many
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #Unknown distance from source to node
        self.dist = 10**10

    def __eq__(self, other):
        return self.position == other.position


def dijkstra(graph, grid, start):
    vertexset = dict()

    #Slight variation in dijkstra's original algorithm. Here we account the start square's 
    #original cost, instead of initializing it to zero.
    #In this problem, costs lie in the nodes themselves instead of the node's edges
    #The cost of moving from u to v is instead calculated as the cost of node v itself.
    graph[start[0]][start[1]].dist = grid[start[0]][start[1]]

    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            vertexset[(i,j)] = graph[i][j].dist

    while len(vertexset) > 0:
        (pos, dist) = reduce(lambda x, y: x if x[1] < y[1] else y, vertexset.iteritems())

        del vertexset[pos]

        #For each neighbor of u
        for (i, j) in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            (x, y) = (pos[0] + i, pos[1] + j)

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
                continue

            alt = dist + grid[x][y]
            if alt < graph[x][y].dist:
                graph[x][y].dist = alt
                graph[x][y].parent = graph[pos[0]][pos[1]]
                vertexset[(x,y)] = alt


def problem_82():

    fp = open("problem files/p082_matrix.txt")

    #test grid
    '''grid = [[131,673,234,103,18],
            [201,96,342,965,150],
            [630,803,746,422,111],
            [537,699,497,121,956],
            [805,732,524,37,331]]'''

    grid = map(lambda line: map(int, line.split(',')), fp.read().splitlines())

    fp.close()
    
    graph = []

    for i in xrange(len(grid)):
        row = []
        for j in xrange(len(grid[i])):
            row.append(Node(None,(i,j)))
        graph.append(row)

    dijkstra(graph, grid, (0, 0))

    #The goal node is at the bottom right position in the grid
    print graph[-1][-1].dist


if __name__ == '__main__':
    problem_82()
