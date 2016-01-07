import turtle

def drawTriangle(myTurtle):
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.right(240)
def draw4Triangles(myTurtle):
	c = 0
	while c < 4:
		drawTriangle(shawn)
		myTurtle.penup()
		myTurtle.forward(15)
		myTurtle.pendown()
		c = c + 1
	myTurtle.penup()
	myTurtle.backward(60)
	myTurtle.pendown()
def drawRows(myTurtle):
	c = 0
	while c < 3:
		draw4Triangles(shawn)
		myTurtle.left(30)
		c = c + 1
def drawOtherRows(myTurtle):
	drawRows(shawn)
	myTurtle.right(260)
	drawRows(shawn)	
shawn = turtle.Turtle()
drawOtherRows(shawn)
turtle.exitonclick()
