# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = [(color.rgb.r, color.rgb.g,color.rgb.b) for color in colors]
#
# print(rgb_colors)

import turtle
import random

color_list = [(228, 227, 226), (246, 237, 243), (243, 244, 246), (234, 166, 59), (45, 112, 157), (113, 150, 203),
              (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117),
              (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116),
              (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188),
              (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.hideturtle()
number_of_dots = 100


def initialize_position():
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)


def go_to_new_line():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

initialize_position()
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        go_to_new_line()

screen = turtle.Screen()
screen.exitonclick()
