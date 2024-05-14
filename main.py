import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

t = turtle.Turtle()
t.hideturtle()
t.penup()

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = []
        for state in states_list:
            if state not in correct_guesses:
                missed_states.append(state)
        data_to_save = {
            "missed_states": missed_states
        }
        pandas.DataFrame(data_to_save).to_csv("missed_states.csv")
        break
    if answer_state in correct_guesses:
        continue
    if answer_state in states_list:
        correct_guesses.append(answer_state)
        correct_guess = data[data.state == answer_state]
        x = int(correct_guess.x)
        y = int(correct_guess.y)
        t.goto(x, y)
        t.write(answer_state)


