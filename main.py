from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from wall import Wall
import time

COLOR=["red", "red", "yellow", "yellow", "blue","blue", "green", "green"]
POSITION=[50, 75, 100, 125, 150, 175, 200, 225]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

#create objects
paddle = Paddle((0, -280))
ball = Ball((0, -230))
scoreboard = Scoreboard()

#create walls
walls = []
brick_width = 82  # Each brick's actual width after stretching
brick_height = 20  # Each brick's height
gap = 4  # Space between bricks
columns = 9  # Number of bricks per row
rows = 8  # Number of rows

for row in range(rows):
    y_position = POSITION[row]  # Use predefined Y positions
    for col in range(columns):
        x_position = -350 + col * (brick_width + gap)  # Adjust for spacing
        wall = Wall((x_position, y_position), COLOR[row])  # Create a Wall instance
        walls.append(wall)  # Store in the list

#paddle movement
screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeyrelease(paddle.stop_moving_right, "Right")
screen.onkeypress(paddle.go_left, "Left")
screen.onkeyrelease(paddle.stop_moving_left, "Left")

game_is_on = True
start_time = time.time()
while game_is_on:
    time.sleep(0.01)
    screen.update()
    paddle.move()
    ball.move()
    
    #detect collision with bricks
    ball.detect_collision(walls, scoreboard)
    
    #Detect collision with side wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # #Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() > -270:
        ball.bounce_y()

    #Detect paddle misses:
    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.loosing_life()
    
    # Bounce of the top boundary
    if ball.ycor() > 235:
        ball.bounce_y()
    
    #Increase speed of the ball after certain time
    if time.time() - start_time >10:
        ball.move_speed *= 0.90
        start_time = time.time()
    
    #End game if lives are 0
    if scoreboard.life == 0:
        scoreboard.game_over()
        game_is_on = False
    
    #End game if no more bricks
    if not walls:
        scoreboard.you_win()
        game_is_on = False

screen.exitonclick()