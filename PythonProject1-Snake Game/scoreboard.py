from turtle import Turtle





class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        with open("data.txt") as data:
            self.high_score= int(data.read())
   
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.scoring()
        self.penup()
        self.hideturtle()
        
        
    def scoring(self):
      
      
        self.clear()
        self.write(f"Your Score : {self.score}       High Score: {self.high_score}",align="center",font=("Arial",15,"normal"))
       
   
        
    def increase_score(self):
 
        self.score += 1
        self.write(f"Your Score : {self.score}       High Score: {self.high_score}", align="center",font=("Arial", 15, "normal"))
        self.scoring()
       
    
    def reset(self):
       
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
            
        self.score = 0
        self.scoring()
 
        
    