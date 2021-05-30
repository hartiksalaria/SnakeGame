from turtle import Turtle, Screen
import time

screen = Screen()
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD = 10


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for i in SNAKE_POSITIONS:
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(i)
            self.snake_body.append(t)

    def add_segment(self):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(t)

    def move(self):
        screen.tracer(0)
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].xcor(), self.snake_body[i - 1].ycor())
        self.snake_body[0].forward(FORWARD)
        time.sleep(0.05)
        screen.update()

    def right(self):
        if self.snake_body[0].heading() == 270:
            self.snake_body[0].left(90)
        else:
            self.snake_body[0].right(90)

    def left(self):
        if self.snake_body[0].heading() == 270:
            self.snake_body[0].right(90)
        else:
            self.snake_body[0].left(90)

    def up(self):
        if self.snake_body[0].heading() == 0:
            self.snake_body[0].left(90)
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].right(90)

    def down(self):
        if self.snake_body[0].heading() == 0:
            self.snake_body[0].right(90)
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].left(90)
