FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-200,250)
        self.write( f" Level : {self.score}", align ="center", font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)
        
    def add_score(self):
        
        self.score+=1
        self.clear()
        
        self.goto(-200, 250)
        self.write(f" Level : {self.score}", align="center", font=FONT)

        
        
    
