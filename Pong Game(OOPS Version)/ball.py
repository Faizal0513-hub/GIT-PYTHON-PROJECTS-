from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 10
        self.y_move = 10
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y =self.ycor()  + self.y_move
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.y_move*= -1
    
    def bounce_X(self):
        self.x_move *= -1
    
    def ball_bounds(self):
        self.goto(0,0)
    
    def add_speed(self):
        self.x_move+= 3
        self.y_move+= 3
        
    
    
        
      