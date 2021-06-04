import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


total_state = len(data.state)
correct_state = []
missing_state = []
all_states = data.state.to_list()

while len(correct_state) <= 50:
    input_state = screen.textinput(title=f"{correct_state}/{total_state} States Correct", prompt="What's another state's name?")

    if input_state == "Exit":
        for state in all_states:
            if state not in correct_state:
                missing_state.append(state)
        print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if input_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_state.append(input_state)
        state_data = data[data.state == input_state.title()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(input_state.title())




turtle.mainloop()
