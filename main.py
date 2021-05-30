from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
snake = Snake()
food = Food()
score = Score()

screen.bgcolor("black")
screen.setup(height=800, width=1000)
screen.title("My Snake Game")
is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while is_on:
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        score.update()
        snake.add_segment()
    if snake.snake_body[0].xcor() > 480 or snake.snake_body[0].xcor() < -480 or snake.snake_body[0].ycor() > 380 or snake.snake_body[0].ycor() < -360:
        is_on = False
        score.game_over()
    for body in snake.snake_body:
        if body == snake.snake_body[0]:
            pass
        elif body.distance(snake.snake_body[0]) < 10:
            is_on = False
            score.game_over()
screen.exitonclick()
