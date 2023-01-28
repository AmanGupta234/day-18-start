import turtle
from turtle import Turtle, Screen
import heroes

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for i in range(0,4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
# print(heroes.gen())

# for i in range(50):
#     j = -1
#     j = j ** i
#     if j == 1:
#         timmy_the_turtle.pendown()
#         timmy_the_turtle.forward(10)
#     else:
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(10)

# for i in range(3, 11):
#
#     for j in range(i):
#         timmy_the_turtle.forward(80)
#         timmy_the_turtle.right(360 / i)

import turtle as t
import random

########### Challenge 3 - Draw Shapes ########

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# tim.width(10)
#
# directions = [0, 90, 180, 270]
# i = 0
# tim.speed("fast")
# while i < 10000:
#     i += 1
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(random.randint(8, 50))
tim.pencolor(random_color())
tim.speed('fastest')
tim.circle(100)
tim.left(5)

while tim.heading() != 0:
    tim.pencolor(random_color())
    tim.circle(100)
    tim.left(5)
screen = Screen()
screen.exitonclick()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
