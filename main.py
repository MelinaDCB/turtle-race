import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet !", prompt="Which turtle will win the race ? Enter a color : ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.pencolor("lightblue")
tim.pensize(25)
tim.goto(230, 200)
tim.right(90)
tim.pendown()
tim.forward(400)

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won ! the {winning_turtle} turtle is the winner !")
            else:
                print(f"You've lost ! the {winning_turtle} turtle is the winner !")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
