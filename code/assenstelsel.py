import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def walkto(x, y, c='orange'):
    tina.penup()
    tina.home()
    tina.pencolor(c)
    tina.pendown()
    tina.forward(x)
    tina.left(90)
    tina.forward(y)

def coord(x, y, lbl, sz=4):
    tina.pencolor('black')
    tina.penup()
    tina.goto(x, y)
    tina.pendown()
    tina.dot(sz)
    tina.write("   {} ({}, {}) ".format(lbl, x, y))

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
        
def teken_pos_y_as(n, step=50, tick=10, width=2, show_tick=False):
    tina.penup()
    tina.goto(0,0)
    tina.setheading(90)
    tina.pendown()
    tina.width(width)
    for i in range(n):
        tina.forward(step)
        tina.left(90)
        if not show_tick:
            tina.penup()
        tina.forward(tick)
        tina.write(" "+str((i+1)*step)+" ", align='right')
        tina.backward(2*tick)
        tina.forward(tick)
        if not show_tick:
            tina.pendown()
        tina.pendown()
        tina.right(90)
        
def teken_neg_y_as(n, step=50, tick=10, width=2, show_tick=False):
    tina.penup()
    tina.goto(0,0)
    tina.setheading(-90)
    tina.pendown()
    tina.width(width)
    for i in range(n):
        tina.forward(step)
        tina.left(90)
        if not show_tick:
            tina.penup()
        tina.forward(tick)
        tina.backward(2*tick)
        tina.write(" -"+str((i+1)*step)+" ", align='right')
        tina.forward(tick)
        if not show_tick:
            tina.pendown()
        tina.pendown()
        tina.right(90)
        

def teken_assenstelsel(show_tick=False):
    tina.speed(0)
    teken_pos_x_as(5, show_tick=show_tick)
    teken_pos_y_as(5, show_tick=show_tick)
    teken_neg_x_as(5, show_tick=show_tick)
    teken_neg_y_as(5, show_tick=show_tick)
    tina.penup()
    tina.home()
    tina.pendown()

# einde defs    

teken_assenstelsel(show_tick=False)
tina.speed(2)

walkto(100, 100)
coord(100, 100, 'A')

tina.speed(0)






tina.penup()
tina.goto(0, 0)
tina.pendown()
