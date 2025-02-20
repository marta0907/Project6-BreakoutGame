from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.05
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0, -230)
        self.y_move = abs(self.y_move)
        self.bounce_x()
    
    def detect_collision(self, walls, scoreboard): #with wall bricks
        for wall in walls:
            if self.distance(wall) < 40:  # Collision detected
                wall.goto(1000, 1000)  # Move the brick off-screen
                walls.remove(wall)  # Remove from wall list
                scoreboard.point()
                self.bounce_y()# Increase score
                break  # Exit after the first collision
    
            
            
        
        
        
