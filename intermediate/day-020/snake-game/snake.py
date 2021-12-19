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
