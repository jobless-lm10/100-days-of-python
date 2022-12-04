from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(5)

def move_backwards():
    turtle.back(5)

def rotate_clockwise():
    turtle.right(5)

def rotate_anti_clockwise():
    turtle.left(5)

def clear():
    turtle.clear()
    turtle.reset()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(rotate_anti_clockwise, 'a')
screen.onkey(rotate_clockwise, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
