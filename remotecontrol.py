import turtle
from Tkinter import *
def square(myTurtle, side):
	sides = 0
	while sides < 4:
		myTurtle.forward(side)
		myTurtle.right(90)
		sides = sides + 1
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='pen up', command=lambda: shawn.penup())
pendown = Button(frame, text='pen down', command=lambda: shawn.pendown())
backward = Button(frame, text='backward', command=lambda:shawn.backward(50))
square3 = Button(frame, text='square', command=lambda:square(shawn,50))
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
backward.pack(side=LEFT)
square3.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
