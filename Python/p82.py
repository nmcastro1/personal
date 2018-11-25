#Problem 83 - Minimal path sum in a 80 by 80 matrix, from the left column to the right column
#can only move up, down or right

#Solution using dijkstra path-finding algorithm. I picked this over A* since we have
#multiple starting nodes and multiple goals.
#A possible A* solution would have reused previously-computed paths instead of re-running the algorithm
#multiple times

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #Unknown distance from source to node, initialize it to a large value
        self.dist = 10**10

    def __eq__(self, other):
        return self.position == other.position


def dijkstra(graph, grid):
    vertexset = dict()

    #instead of initializing only the start node, we initialize the whole left column
    for i in xrange(len(grid)):
        graph[i][0].dist = grid[i][0]

    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            vertexset[(i,j)] = graph[i][j].dist

    while len(vertexset) > 0:
        (pos, dist) = reduce(lambda x, y: x if x[1] < y[1] else y, vertexset.iteritems())

        del vertexset[pos]

        #For each neighbor of u
        for (i, j) in [(0, 1), (-1, 0), (1, 0)]:
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

    #problem test grid
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

    dijkstra(graph, grid)
    
    #We explore all the distances to the nodes in the right column, looking for the smallest one
    col = 0
    min_dist = graph[0][-1].dist
    for i in xrange(1, len(grid)):
        if graph[i][-1].dist < min_dist:
            col = i
            min_dist = graph[i][-1].dist

    print min_dist


if __name__ == '__main__':
    problem_82()
