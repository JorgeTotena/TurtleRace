"""REQUIREMENTS:
-Once the screen is started, we will give the user a prompt: who will win the race? Enter a color:
-The turtles will have the colors of the rainbow
-Once the user inputs a color, the game will start and the turtles will be put right in the start
-Every turtle will move forward randomly until the end
-The turtle who gets first to the end of the screen will be the winner


"""
import random
import turtle
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = [-100, -60, -20, 20, 60, 100]
all_turtles = [] #these are all the turtles contain in the for loop


for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.teleport(x, y[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle) #this concept is really important about iteration and adding elements to a list

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0,10) #creates a random distance to move the turtles
        turtle.forward(rand_distance) #moves forward by a random distance
        if turtle.xcor() >= 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won", winning_color, "turtle is the winner")
            else:
                print("You've lost", winning_color, "turtle is the winner")






"""for i in colors:
    turtle1 = Turtle(shape="turtle")
    turtle1.teleport(x,y+50)
    turtle2 = Turtle(shape="turtle")
    turtle2.teleport(x, y + 100) """


screen.exitonclick()