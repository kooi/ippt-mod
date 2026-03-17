import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def envelop(x, c):
    # definitie van de functie envelop() hier invullen

tina.penup()
tina.forward(-100)
tina.pendown()
envelop(50, "red")
tina.penup()
tina.forward(150)
tina.pendown()
envelop(100, "green")
