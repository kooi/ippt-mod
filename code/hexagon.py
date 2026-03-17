import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def hexagon():
    for i in range(6):
        tina.forward(50)
        tina.right(60)


for i in range(10):
    hexagon(i*10)
