import time
from turtle import  Screen
from snake import Snake

def start_screen() -> Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # Turns off the screen updates

    return screen

screen = start_screen()
snake = Snake()

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








screen.exitonclick()
