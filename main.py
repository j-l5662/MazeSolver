from maze import Maze, drawMaze, solveMaze
import argparse
import dijkstra as d
from pen import Pen
import turtle
import io
from PIL import Image 

def saveScreen(imageName):
    ts = turtle.getscreen() 
    ps = ts.getcanvas().postscript(colormode='color')
    out = io.BytesIO()
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save(imageName,format="PNG")

if __name__ == "__main__":
    maze = Maze(25)

    blackPen = Pen()
    greenPen = Pen()
    redPen = Pen()

    blackPen.color("black")
    greenPen.color("green")
    redPen.color("red")
    redPen.ht()
    wn = turtle.Screen()
    wn.bgcolor("gray")
    wn.setup(800,800)

    mazeArray = maze.drawMaze()

    drawMaze(mazeArray,blackPen,greenPen,maze.exit)

    turtle.ht()
    saveScreen("preMaze.png")

    distance, dmaze = d.dijkstra(maze,maze.exit[0],maze.exit[1],verbose=True)
    saveScreen("preMaze_d.png")
    solveMaze(maze,dmaze,redPen,maze.exit[0],maze.exit[1],distance)
    saveScreen("postMaze.png")
    while True:
        pass
    