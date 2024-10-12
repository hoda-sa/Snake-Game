from turtle import Turtle
FONT = ('Calibri', 15, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.goto(x=0, y= 280)
        self.color("white")
        self.write(f"Score : {self.score} High Score = {self.high_score}", False, align= ALIGNMENT, font= FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.hideturtle()
    #     self.color("white")
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)