from turtle import Turtle
from gameconst import SCREEN_HEIGHT, ALIGNMENT, FONT


def check_high_score():
    with open("highscore.txt", mode="r") as file:
        return file.read()
    pass


def write_high_score(score):
    with open("highscore.txt", mode="w") as file:
        return file.write(str(score))
    pass


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.cur_score = 0
        self.high_score = int(check_high_score())
        self.hideturtle()
        self.setposition(0, int(SCREEN_HEIGHT / 2 - 30))
        self.color("white")
        self.update_score()
        pass

    def score_one(self):
        self.cur_score += 1
        self.update_score()
        pass

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.cur_score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        pass

    def update_snake(self):
        if self.cur_score > self.high_score:
            write_high_score(self.cur_score)
            self.high_score = self.cur_score
        self.cur_score = 0
        self.update_score()
        pass

# scoreboard.clear()
