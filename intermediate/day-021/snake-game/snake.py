from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
HEAD = 0
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]

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
        self.add_segment(self.body[-1].position())

    def move(self):
        start, stop, step = len(self.body) -1, 0, -1
        for index in range(start, stop, step):
            new_x = self.body[index -1].xcor()
            new_y = self.body[index -1].ycor()
            self.body[index].goto(new_x, new_y)
            
        self.body[HEAD].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # Here we put a lock to not allow the backward
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
