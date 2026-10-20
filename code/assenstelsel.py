import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def teken_pos_x_as(n, step=50, tick=10, width=2, show_tick=False):
    tina.penup()
    tina.goto(0,0)
    tina.setheading(0)
    tina.pendown()
    tina.width(width)
    for i in range(n):
        tina.forward(step)
        tina.left(90)
        if not show_tick:
            tina.penup()
        tina.forward(tick)
        tina.backward(2*tick)
        tina.write(" "+str((i+1)*step))
        tina.forward(tick)
        if not show_tick:
            tina.pendown()
        tina.pendown()
        tina.right(90)
        
def teken_neg_x_as(n, step=50, tick=10, width=2, show_tick=False):
    tina.penup()
    tina.goto(0,0)
    tina.setheading(0)
    tina.pendown()
    tina.width(width)
    for i in range(n):
        tina.backward(step)
        tina.left(90)
        if not show_tick:
            tina.penup()
        tina.forward(tick)
        tina.backward(2*tick)
        tina.write(" -"+str((i+1)*step))
        tina.forward(tick)
        if not show_tick:
            tina.pendown()
        tina.pendown()
        tina.right(90)
        


teken_pos_x_as(5, show_tick=True)
teken_neg_x_as(5, show_tick=True)


# tina tekent een assenstelsel
