from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_board()
game_over = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_upward)
screen.onkey(key="Down", fun=snake.turn_downward)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # Collision with a food
    if snake.segments[0].distance(food) < 18:
        food.refresh()
        snake.extend_body()
        scoreboard.add_score()

    # Collision with a wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_over.game_over()
        is_game_over = True

    # Collision with snake body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_over.game_over()
            is_game_over = True


screen.exitonclick()
