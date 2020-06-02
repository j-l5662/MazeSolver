# Python Maze Solver

A randomized maze generator with the minimal path solution that is implemented using both Dijkstra or A* algorithm.

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Future Work](#Future\sImplementations)

## Background

This is a side project to implement popular shortest path algorithms(e.g. [Dijkstra](#https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm) and [A* Search](#https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode)). The code base is written in Python and it leverages libraries such as  [Turtle](#https://docs.python.org/3.3/library/turtle.html?highlight=turtle) and [PIL](#https://pillow.readthedocs.io/en/3.0.x/handbook/overview.html) to generate and save the images.

While other projects implemented a user defined maze, I developed a randomized maze generation to create mazes to test the algorithm.  

## Install

First install the necessary python libraries.

```pip install requirements.txt```

For Macs install ghostscript to convert the turtle canvas from a postscript file into a png file.

```brew install ghostscript```

## Usage

```python main.py```

Dijkstra Implementation

![](res/dijkstra.gif)


A* Implementation

![](res/astar.gif)


## Future Implementations

 - Implement a drawing GUI to allow users to draw their own mazes or utilize a randomized maze.
