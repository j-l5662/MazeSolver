import sys
import random
import enum 
import numpy as np 
import time
import math
import os
import io
import dijkstra as d


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
        self.maze[x,y] = 0
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
                # Make a passage in the maze
                self.maze[x,y] = 0
                # Check the cell neighbors
                self.addNeighbors(x-1,y,visited)
                self.addNeighbors(x+1,y,visited)
                self.addNeighbors(x,y+1,visited)
                self.addNeighbors(x,y-1,visited)
            visited.remove(cell)
        i = self.size - 1
        checkMaze = np.asarray(self.maze)
        # Set the exit of the maze as the right most bottom node that is a passage
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
       

    def drawMaze(self):
        maze = np.asarray(self.maze)
        testMaze = []
        testMaze.append('X' * (self.size+2))
        for i in range(self.size):
           str = 'X'
           for j in range(self.size):
               if maze[i,j] != 0:
                   str = str + 'X'
               else:
                   str = str + ' '
           str = str + 'X'
           testMaze.append(str)
        testMaze.append('X' * (self.size+2))

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

            screenX = -300 + (x * 24)
            screenY = 300 - (y * 24)
            if (y == 1 and x == 1) or (y == exit[0]+1 and x == exit[1]+1):
                pen2.goto(screenX,screenY)
                pen2.stamp()
            elif char == 'X':
                pen1.goto(screenX,screenY)
                pen1.stamp()

def solveMaze(mazeObject,dmaze,pen,exitX,exitY,distance):
    pen.ht()
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
        screenX = -300 + ((currentNode[1] + 1) * 24)
        screenY = 300 - ((currentNode[0] + 1) * 24)
        pen.goto(screenX,screenY)
        pen.stamp()   
    
if __name__ == "__main__":
    # g = Maze(25)
    # blackPen = Pen()
    # greenPen = Pen()
    # redPen = Pen()

    # blackPen.color("black")
    # greenPen.color("green")
    # redPen.color("red")
    # redPen.ht()
    # wn = turtle.Screen()
    # wn.bgcolor("white")
    # wn.setup(800,800)

    # mazeArray = g.drawMaze()

    # drawMaze(mazeArray,blackPen,greenPen,g.exit)
    

    distance, dmaze = d.dijkstra(g,g.exit[0],g.exit[1])
    solveMaze(g,dmaze,redPen,g.exit[0],g.exit[1],distance)

    ts = turtle.getscreen()
    ps = ts.getcanvas().postscript(colormode='color')
    out = io.BytesIO()
    img = Image.open(io.BytesIO(ps.encode('utf-8')))

    img.save('postMaze.png',format="PNG")
    while True:
        pass