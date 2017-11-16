from graphics import *
center = 0

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

