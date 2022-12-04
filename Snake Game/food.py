from turtle import Turtle
from random import randint

SHAPE = "circle"
COLOR = "blue"
RESIZE = 0.5
SPEED = "fastest"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=RESIZE, stretch_len=RESIZE)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        self.goto(randint(-14, 14)*20, randint(-14, 14)*20)
