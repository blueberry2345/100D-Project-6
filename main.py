import random
import time
from turtle import Screen, Turtle
from ball import Ball

# Create screen.
screen = Screen()
screen.title("Breakout")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create paddle for user to interact with.
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.penup()
paddle.goto(0,-250)

# Turtle that displays current score on the screen.
total_score = 0
score = Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(-20,-50)
score.write(total_score, font=("Arial", 20, "normal"))

# Create ball for the game.
game_ball = Ball()

colors = ["red", "blue", "green", "orange", "purple", "yellow"]
blocks = []

# Loop that creates blocks for top line.
for i in range(15):
    block = Turtle()
    block.color(random.choice(colors))
    block.shape("square")
    block.shapesize(stretch_wid=2, stretch_len=2)
    block.penup()
    block.goto(-355 + (i * 50),275)
    blocks.append(block)

# Loop that creates blocks for lower line.
for i in range(15):
    block = Turtle()
    block.color(random.choice(colors))
    block.shape("square")
    block.shapesize(stretch_wid=2, stretch_len=2)
    block.penup()
    block.goto(-355 + (i * 50),225)
    blocks.append(block)

# Function to let paddle move left or right if its not currently on the edge of the screen.
def go_left():
    if paddle.xcor() > -340:
        paddle.goto((paddle.xcor() - 20), paddle.ycor())

def go_right():
    if paddle.xcor() < 340:
        paddle.goto((paddle.xcor() + 20), paddle.ycor())

# Set game to be on until game has finished.
game_on = True

screen.listen()

# Move paddle using left or right arrow key.
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


while game_on:
    time.sleep(0.1)
    screen.update()
    game_ball.move()

    # If ball reaches block then bounce the ball, remove the block and update score.
    for i in blocks:
        if game_ball.distance(i) < 35:
            game_ball.bounce()
            blocks.remove(i)
            i.hideturtle()
            score.clear()
            score.goto(-20, -50)
            total_score += 1
            score.write(total_score, font=("Arial", 20, "normal"))


    # Bounce ball vertically if it reaches ceiling.
    if game_ball.ycor() > 280:
        game_ball.bounce()

    # Bounce ball if it touches paddle.
    if game_ball.distance(paddle) < 50 and game_ball.ycor() < -220 and game_ball.ycor() > -250 and game_ball.y_move < 0:
        game_ball.bounce()

    # Bounce ball horizontally if it reaches horizontal edge of screen.
    if game_ball.xcor() > 380 or game_ball.xcor() < -380:
        game_ball.bounce_horizontal()

    # End game if user eliminates all blocks.
    if (len(blocks) == 0):
        score.clear()
        score.goto(-20, -50)
        total_score += 1
        score.write("Victory!", font=("Arial", 20, "normal"))
        game_ball.hideturtle()
        time.sleep(5)
        game_on = False


screen.exitonclick()
