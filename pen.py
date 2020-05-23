import turtle


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

    def draw(self, x, y, coordinate):
        screenX = -coordinate + ((y + 1) * 24)
        screenY = coordinate - ((x + 1) * 24)
        self.goto(screenX,screenY)
        self.stamp()