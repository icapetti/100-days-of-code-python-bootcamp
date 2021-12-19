# Snake game
## Roadmap
This game must be constructed with 3 classes: Snake, Food and Scoreboard.

- [x] Create a snake body
- [x] Move the snake
- [x] Converts all we have until now into OOP
- [x] Control the snake
- [ ] Detect collision with food
- [ ] Create a scoreboard
- [ ] Detect collision with wall
- [ ] Detect collision with tail

### Roadmap development
#### Create a snake body
This code creates our snake which is a list of Turtle objects in square shape.
```python
from turtle import Turtle, Screen

def start_screen() -> Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    return screen

def start_snake() -> list:
    snake = []
    starting_tails_position = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_tails_position:
        new_tail = Turtle(shape="square")
        new_tail.color("white")
        new_tail.penup()
        new_tail.goto(position)   

        snake.append(new_tail)

    return snake 

screen = start_screen()
snake = start_snake()

```

#### Move the snake
This code allows our snake start to move. 
```python
import time
from turtle import Turtle, Screen

def start_screen() -> Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # Turns off the screen updates

    return screen

def start_snake() -> list:
    snake = []
    starting_tails_position = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_tails_position:
        new_tail = Turtle(shape="square")
        new_tail.color("white")
        new_tail.penup()
        new_tail.goto(position)   

        snake.append(new_tail)

    return snake 

screen = start_screen()
snake = start_snake()
snake_head = 0

is_game_on = True
while is_game_on:
    screen.update() # Shows modifies on the screen
    time.sleep(0.1) # Sleeps for 0.1 seconds

    start, stop, step = len(snake) -1, 0, -1
    for index in range(start, stop, step):
        new_x = snake[index -1].xcor()
        new_y = snake[index -1].ycor()
        snake[index].goto(new_x, new_y)
    snake[snake_head].forward(20)
```

#### Converts all we have until now into OOP
`main.py`
```python
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

is_game_on = True
while is_game_on:
    screen.update() # Shows modifies on the screen
    time.sleep(0.1) # Sleeps for 0.1 seconds

    snake.move()
```

`snake.py`
```python
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
HEAD = 0
DISTANCE = 20

class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            new_tail = Turtle(shape="square")
            new_tail.color("white")
            new_tail.penup()
            new_tail.goto(position)   

            self.body.append(new_tail)

    def move(self):
        start, stop, step = len(self.body) -1, 0, -1
        for index in range(start, stop, step):
            new_x = self.body[index -1].xcor()
            new_y = self.body[index -1].ycor()
            self.body[index].goto(new_x, new_y)
            
        self.body[HEAD].forward(DISTANCE)
```

#### Control the snake
Here we build 4 methods on snake class: up, down, left, right.
On the `main.py` we create a listener for keyboard events.

An important thing here: it's not allowed in the snake game to go backwards. We have to handle this.

`main.py`
```python
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

```

`snake.py`
```python
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
HEAD = 0
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            new_tail = Turtle(shape="square")
            new_tail.color("white")
            new_tail.penup()
            new_tail.goto(position)   

            self.body.append(new_tail)

    def move(self):
        start, stop, step = len(self.body) -1, 0, -1
        for index in range(start, stop, step):
            new_x = self.body[index -1].xcor()
            new_y = self.body[index -1].ycor()
            self.body[index].goto(new_x, new_y)
            
        self.body[HEAD].forward(DISTANCE)

    def up(self):
        if self.body[HEAD].heading() != DOWN: # Here we put a lock to not allow the backward
            self.body[HEAD].setheading(UP)

    def down(self):
        if self.body[HEAD].heading() != UP:
            self.body[HEAD].setheading(DOWN)

    def left(self):
        if self.body[HEAD].heading() != RIGHT:
            self.body[HEAD].setheading(LEFT)

    def right(self):
        if self.body[HEAD].heading() != LEFT:
            self.body[HEAD].setheading(RIGHT)

```

