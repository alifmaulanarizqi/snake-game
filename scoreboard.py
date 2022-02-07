from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def score_board(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 18, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
