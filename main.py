from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.pensize(10)
turtle.speed("fast")
Screen().colormode(255)

angle = [0, 90, 180, 270]

for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r, g, b)
    r_angle = random.choice(angle)
    turtle.setheading(r_angle)
    turtle.forward(50)




















screen = Screen()
screen.exitonclick()