import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self) -> None:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
