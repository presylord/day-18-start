from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed("fastest")
Screen().colormode(255)

for _ in range(0, 361, 5):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r, g, b)

    turtle.circle(100)
    turtle.setheading(_)




















screen = Screen()
screen.exitonclick()