import turtle
import random

# Screen setup
WIDTH, HEIGHT = 500, 500
FOOD_SIZE = 10
DELAY = 100

# Offsets for snake movement
OFFSETS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    # Initialize or reset the game state.
    global snake, snake_dir, food_position
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

def move_snake():
    # Handle the movement of the snake.
    global snake_dir

    # Calculate new head position
    new_head = snake[-1].copy()
    new_head[0] += OFFSETS[snake_dir][0]
    new_head[1] += OFFSETS[snake_dir][1]

    # Collision detection with itself
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        # Check for food collision
        if not food_collision():
            snake.pop(0)

        # Wrap around screen edges
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < -WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Update screen and redraw
        pen.clearstamps()
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
        screen.update()

        # Recursive call to continue movement
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    # Check if snake collides with food.
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    # Generate a random position for food.
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return x, y

def get_distance(pos1, pos2):
    # Calculate the distance between two points.
    return ((pos2[1] - pos1[1]) ** 2 + (pos2[0] - pos1[0]) ** 2) ** 0.5

# Directional controls
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

# Screen configuration
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game - Python Edition")
screen.bgcolor("blue")
screen.tracer(0)

# Create turtle objects for snake and food
pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Start the game
reset()
turtle.done()
