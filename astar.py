import io
from pen import Pen
from queue import PriorityQueue

class Node():
    def __init__(self,point,g,h,parent = None):
        self.point = point
        self.g = -1
        self.h = -1
        self.parent = parent

    def __lt__(self,ob2):
        return self.point < ob2.point



def manhattan_distance(x,y):
    return (abs(x[0]-y[0])) + (abs(x[1] - y[1]))
    
def aStar(mazeObject, start, end,verbose=False):
    if verbose:
        pen = Pen()
        pen.color("yellow")
    q = PriorityQueue()
    g_cost = 0
    h_cost = manhattan_distance(start,end)
    startNode = Node(start,g_cost,h_cost)
    f_cost = startNode.g + startNode.h 
    q.put((f_cost, startNode))

    closed = set()
    while not q.empty():
        checkNode = q.get()
        current_F = checkNode[0]
        node = checkNode[1]

        # g_cost = 1
        # h_cost = how far it is from the end node
        # f_cost = g_cost + h_cost
        if node.point == end:
            if verbose:
                pen2 = Pen()
                pen2.color("red")
                retracePath(node.parent,pen2)
            print("Retraced Path")
            return
        closed.add(node.point)

        if verbose and node.point != start:   
            pen.draw(node.point[0],node.point[1],300)
        for neighbor in mazeObject.getNeighbors(node.point[0],node.point[1]):
            if neighbor in closed:
                continue
            g_cost = node.g + 1
            h_cost = manhattan_distance(neighbor,end)
            f_cost = g_cost + h_cost
            # print(f"Test: {f_cost}")
            childNode = Node(neighbor,g_cost,h_cost,node)
            if f_cost < current_F or neighbor not in [element[1].point for element in q.queue]:
                if neighbor not in [element[1].point for element in q.queue]:
                    q.put((f_cost,childNode))
            
        
    return 0


def retracePath(node,pen):
    if node.parent == None:
        return

    pen.draw(node.point[0],node.point[1],300)
    return retracePath(node.parent,pen)