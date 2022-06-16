import time
from turtle import Screen, Turtle
from snack import Snake
from food import Food
from score_board import Score_board

screen  = Screen()
timm1 = Turtle()
timm2 = Turtle()
timm3 = Turtle()
screen.setup(width= 600, height =  600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
segments = []
#squre area
# timm3.goto(x =66, y = 0)
# # timm3.shapesize(2.0, 2.0)
# timm3.shape("square")
# timm3.color("white")
# timm2.goto(x = 44, y=0)
# timm2.shape("square")
# timm2.color("white")
# timm1.goto(x = 22, y = 0)
# timm1.shape("square")
# timm1.color("white")

snake = Snake()
food = Food()
score_board = Score_board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colligion food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    # collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_one = False
        score_board.game_over()

    #detect collision with tail.
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_one = False
            score_board.game_over()



screen.exitonclick()