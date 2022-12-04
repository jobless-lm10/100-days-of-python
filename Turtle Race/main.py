from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = {}

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your Bet", prompt="Choose color of any turtle to place the bet on: ")

position_y = []
for i in range(1, len(colors)+1):
    position_y.append((400//(len(colors)+1)*i)-200)

for i in range(len(colors)):
    turtles[colors[i]] = Turtle(shape="turtle")
    turtles[colors[i]].color(colors[i])
    turtles[colors[i]].penup()
    turtles[colors[i]].setposition(x=-230, y=position_y[i])

race_finished = False
winner = None
while not race_finished:
    for turtle in turtles:
        if(turtles[turtle].xcor() > 230):
            race_finished = True
            winner = turtle
            break
        turtles[turtle].forward(randint(1, 10))

print(f"{winner.upper()} turtle won the race.")
if(user_bet.lower() == winner):
    print("Congratulations! Your selected turtle won the race.")
else:
    print("Sorry! Your selected turtle didn't win the race.")

screen.exitonclick()