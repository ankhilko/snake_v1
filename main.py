import time
from turtle import Screen
from snake import Snake
from food import Food
import scoreboard
from gameconst import SCREEN_WIDTH, SCREEN_HEIGHT, border_w, border_h
import io

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake v.K")
my_score = scoreboard.Scoreboard()
screen.tracer(0)

game_is_on = True


def gameover():
    global game_is_on
    game_is_on = False
    pass


my_snake = Snake()

food = Food()

screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right, key="Right")
screen.onkey(fun=gameover, key="q")


def update_all():
    global my_snake
    global my_score
    my_score.update_snake()
    my_snake.update_snake()
    pass


while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(food) < 15:
        my_snake.extend()
        food.refresh()
        my_score.score_one()

    if my_snake.head.xcor() < -border_w or \
            my_snake.head.xcor() > border_w or \
            my_snake.head.ycor() < -border_h or \
            my_snake.head.ycor() > border_h:
        # game_is_on = False
        update_all()


    for segment in my_snake.snake_segments[1:]:
        if my_snake.head.distance(segment) < 5:
            # game_is_on = False
            update_all()

screen.exitonclick()
