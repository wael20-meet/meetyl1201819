# #probrlem1
# import Tkinter as Tk
# import tkSimpleDialog as  simpledialog
# #Then when ever you want to ask the user for input use this code
# greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=Tk.Tk().withdraw())
# if greeting in ["Arrr!"]:
# 	print("Go away, pirate.")
# else:
# 	print("Greetings, hater of pirates!")


# #problem2

# import Tkinter as tk
# import tkSimpleDialog as simpledialog

# year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

# if year <= 1900:
#     print ("Woah, that's the past!")
# if year > 1900 & year < 2020:
#     print ("That's totally the present!")
# else:
#     print ("Far out, that's the future!!")


# #problem3

# class Person(object):
#   def __init__(self, first_name, last_name):
#     self.first = fname
#     self.last = lname
#   def speak(self):
#   	print("My name is" + self.fname + " " + self.lname)

# 	me = Person("Brandon", "Walsh")
# 	you = Person("Ethan", "Reed")

# 	me.speak()
# 	you.speak()

# #problem4

# import Tkinter as Tk
# import tkSimpleDialog as simpledialog
# # Calculating Grades (ok, let me think about this one)

# # Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# # Average	Grade
# # 90+	A
# # 80-89	B
# # 70-79	C
# # 60-69	D
# # 0-59	F

# # Exams: 89, 90, 90
# # Average: 90
# # Grade: A
# # Student is passing.

# # Exams: 50, 51, 0
# # Average: 33
# # Grade: F
# # Student iis failing.

# exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=Tk.Tk().withdraw()))

# exam_two = int(simpledialog.askstring("Input"," exam grade two: ", parent=Tk.Tk().withdraw()))

# exam_three = int(simpledialog.askstring("Input"," exam grade three: ", parent=Tk.Tk().withdraw()))

# grades = [exam_one , exam_two , exam_three]
# sum = 0
# for grade in grades :
#  	sum = sum + grade

# avg = sum / len(grades)

# if avg >= 90:
#     letter_grade = "A
# elif avg >= 80 and avg < 90:
#     letter_grade = "B"
# elif avg > 69 and avg < 80:
#     letter_grade = "C"
# elif avg <= 69 and avg >= 65:
#     letter_grade = "D"
# else:
#     letter_grade = "F"


# if lettergrade is "F":
#     print ("Student is failing.")
# else:
#     print ("Student is passing.")

# #problem5

# class Person():
#    def __init__(self, name, favorite_food ,age, color):
#        self.name = name
#        self.fav_food = favorite_food
#        self.age = age
#        self.color = color	

#    def define_color(self, color="Red"):
#        self.color = color

#    def print_info(self):
#        print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
#        print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


# a = Person("Britney", "Pizza", 16, "black")
# a.define_color("Black")
# a.print_info()

# b = Person("Jake", "hamburger" , 15, "yellow")
# b.print_info()


# #problem6

# class Bear():
# 	def __init__(self, name):
# 		self.name = name
		
# 	def say_hi(self):

# 		print("A new bear created. Its name is: " + self.name)
# 		print("Hi! I'm a bear my name is" + self.name)
		
# my_bear = Bear("Danny")
# print(my_bear.say_hi())


# #problem7
 
# balloons = 5
# name = "Ron"
# color = "Yellow"
# print("This is a tale about " , balloons , "balloons. The first kid is " , name ,  "who got a " , color , "balloon")


# #problem8

# class Cake():
# 	def __init__(self, flavor):
# 		self.cake_flavor = flavor

# 	def eat(self):
# 		print('Yummy!!! Eating a', self.cake_flavor, 'cake :')

# cake0 = Cake("chocolate")
# cake0.eat()
# # what I want to be printed: Yummy!!! Eating a chocolate cake :)


# #problem9

class Cat():
def__init__(self, name):
self.name = name
self.age = 0 
	def birthday(self):
		self.age += 1
		if self.age >= 100
			print(“Dong dong, the cat is dead!”)
		else:
			print(self.name, ‘hasing its’, self.age, ‘birthday!’)

my_cat = Cat(“Salem”)
my_cat.birthday(8)
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)




