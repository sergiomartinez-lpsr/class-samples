import turtle
def drawTee(myTurtle):
	myTurtle.forward(100)
	myTurtle.backward(25)
	myTurtle.right(90)
	myTurtle.forward(25)
	myTurtle.backward(50)
	myTurtle.forward(25)
	myTurtle.right(90)
	myTurtle.forward(75)
	myTurtle.left(90)
def drawFourTees(myTurtle):
	c = 0
	while c < 4:
		drawTee(shawn)
		c = c + 1
# make your turtle down here and pass it to the appropiate places
shawn = turtle.Turtle()
drawFourTees(shawn)
turtle.exitonclick()
