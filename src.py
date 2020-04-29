import sys
import random
import enum 
import numpy as np 
import time

class Cell():
    def __init__(self,x,y,weight):
        self.x = x
        self.y = y
        self.weight = weight

    
class Graph:
    def __init__(self,graphSize):

        self.size = graphSize
        self.maze = np.random.randint(1,100,size=(graphSize,graphSize))
        

    def generateMaze(self):
        visited = []
        x = 0
        y = 0
        self.makePassage(x,y)
        self.addNeighbors(x-1,y,visited)
        self.addNeighbors(x+1,y,visited)
        self.addNeighbors(x,y+1,visited)
        self.addNeighbors(x,y-1,visited)
        # while len(visited) < self.size ** 2:
        #     print(list(visited)[0])
        #     for i in list(visited):
        #         minNeighbor = min(self.checkNeighbor(i[0]+1,i[1]),self.checkNeighbor(i[0]-1,i[1]),self.checkNeighbor(i[0],i[1]+1),\
        #         self.checkNeighbor(i[0],i[1]-1))

        #         print(minNeighbor)
        #     return
        # https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm
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
            # self.printMaze()
            # print(len(visited))
            # if count == 10:
            #     break
            # print()
            # time.sleep(.5)
        # self.printMaze()
        
    
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

    # def checkNeighbor(self,x,y):
    #     if x >= 0 and x < self.size and y >= 0 and y < self.size:
    #         return self.maze[x,y]
    #     elif self.maze[x,y] == 0:
    #         return 100
    #     else:
    #         return 100
            
    def makePassage(self,x,y):
        self.maze[x,y] = 0


    def printMaze(self):
        maze = np.asarray(self.maze)
        for i in range(g.size):
           for j in range(g.size):
               if maze[i,j] != 0:
                   print("1",end='')
               else:
                    print(f"{maze[i,j]}",end='')
           print()

if __name__ == "__main__":
    g = Graph(5)
    # g.printMaze()    
    g.generateMaze()
    # print(g.maze[0,0])
    # print("Hello")