from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

DELAY = 0.1
PROXIMITY = 15
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(DELAY)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < PROXIMITY:
        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
