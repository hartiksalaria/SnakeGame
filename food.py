import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("yellow")
        self.refresh()
        self.shapesize(0.5, 0.5)

    def refresh(self):
        self.goto(random.randint(-480, 480), random.randint(-380, 300))