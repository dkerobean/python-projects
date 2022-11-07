import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = turtle.textinput(title=f"{len(guessed_state)}/50 Guessed Right", prompt="What's another state?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coord = data[data.state == answer_state]
        t.goto(int(state_coord.x), int(state_coord.y))
        t.write(answer_state)



turtle.mainloop()