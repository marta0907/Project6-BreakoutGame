from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 00
        self.life = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 40, "normal"))
        self.goto(150, 250)
        self.write(f"Lives: {self.life}", align="center", font=("Courier", 40, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def loosing_life(self):
        self.life -= 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
    
    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=("Courier", 40, "normal"))