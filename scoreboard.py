from turtle import Turtle

FONT = ("Arial", 18, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.score_board()
        # self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.score_board()
