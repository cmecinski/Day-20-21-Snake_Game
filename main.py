from turtle import Screen, Turtle
from snake import Snake
import time

#Create starting Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
#Turns animation off to allow it to be manually updated
screen.tracer(0)

#Create Starting 3 tile Snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()