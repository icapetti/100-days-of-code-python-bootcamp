import time
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def start_screen() -> Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # Turns off the screen updates

    return screen

screen = start_screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() # Listen for keyboard input
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

is_game_on = True
while is_game_on:
    screen.update() # Shows modifies on the screen
    time.sleep(0.1) # Sleeps for 0.1 seconds
    snake.move()

    # Detect food colision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect wall colision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect colision with tail (if head collides with any segment in the tail)
    for segment in snake.body[1:]: # Using slice because the segmant 0 is the head
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
