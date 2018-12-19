import turtle


turtle.pensize(10)
for i in range(5):
	turtle.hideturtle()
	turtle.forward(100)
	turtle.left(216)
turtle.showturtle()
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor('black')
for i in range(3):
	turtle.forward(50)
	turtle.left(90)
turtle.right(45)
turtle.forward(35.35)
turtle.left(90)
turtle.forward(35.5)
turtle.end_fill()
turtle.reset()
turtle.addshape("flappy.gif")
turtle.shape("flappy.gif")
def thing():
	turtle.speed(0)
	turtle.forward(200)
	turtle.right(30)
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(60)
	turtle.penup()
	turtle.setpos(0,0)
	turtle.pendown()
	turtle.right(1)
for i in range(360):
	thing()