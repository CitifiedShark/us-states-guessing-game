import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# allows to add another type of shape
turtle.addshape(image)
turtle.shape(image)

score = 0

correct_guesses = []
data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()

game_is_on = True
while game_is_on:
    # creates popup question box
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another states name?")
    answer_state = answer_state.title()

    # Convert the guess to Title case
    # Check if the guess is among the 50 states
    # Write correct guesses onto the map
    # Use a loop to allow the user to keep guessing
    # Record the correct guesses in a list
    # Keep track of the score
    if answer_state == "Exit":
        states_to_learn_list = states_list
        for state in states_list:
            for guessed_state in correct_guesses:
                if guessed_state == state:
                    states_to_learn_list.pop(state)
        missing_states = pandas.DataFrame(states_to_learn_list)
        missing_states.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        if answer_state not in correct_guesses:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_row = data[data.state == answer_state]
            t.goto(state_row.x.item(), state_row.y.item())
            t.write(answer_state)

            correct_guesses.append(answer_state)
            score += 1

## states to learn.csv


