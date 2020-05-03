


def dijkstra(maze):
    unvisited = set()
    for i in len(maze):
        for j in len(maze[i]):
            if maze[i,j] == 0:
                unvisited.add(maze[i,j])
    pass