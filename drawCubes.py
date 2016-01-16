import turtle
# makes first rhombus with the color of gold
def makeRhombus(myTurtle):
	myTurtle.fillcolor("GoldenRod")
# begins filling in rhombus
	myTurtle.begin_fill()
	myTurtle.left(90)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.right(120)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.end_fill()
# makes another rhombus, this time grey 
def makeAnotherOne(myTurtle):
	myTurtle.fillcolor("DimGray")
# begins filling in
        myTurtle.begin_fill()
	myTurtle.right(60)
        myTurtle.forward(20)
        myTurtle.right(60)
        myTurtle.forward(20)
        myTurtle.right(120)
        myTurtle.forward(20)
        myTurtle.right(60)
        myTurtle.forward(20)
        myTurtle.end_fill()
# makes third rhombus now light blue
def makeLastRhombus(myTurtle):
	myTurtle.fillcolor("LightBlue")
# begins filling in
	myTurtle.begin_fill()
	myTurtle.left(30)
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.left(60)
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.end_fill()
# makes cube using all rhombuses made before
def makeCube(myTurtle):
	makeRhombus(shawn)
	makeAnotherOne(shawn)
	myTurtle.backward(20)
	myTurtle.right(270)
	makeLastRhombus(shawn)
# makes anothe cubes using the function before
def makeAnotherCube(myTurtle):
	makeCube(shawn)
# lifts pen up in order to make the other cube without drawing anything
	myTurtle.penup()
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.left(30)
# puts pen down
	myTurtle.pendown()
# makes rows of cubes
def makeRow(myTurtle):
	c = 0 
	while c < 5:
		makeAnotherCube(shawn)
# adds one so that it's not an infinite loop
		c = c + 1
# puts the cubes in position
def makeIntoPosition(myTurtle):
	myTurtle.penup()
	myTurtle.backward(175)
	myTurtle.left(90)
	myTurtle.forward(40)
	myTurtle.right(120)
	myTurtle.forward(20)
	myTurtle.left(30)
	myTurtle.pendown()
# creates shawn as a turtle
shawn = turtle.Turtle()
# adds speed so that shawn can go faster
shawn.speed(10)
# makes all rows using the other functions
def makeMoreRows(shawn):
	c = 0 
	while c < 4:
		makeRow(shawn)
		makeIntoPosition(shawn)
		c = c + 1
makeMoreRows(shawn)
turtle.exitonclick()
