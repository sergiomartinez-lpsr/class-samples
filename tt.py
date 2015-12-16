
import turtle
t = turtle.Turtle()
t.color("blue")
lines = 0
while lines < 8:
	t.right(45)
	t.forward(20)
	t.right(90)
	t.forward(80)
	t.left(135)
	t.forward(80)
	t.right(45)
	lines = lines + 1 
turtle.exitonclick()
