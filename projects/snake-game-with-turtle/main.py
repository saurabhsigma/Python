import turtle
import time
import random

# Game settings
delay = 100  # Delay in milliseconds (100ms = 0.1s)
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off auto-screen updates

# Head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "up"  # Snake starts moving UP

# Food
food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(['circle']))
food.color(random.choice(['red', 'green', 'black']))
food.penup()
food.goto(0, 100)

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# Snake body segments
segments = []

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Move function
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings for movement (WASD + Arrow Keys)
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")


# Main game loop (event-driven)
def game_loop():
    global score, high_score, delay

    # Check collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()
    
    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

    # Move the body segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move first segment to head's previous position
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()  # Move the head

    # Check collision with body
    for segment in segments:
        if head.distance(segment) < 20:
            reset_game()

    wn.update()  # Update the screen
    wn.ontimer(game_loop, delay)  # Repeat function after delay

# Reset function to restart game
def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "up"

    for segment in segments:
        segment.goto(1000, 1000)  # Move body off-screen
    segments.clear()

    score = 0
    delay = 100  # Reset delay
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

# Start the game loop
game_loop()

# Keep the window open
wn.mainloop()
