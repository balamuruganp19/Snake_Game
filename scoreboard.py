from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.write(f"Score:{self.score}", align="center", font=("arial", 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("arial", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("arial", 18, "bold"))