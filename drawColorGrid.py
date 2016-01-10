import turtle
def drawRedSquare(myTurtle):
	myTurtle.color("red")	
	c = 0 
	while c < 4:
		myTurtle.forward(30)
		myTurtle.right(90)
		c = c + 1
def drawBlueSquare(myTurtle):
	myTurtle.color("blue")
	c = 0 
	while c < 4:
		myTurtle.forward(30)
		myTurtle.right(90)
		c = c + 1
def drawGreenSquare(myTurtle):
	myTurtle.color("green")
	c = 0 
	while c < 4:
		myTurtle.forward(30)
		myTurtle.right(90)
		c = c + 1
def drawYellowSquare(myTurtle):
	myTurtle.color("yellow")
	c = 0 
	while c < 4:
		myTurtle.forward(30)
		myTurtle.right(90)
		c = c + 1 
def draw4Squares(myTurtle):
	drawRedSquare(shawn)
	myTurtle.left(90)
	drawBlueSquare(shawn)
	myTurtle.left(90)
	drawGreenSquare(shawn)
	myTurtle.left(90)
	drawYellowSquare(shawn)	
def drawOtherSquares(myTurtle):
	draw4Squares(shawn)
	myTurtle.penup()
	myTurtle.forward(30)
	myTurtle.left(90)
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	draw4Squares(shawn)
def draw1More(myTurtle):
	drawOtherSquares(shawn)
	myTurtle.penup()
	myTurtle.left(90)
	myTurtle.forward(30)
	myTurtle.left(90)
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	draw4Squares(shawn)
def drawAnotherOne(myTurtle):
	draw1More(shawn)
	myTurtle.penup()
	myTurtle.left(90)
	myTurtle.forward(30)
	myTurtle.left(90)
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	draw4Squares(shawn)
def drawLastSquare(myTurtle):
	drawAnotherOne(shawn)
	myTurtle.penup()
	myTurtle.left(90)
	myTurtle.forward(30)
	myTurtle.left(90)
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	draw4Squares(shawn)
shawn = turtle.Turtle()
drawLastSquare(shawn)
turtle.exitonclick()
