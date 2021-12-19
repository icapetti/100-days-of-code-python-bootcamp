import random

from turtle import Turtle, Screen

def create_turtles():
    turtles = []
    x = -250
    y = -100
    for t in TURTLES_COLORS:
        turtle = Turtle(shape='turtle')
        turtle.color(t)
        turtle.penup()
        turtle.speed(0)
        turtle.goto(x, y)

        turtles.append(turtle)
        y += 30
    
    return turtles

TURTLES_COLORS = ['green', 'yellow', 'red', 'blue', 'violet', 'orange', 'indigo']
is_race_on = False

screen = Screen()
screen.setup(width=600, height=400)
turtles = create_turtles()

user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Which turtle will win the race? Enter rainbow color: ").lower()

is_race_on = True if user_bet else False

random.shuffle(turtles)
while is_race_on:
    for t in turtles:
        if t.xcor() > 200:
            winner = t.color()[0]
            is_race_on = False
        t.speed(random.randint(0, 10))
        t.forward(random.randint(0, 10))

if user_bet in winner:
    print("Congratulatons! Your bet was correct!")
else:
    print("Sorry, you lost!")

print(f"The winner was {winner}")
screen.exitonclick()
