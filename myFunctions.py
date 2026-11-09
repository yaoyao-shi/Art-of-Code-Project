import turtle
from random import randint
bgcolor = "black"
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor(bgcolor)
screen.setup(width=960, height=800)
turtle.tracer(0)
a = turtle.Turtle()
a.speed(0)
a.pensize(5)
screenwidth = screen.window_width()
screenheight = screen.window_height()


def stars(num, size):
    for _ in range(num):
        x = randint(-screenwidth//2 + size, screenwidth//2 - size)
        y = randint(-screenheight//2 + size, screenheight//2 - size)
        a.penup()
        a.goto(x, y)
        a.pensize(size)
        a.fillcolor("white")
        a.begin_fill()
        a.pencolor(255, 255, 255)
        a.pendown()
        a.circle(size)
        a.end_fill()
        a.pensize(5)

def moon(x, y, radius):
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.pencolor("grey")
    a.fillcolor((195, 195, 195))
    a.begin_fill()
    for _ in range(20):
        a.forward(radius/290)
        a.left(1)
    a.setheading(180)
    a.heading()
    for _ in range(180):
        a.forward(radius/310)
        a.right(1)
    a.setheading(160)
    a.heading()
    for _ in range(200):
        a.forward(radius/290)
        a.left(1)
    a.end_fill()

def clouds(x, y, minsize, maxsize):
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.pencolor("white")
    a.fillcolor("white")
    for _ in range(5):
        a.begin_fill()
        s = randint(minsize, maxsize)
        a.circle(s)
        a.penup()
        a.forward(s * 1.5)
        a.pendown()
        a.end_fill()

def grass(distance, x, y):
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.pensize(5)
    a.pencolor("dark green")
    a.fillcolor("green")
    a.begin_fill()
    for _ in range(2):
        a.forward(distance)
        a.left(90)
        a.forward(distance/10)
        a.left(90)
    a.end_fill()

def mountain(x, y, min, max):
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.pencolor(99, 99, 99)
    a.fillcolor("gray")
    a.begin_fill()
    d = randint(min, max)
    for _ in range(3):
        a.forward(d)
        a.left(120)
    a.end_fill()

def trees(x, y, size):
    a.penup()
    a.goto(x, y)   
    a.pendown()
    a.pencolor("brown")
    a.fillcolor("brown")
    a.begin_fill()
    for _ in range(2):
        a.forward(size/5)
        a.left(90)
        a.forward(size)
        a.left(90)
    a.end_fill()
    a.penup()
    a.goto(x + size/10, y + size)
    a.pendown()
    a.pensize(5)
    for _ in range(3):
        a.pencolor("dark green")
        a.fillcolor("green")
        a.begin_fill()
        a.circle(size/4)
        a.left(120)
        a.end_fill()
    a.forward(0)