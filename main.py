from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
new_snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        score.increase_score()
    if new_snake.head.xcor() > 290 or new_snake.head.xcor() < -290 or new_snake.head.ycor() > 290 or new_snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
