import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def tekenster():
    for i in range(12):
        tina.forward(50)
        tina.backward(50)
        tina.right(30)
