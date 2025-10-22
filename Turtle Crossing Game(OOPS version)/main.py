import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager =CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(player.go_up ,"Up")
screen.onkey(player.go_down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if player.distance(car) < 20:

            screen.clear()
            scoreboard.game_over()
            game_is_on=False
            
    if player.is_on_the_finishline():
        player.go_start_position()
        car_manager.move_faster()
        scoreboard.add_score()
    
            

screen.exitonclick()
