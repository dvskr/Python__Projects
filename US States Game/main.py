from turtle import*
import pandas as pd
screen=Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
shape(image)



data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
print(all_states)

guessed_states=[]

while len(guessed_states)<50:

    answer_state = screen.textinput(title=f"{len(guessed_states)/50}", prompt="What's another state's name?r").title()

    if answer_state == "Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)


mainloop()
