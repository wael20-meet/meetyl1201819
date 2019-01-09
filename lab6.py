import turtle
from turtle import Turtle
import random
turtle.colormode(255)
class Rectangle(Turtle):
	def __init__ (self,x,y):
		Turtle.__init__(self)
		turtle.register_shape("rectangle",((0,0),(0,y),(x,y),(x,0),(0,0)))
		self.shape("rectangle")
	def random_color(self):
		r = random.randint(0,255)
		r1 = random.randint(0,255)
		r2 = random.randint(0,255)
		self.color([r,r1,r2])

<<<<<<< HEAD
		def random_color(self):
			R = randrange(0,257,10)
			G = randrange(0,257,10)
			B = randrange(0,257)
=======

# rect = Rectangle(75,100)
# rect.random_color();
class Square(Rectangle):
	def __init__ (self):
		Rectangle.__init__(self,50,50)
	
# Square = Square()
# Square.random_color()
>>>>>>> 807944e3676a9983e654fe841e381364de9edba7

class Hexagon(Turtle):
	def __init__(self, x):
		Turtle.__init__(self)
		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,2*x),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
		self.shape("Hexagon")
	def random_color(self):
		r = random.randint(0,255)
		r1 = random.randint(0,255)
		r2 = random.randint(0,255)
		self.color([r,r1,r2])

H = Hexagon(20)
H.random_color()

turtle.mainloop()
