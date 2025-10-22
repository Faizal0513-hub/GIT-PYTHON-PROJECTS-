import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Games")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)



def get_mouse_click_coordinate(x,y):
   print(x,y)
    




    


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states=[]


while  len(guessed_states) < 50 :
    answer_the_state = screen.textinput(title=f"{len(guessed_states)}/50 States are Correct", prompt="What's the another state name?").title()
    print(answer_the_state)
    if answer_the_state=="Exit":
        remaining_states = [state for state in all_states if state not in guessed_states]
      
        # for state in all_states:
        #     if state not in guessed_states:
        #         remaining_states.append(state)

        
        Data = pandas.DataFrame(remaining_states)
        Data.to_csv("missed_states.csv")
        
        break
    
   
        
        
        
    if answer_the_state in all_states:
           guessed_states.append(answer_the_state)
           t= turtle.Turtle()
           t.hideturtle()
           t.penup()
           state_data=data[data.state==answer_the_state] # checks the column in the state
           t.goto(state_data.x.item(),state_data.y.item())
           t.write(answer_the_state)

        
       







