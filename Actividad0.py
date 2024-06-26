from turtle import *

from random import random

from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
snake_color = (100/255, 0/255, 30/255)
food_color = (0/255, 0/255, 20/255)


def change_color():
    """Change snake color randomly."""
    global food_color
    global snake_color 
    snake_color = (random(), random(), random()) 
    food_color = (random(), random(), random())

if snake_color == (255, 0, 0):
    change_color()       
if food_color == (255, 0, 0):
    change_color()  
        
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    move_x = randrange(-1, 2) * 10
    move_y = randrange(-1, 2) * 10
    new_food = vector(food.x + move_x, food.y + move_y)

    if inside(new_food):
        food.x = new_food.x
        food.y = new_food.y

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))

        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        change_color()

    else:
        snake.pop(0)

    move_food()
    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(change_color, 'c')
move()
done()
