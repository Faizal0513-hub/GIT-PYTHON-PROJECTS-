from turtle import Turtle,Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time



paddle=Turtle()
screen = Screen()

screen.bgcolor("black")
screen.title("Pong")
screen.setup(height=600,width=800)
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() <- 320 :
        ball.bounce_X()
       
        
    if ball.distance(right_paddle) < 50  or ball.distance(left_paddle) < 50 :
        ball.bounce_X()
        ball.add_speed()
        
    # Detecting if the paddle misses
    
    if ball.xcor() > 360 :
        ball.ball_bounds()
        screen.update()
        scoreboard.r_point()
        ball.bounce_X()
        

    elif  ball.xcor() < -360 :
        ball.ball_bounds()
        screen.update()
        scoreboard.l_point()
        ball.bounce_X()
    
        
    
        
        
        
        
        
screen.exitonclick()

















