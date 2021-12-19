# Snake game
## Roadmap
This game must be constructed with 3 classes: Snake, Food and Scoreboard.

- [x] Create a snake body
- [x] Move the snake
- [x] Converts all we have until now into OOP
- [x] Control the snake
- [x] Detect collision with food
- [X] Create a scoreboard
- [x] Detect collision with wall
- [x] Detect collision with tail

### Roadmap development
#### Detect collision with food
Create the Food class and the collision detection on main:
`food.py`
```python
import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

```

`main.py`
```python
import time
from turtle import  Screen
from snake import Snake
from food import Food

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

```

#### Create a scoreoard
`scoreboard.py`
```python
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

```

`main.py`
```python
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

```

#### Detect collision with wall
Add a new method on `scoreboard.py`:
```python
def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

```

Add the validation on `main.py`
```python
# Detect food colision
if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()

# Detect wall colision
if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
    or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    is_game_on = False
    scoreboard.game_over()
```

#### Detect collision with tail
On `snake.py` we modify `create_snake` method and add another two methods:
```python
def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

def add_segment(self, position):
    new_tail = Turtle(shape="square")
    new_tail.color("white")
    new_tail.penup()
    new_tail.goto(position)   

    self.body.append(new_tail)

def extend(self):
    self.add_segment(self.body[-1])
```

On `main.py` we add the collision tail validation:
```python
# Detect wall colision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect colision with tail (if head collides with any segment in the tail)
    for segment in snake.body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
```

## Class inheritance concepts
In inheritance, the child class inherits all the properties and methods of the parent class.

How to set inheritance:

```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__() # Here we call the parent class constructor so all the attributes 
                           # and methods are inherited and available to the child class
    def swim(self): # This is a new method that is only available to the Fish class
        print("The fish is swimming")

    def breathe(self):
        super().breathe() # Here we call the parent class method
        print("The fish is breathing with gills") # Here we add extra functionality to the breathe  method inherited 
                                                  # from the parent class. So this breathe method has all the functionality 
                                                  # of the parent class plus the extra functionality of the child class

```

