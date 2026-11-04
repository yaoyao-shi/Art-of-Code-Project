import turtle
from random import randint
bgcolor = "black"
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor(bgcolor)
turtle.tracer(0)
a = turtle.Turtle()
a.speed(0)
a.pensize(5)


def star(num, size):
    for _ in range(num):
        x = randint(-500, 500)
        y = randint(-500, 500)
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
    a.goto(x, y - radius)
    a.pendown()
    a.pencolor("grey")
    a.fillcolor("white")
    a.begin_fill()
    a.circle(radius)
    a.end_fill()
    a.penup()
    a.goto(x + radius * 0.6, y - radius)
    a.pendown()
    a.pencolor(bgcolor)
    a.fillcolor(bgcolor)
    a.begin_fill()
    a.circle(radius)
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