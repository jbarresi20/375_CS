from graphics import *
import random
center = 0
startingpointx = random.randrange

def main():
    global center
    win = GraphWin("Tree Drawing", 200, 400)
    win.setBackground(color_rgb(0,104,204))
    ground(win)
    trunk(win)
    center = Point(50,125)
    bushes(win)
    center = Point(75,75)
    bushes(win)
    center = Point(125,75)
    bushes(win)
    center = Point(150,125)
    bushes(win)
    center = Point(50,125)
    bushes(win)
    center = Point(100,125)
    bushes(win)
 # Here's where I will draw the face!

    input("Press Enter to Quit")

def ground(win):
    rect = Rectangle(Point(0,350), Point(200,400))
    rect.draw(win)
    rect.setFill('green')
    for i in range (5000):
        randomgreen = random.randrange(50,150)
        startingpointgrassx = random.randrange (0,200)
        startingpointgrassy = random.randrange (350,400)
        line = Line(Point(startingpointgrassx,startingpointgrassy), Point(startingpointgrassx, startingpointgrassy + 5))
        line.setOutline(color_rgb(0, randomgreen,0))
        line.draw(win)


def trunk (win):
    rect2 = Rectangle(Point(125,350), Point(75,125))
    rect2.draw(win)
    rect2.setFill(color_rgb(102,51,0))
def bushes(win):
    global center
    circ = Circle(center, 50)
    circ.draw(win)
    circ.setFill(color_rgb(0,60,0))


main()
