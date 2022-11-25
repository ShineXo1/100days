import turtle
import colorgram
from turtle import Turtle, Screen
import random


# rgb_colors = []
# colors = colorgram.extract('damien-hirst-bromobenzotrifluoride.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
turtle.colormode(255)
t = Turtle()
screen = Screen()
t.hideturtle()
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
              (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190)]

t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 101
t.speed('fastest')

for dot_number in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    
    if dot_number % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen.exitonclick()
