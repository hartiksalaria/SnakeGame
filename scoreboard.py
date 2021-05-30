from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 350)
        self.color("white")
        self.write(f"Score : {self.score}", font=("Arial", 40, "normal"), align="center")

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", font=("Arial", 40, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f" GAME OVER ", font=("Arial", 40, "normal"), align="center")