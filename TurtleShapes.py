import turtle

turtle.speed(10)
for s in range (5):

	turtle.forward(500)
	turtle.left(216)
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
turtle.begin_fill()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(45)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(45)
turtle.forward(200)
turtle.end_fill()



turtle.mainloop()


