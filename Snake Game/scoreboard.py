from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT_SIZE = 24
FONT_STYLE = "normal"
FONT = ("Ariel", FONT_SIZE, FONT_STYLE)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.score = 0
        self.high_score = self.read_high_score()
        self.goto(0, 260)
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def read_high_score():
        with open("high_score.txt") as file:
            return int(file.read())

    def write_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(f"{self.score}")
