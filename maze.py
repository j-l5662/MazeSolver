import sys
import random
import enum 
import numpy as np 
import time
import turtle
import math
import os
import io
from PIL import Image 


class Node():
    def __init__(self,x,y,distance,visited = False):
        self.x = x
        self.y = y
        self.distance = distance
        self.visited = visited

    
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class GreenPen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class RedPen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Maze:
    def __init__(self,graphSize):

        self.size = graphSize
        self.maze = np.random.randint(1,100,size=(graphSize,graphSize))
        self.entrance = (0,0)
        self.generateMaze()
        

    def generateMaze(self):
        visited = []
        x = 0
        y = 0
        self.makePassage(x,y)
        self.addNeighbors(x-1,y,visited)
        self.addNeighbors(x+1,y,visited)
        self.addNeighbors(x,y+1,visited)
        self.addNeighbors(x,y-1,visited)
        # https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm
        # https://stackoverflow.com/questions/23843197/maze-generating-algorithm-in-grid
        while len(visited) > 0:
            cell = random.choice(visited)
            x = cell[0]
            y = cell[1]
            if self.validPassage(x,y):
                self.makePassage(x,y)
                self.addNeighbors(x-1,y,visited)
                self.addNeighbors(x+1,y,visited)
                self.addNeighbors(x,y+1,visited)
                self.addNeighbors(x,y-1,visited)
            visited.remove(cell)
        i = self.size - 1
        checkMaze = np.asarray(self.maze)
        while i >= 0:
            j =  self.size - 1
            while j >= 0:
                if checkMaze[i,j] == 0:
                    self.exit = (i,j)
                    return
                j -= 1
            i -= 1
        
    
    def addNeighbors(self,x,y,visited):
        if self.inBounds(x,y) and self.maze[x,y] != 0:
            visited.append((x,y))
        return

    def validPassage(self,x,y):
        count = 0 
        if self.inBounds(x+1,y) and self.maze[x+1,y] == 0:
            count += 1
        if self.inBounds(x-1,y) and self.maze[x-1,y] == 0:
            count += 1
        if self.inBounds(x,y-1) and self.maze[x,y-1] == 0:
            count += 1
        if self.inBounds(x,y+1) and self.maze[x,y+1] == 0:
            count += 1
        return count < 2


    def inBounds(self,x,y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size

    def getNeighbors(self,x,y):
        neighbors = []
        if self.inBounds(x+1,y) and self.maze[x+1,y] == 0:
            neighbors.append((x+1,y))
        if self.inBounds(x-1,y) and self.maze[x-1,y] == 0:
            neighbors.append((x-1,y))
        if self.inBounds(x,y-1) and self.maze[x,y-1] == 0:
            neighbors.append((x,y-1))
        if self.inBounds(x,y+1) and self.maze[x,y+1] == 0:
           neighbors.append((x,y+1))
        return neighbors
            
    def makePassage(self,x,y):
        self.maze[x,y] = 0

    def drawMaze(self):
        maze = np.asarray(self.maze)
        testMaze = []
        testMaze.append('X' * (g.size+2))
        for i in range(self.size):
           str = 'X'
           for j in range(self.size):
               if maze[i,j] != 0:
                   str = str + 'X'
               else:
                   str = str + ' '
           str = str + 'X'
           testMaze.append(str)
        testMaze.append('X' * (g.size+2))

        return testMaze

    def printMaze(self):
        maze = np.asarray(self.maze)
        for i in range(self.size):
           if i == 0:
                for j in range(self.size+2):
                    print("X",end='')
                print()
           for j in range(self.size):
               if j == 0:
                   print("X",end='')
               if maze[i,j] != 0:
                   print("X",end='')
               else:
                    print(f" ",end='')
           print("X",end='')
           print()
        for j in range(self.size+2):
           print("X",end='')
        print()

def drawMaze(mazeArray,pen1,pen2,exit):
    # mazeArray = np.asarray(self.maze)
    for y in range(len(mazeArray)):
        for x in range(len(mazeArray[y])):
            char = mazeArray[y][x]

            screenX = -288 + (x * 24)
            screenY = 288 - (y * 24)
            if (y == 1 and x == 1) or (y == exit[0]+1 and x == exit[1]+1):
                pen2.goto(screenX,screenY)
                pen2.stamp()
            elif char == 'X':
                pen1.goto(screenX,screenY)
                pen1.stamp()
    pen1.ht()
    pen2.ht()

def dijkstra(mazeObject,destination_i,destination_j):

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
                    # unvisited.append(Node(i,j,math.inf))
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

def solveMaze(mazeObject,dmaze,pen,exitX,exitY,distance):
    pen.ht()
    print(pen.isvisible())
    for x in range(len(dmaze)):
        for y in range(len(dmaze)):
            if dmaze[x][y]:
                dmaze[x][y].visited = False
    currentNode = (exitX,exitY)
    while currentNode != (0,0):
        x = currentNode[0]
        y = currentNode[1]
        for neighbor in mazeObject.getNeighbors(x,y):
            cell = dmaze[neighbor[0]][neighbor[1]]
            if not cell.visited:
                if cell.distance < distance:
                    currentNode = neighbor
                    distance = cell.distance
                    cell.visited = True
        screenX = -288 + ((currentNode[1] + 1) * 24)
        screenY = 288 - ((currentNode[0] + 1) * 24)
        pen.goto(screenX,screenY)
        pen.stamp()   
    
if __name__ == "__main__":
    g = Maze(25)
    pen = Pen()
    greenPen = GreenPen()
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.setup(800,800)

    mazeArray = g.drawMaze()
    print(g.exit)
    drawMaze(mazeArray,pen,greenPen,g.exit)
    turtle.ht()
    ts = turtle.getscreen()
    # while True:
    #     pass  
    ps = ts.getcanvas().postscript(colormode='color')
    out = io.BytesIO()
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('preMaze.png',format="PNG")

    distance, dmaze = dijkstra(g,g.exit[0],g.exit[1])
    solveMaze(g,dmaze,RedPen(),g.exit[0],g.exit[1],distance)

    ts = turtle.getscreen()

    ps = ts.getcanvas().postscript(colormode='color')
    out = io.BytesIO()
    img = Image.open(io.BytesIO(ps.encode('utf-8')))

    img.save('postMaze.png',format="PNG")
    while True:
        pass