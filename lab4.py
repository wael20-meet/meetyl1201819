class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name =  name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! " + self.name + "is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color "+ self.favorite_color)
	def make_sound(self):
		print(self.sound)
		for i in range(3):
			print(self.sound)
cat = Animal("meow" , "kitty" ,"13","cheese" , "red")
cat.eat()
cat.description()
cat.make_sound()

class Person():
	def __init__(self,sound,name,age,food,color):
		self.sound = sound
		self.name = name 
		self.age = age 
		self.food = food 
		self.color = color
		def eat_food(self):
		print(self.name+" is eating "+self.food+" which is her favorite food")

