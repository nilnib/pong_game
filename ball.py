from turtle import Turtle

#Ball class inherits Turtle class by passing it
class Ball(Turtle):
    #Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    #ball movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    #ball bounce methods 1
    #Wall
    def bounce_y(self):
        self.y_move *= -1

    #ball bounce methods 2
    #Paddle
    def bounce_x(self):
        self.x_move *= -1
        #increase speed when ball touches the paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        #reset the ball speed after paddle misses the ball
        self.move_speed = 0.1
        self.bounce_x()