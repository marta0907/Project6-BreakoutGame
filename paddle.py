from turtle import Turtle
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.move_speed = 15
        self.moving_right = False
        self.moving_left = False

    def go_right(self):
        self.moving_right = True
        
    def go_left(self):
        self.moving_left = True
    
    def stop_moving_right(self):
        self.moving_right = False
    
    def stop_moving_left(self):
        self.moving_left = False
    
    def move(self):
        if self.moving_right and self.xcor() <350:
            self.goto(self.xcor() + self.move_speed, self.ycor())
        if self.moving_left and self.xcor() > -350:
            self.goto(self.xcor() - self.move_speed, self.ycor())
            
