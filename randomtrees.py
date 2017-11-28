from graphics import *
import random
x = 0
y = 0
height = 0
numberoftrees = 0

def main():
    global center, x, y, height
    win = GraphWin("Tree Drawing", 800, 1000)
    numberoftrees = eval(input("How many trees would you like to see?"))
    win.setCoords(0,1000,800,0)
    win.setBackground(color_rgb(0,104,204))
    ground(win)
    for g in range (numberoftrees):
        x = random.randrange(50,751)
        y = random.randrange(820,950)
        height = random.randrange(125, 351)
        trunk(win)
        center = Point(x - 25, y - (height + 50))
        bushes(win)
        center = Point(x + 25, y - (height + 50))
        bushes(win)
        center = Point(x + 50, y - height)
        bushes(win)
        center = Point(x - 50, y - height)
        bushes(win)
        center = Point(x, y - height)
        bushes(win)
    input("Press Enter to Quit")


def ground(win):
    rect = Rectangle(Point(0,800), Point(800,1000))
    rect.draw(win)
    rect.setFill('green')
    lines = []
    for i in range (20000):
        randomgreen = random.randrange(50,150)
        startingpointgrassx = random.randrange (0,800)
        startingpointgrassy = random.randrange (800,1000)
        line = Line(Point(startingpointgrassx,startingpointgrassy), Point(startingpointgrassx, startingpointgrassy + 5))
        line.setOutline(color_rgb(0, randomgreen,0))
        lines.append(line)
    for l in lines:
        l.draw(win)


def trunk (win):
    rect2 = Rectangle(Point(x - 25, y - height), Point(x + 25, y))
    rect2.draw(win)
    rect2.setFill(color_rgb(102,51,0))


def bushes(win):
    circ = Circle(center, 50)
    circ.draw(win)
    circ.setFill(color_rgb(0,60,0))

main()
