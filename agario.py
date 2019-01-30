
import time
import turtle
from turtle import *
import random
turtle.tracer(0)
turtle.hideturtle()
import math
import sys
colormode(255) 
turtle.setup(950,534)



class Ball(Turtle):
    def __init__(self, x, y, dx, dy, radius, color):
        Turtle.__init__(self)
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.shapesize(radius/10)
        self.shape("circle")

        r = random.randint (0,255)
        g = random.randint (0,255)
        b = random.randint (0,255)
        self.color((r,g,b))

    def move(self, screen_width, screen_height):
            currentx = self.xcor()
            currenty = self.ycor()
            newx = currentx + self.dx
            newy = currenty + self.dy
            right_side_ball = newx + self.radius
            left_side_ball = newx - self.radius
            top_side_ball = newy + self.radius
            bottom_side_ball = newy - self.radius
            self.goto (newx , newy)

            if right_side_ball >= screen_width:
                self.dx = -self.dx
            
            if left_side_ball <= -screen_width:
                self.dx = -self.dx
            
            if top_side_ball >= screen_height:
                self.dy = -self.dy

            if bottom_side_ball <= -screen_height:
                self.dy = -self.dy



score = 0

RUNNING = True
sleep = 0.01999
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT =turtle.getcanvas().winfo_height()//2

MY_BALL = Ball(0,0,30,20,30,"yellow")

NUMBER_OF_BALLS = 8
MINIMUM_BALL_RADIUS = 25
MAXIMUM_BALL_RADIUS = 40
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
    x = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
    y = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
    dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    if dx == 0:
        dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    if dy == 0:
        dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color = (random.random(), random.random(), random.random())
    ball = Ball(x, y, dx, dy, radius, color)

    BALLS.append (ball)


def move_all_balls():
    for cow in BALLS:
        cow.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
    ball_a_pos = ball_a.pos()
    ball_b_pos = ball_b.pos()   
    if ball_a == ball_b :
        return False

        
    ball_a.xcor()   
    ball_a.ycor()   
    ball_b.xcor()   
    ball_b.ycor()   

    DISTANCE_BETWEEN_CENTERS = ((ball_a.xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor())**2)**0.5

    if DISTANCE_BETWEEN_CENTERS+10 <= ball_a.radius + ball_b.radius:
        return True
    else:
        return False
       
       

def check_all_balls_collision():
    for ball_a in balls:
        for ball_b in balls:
            if check_collide(ball_a,ball_b) == True:
                radius1 = ball_a.r
                radius2 = ball_b.r
                random_x = random.randint(screen_random1_x,screen_random2_x)
                random_y = random.randint(screen_random1_y,screen_random2_y)
                random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                while random_dx == 0:
                    random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                while random_dy == 0:
                    random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                radius = random.randint(minimum_ball_radius,maximum_ball_radius)
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

                if radius1 > radius2:
                    ball_b.goto(random_x,random_y)
                    ball_b.dx = random_dx
                    ball_b.dy = random_dy
                    ball_b.r = radius
                    ball_b.shapesize(ball_b.r/10)
                    ball_b.color = color
                    ball_a.r += 0.5
                    ball_a.shapesize(ball_a.r/10)
                    
                elif radius1 < radius2:
                    ball_a.goto(random_x,random_y)
                    ball_a.dx = random_dx
                    ball_a.dy = random_dy
                    ball_a.r = radius
                    ball_a.shapesize(ball_a.r/10)
                    ball_a.color = color
                    ball_b.r += 0.5
                    ball_b.shapesize(ball_b.r/10)



                
def check_myball_collision():
    for i in BALLS:
        if collide(i,MY_BALL) == True:
            radius_i = i.radius
            radius_MY_BALL= MY_BALL.radius
            ball_a = MY_BALL
            ball_b = i
            if MY_BALL.radius <= i.radius:
                RUNNING = False
                turtle.goto(-200,0)
                turtle.color("red")
                turtle.write("GAME OVER  , YOU'RE A LOOOOOOOSER!!!!!!!", move=False, font=("Arial", 20, "bold"))
                time.sleep(10)
                sys.exit("Error message")


            else:
                X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
                Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
                X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                while X_axis_speed == 0:
                    X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                while Y_axis_speed  == 0:
                    Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                color = (r,g,b)

            
                ball_b.goto(X_coordinate, Y_coordinate)
                ball_b.dx = X_axis_speed 
                ball_b.dy = Y_axis_speed
                ball_b.shapesize(radius/10)
                ball_b.color(color)
                ball_a.radius = ball_a.radius+1 
                ball_a.shapesize(ball_a.radius/10)


    return True

def movearound(event):
    NEW_X_coordinate = event.x - SCREEN_WIDTH
    NEW_Y_coordinate = -(event.y - SCREEN_HEIGHT)
    MY_BALL.goto(NEW_X_coordinate, NEW_Y_coordinate)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



while RUNNING == True:
    if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 :
        SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2 
        SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
        move_all_balls()
   
    if check_myball_collision() == False:
        running = False
        turtle.goto(0,0)
        turtle.write("Game Over",align="center",font=("Arial", 50, "normal"))
        turtle.update()
        time.sleep(5)

     
    turtle.update()
    time.sleep(sleep)



    move_all_balls()
    check_myball_collision()

    

turtle.mainloop()