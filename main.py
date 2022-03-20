#importing relevany class from other modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#create screen object and setting up
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong-The Famous Arcade Game")
#turn off the animation
screen.tracer(0)

#Create paddle object
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Create ball object
ball = Ball()

#Create scoreboard object
scoreboard = Scoreboard()


#Setting keyboard menu to control game movement
screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    #When you turned off the animation you need to update screen every you did something in screen
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or (ball.distance(l_paddle) < 50 and ball.xcor()) < -320:
        ball.bounce_x()


    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()