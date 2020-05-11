import numpy as np
import math
import turtle
from pen import Pen

class Node():
    def __init__(self,x,y,distance,visited = False):
        self.x = x
        self.y = y
        self.distance = distance
        self.visited = visited

def dijkstra(mazeObject,destination_i,destination_j,verbose=False):
    if verbose:
        pen = Pen()
        pen.color("yellow")
    maze = np.asarray(mazeObject.maze)
    dmaze = [[None for _ in range(len(maze))] for __ in range(len(maze))]
    unvisited = set()
    # print(dmaze)
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i,j] == 0:
                if i == 0 and j == 0:
                    dmaze[i][j] = Node(i,j,0)
                    unvisited.add((i,j))
                else:
                    cell = Node(i,j,math.inf)
                    dmaze[i][j] = cell
                    unvisited.add((i,j))
    current_spot = (0,0)
    while not dmaze[destination_i][destination_j].visited:
        x = current_spot[0]
        y = current_spot[1]
        for neighbor in mazeObject.getNeighbors(x,y):
            cell = dmaze[neighbor[0]][neighbor[1]]
            if not cell.visited:
                if verbose and not (x == 0 and y == 0) and not (x == destination_i and y == destination_j):
                        screenX = -300 + ((y + 1) * 24)
                        screenY = 300 - ((x + 1) * 24)
                        pen.goto(screenX,screenY)
                        pen.stamp()
                distance = 1 + dmaze[x][y].distance
                if distance < cell.distance:
                    cell.distance = distance
        dmaze[x][y].visited = True
        unvisited.remove((x,y))
        min_distance = math.inf
        for nodes in list(unvisited):
            x = nodes[0]
            y = nodes[1]
            # print(f"Get Next Node{x}:{y}")
            if dmaze[x][y].distance < min_distance:
                current_spot = nodes
                min_distance = dmaze[x][y].distance
        # print(f"Next Neighbor{current_spot[0]}:{current_spot[1]}")
    # print(f"Done: {dmaze[destination_i][destination_j].distance}")
    return dmaze[destination_i][destination_j].distance, dmaze