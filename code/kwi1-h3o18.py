# Kern Wiskunde V1
# H3 opg. 18

import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(3)

S = 20 # schaalfactor
# Tina werkt opgave 18 uit:

import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(3)

S = 20

coords = [
    (0,8),
    (1,3),
    (4,4),
    (3,1),
    (8,0),
    (3,-1),
    (4,-4),
    (1,-3),
    (0,-8),
    (-1,-3),
    (-4,-4),
    (-3,-1),
    (-8,0),
    (-3,1),
    (-4,4),
    (-1,3),
    (0,8)
]

tina.penup()

for x, y in coords:
    tina.goto(x*S, y*S)
#    tina.pendown()
    tina.dot(4)
#    tina.write("("+str(x)+","+str(y)+")")







