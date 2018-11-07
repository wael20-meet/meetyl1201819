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


turtle.mainloop()