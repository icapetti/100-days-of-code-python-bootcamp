import colorgram
from turtle import Turtle, Screen
from random import choice

def get_colors_from_image(image: str) -> list:
    colors = colorgram.extract('painting_input.jpg', 30)
    return [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]

def init_pos(turtle: Turtle) -> None:
    turtle.hideturtle()
    turtle.speed(0)
    turtle.setx(x)
    turtle.sety(y)
    turtle.speed(1)
    turtle.showturtle()

jimmy = Turtle()
screen = Screen()

jimmy.speed(1)
jimmy.penup()
screen.colormode(255)
screen.setup(width=1.0, height=1.0)

rgb_colors = get_colors_from_image('painting_input.jpg')

x = -250
y = -250
init_pos(jimmy)

for _ in range(10):
    for _ in range(10):
        jimmy.dot(20, choice(rgb_colors))
        jimmy.forward(50)

    y += 50
    jimmy.speed(0)
    jimmy.setposition(x=x, y=y)
    jimmy.speed(1)

screen.exitonclick()
