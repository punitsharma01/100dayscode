import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_state_cords = pandas.read_csv("50_states.csv")
# print(len(us_state_cords))
# print(us_state_cords.iloc[0]["x"])
state_row = us_state_cords[us_state_cords["state"] == "Ohio"]
state = state_row.state.item()
x_cord = us_state_cords[us_state_cords["state"] == "Ohio"]["x"]
y_cord = us_state_cords[us_state_cords["state"] == "Ohio"]["y"]
x, y = state_row.x.item(), state_row.y.item()
# print(x_cord.iloc[0], y_cord.iloc[0])
# print(x, y)

ind = us_state_cords.index[us_state_cords["state"] == "Ohio"].tolist()
# print(ind[0])
# print(cord.at[ind[0], "x"])

# State Guessing Game
us_states_list = us_state_cords["state"].tolist()
guessed_states = []
for i in range(len(us_state_cords)):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(us_state_cords)} States Correct",
        prompt="What's the name of another state?"
    ).title()
    if answer_state == "Exit":
        missing_states = list(set(us_states_list) - set(guessed_states))
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in us_states_list:
        input_state = answer_state.capitalize()
        guessed_states.append(input_state)
        state_row = us_state_cords[us_state_cords["state"] == input_state]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(state_row.x.item(), state_row.y.item())
        tim.write(state_row.state.item(), align="center", font=("Courier", 16, "normal"))
        # print(state_row.x.item(), state_row.y.item())
