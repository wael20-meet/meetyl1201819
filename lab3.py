import turtle

for s in range (1):
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
for i in range(3):
	turtle.forward(50)
	turtle.left(90)
	turtle.right(45)
	turtle.forward(35.35)
	turtle.left(90)
	turtle.forward(35.5)
	turtle.end_fill()
	turtle.reset()
	turtle.addshape("khaled.gif")
	turtle.shape("khaled.gif")
<<<<<<< HEAD


turtle.mainloop()
=======
def peace():
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
	peace()
turtle.mainloop()

