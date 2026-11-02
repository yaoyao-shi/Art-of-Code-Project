import turtle
from random import randint

turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("orange")
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
    for _ in range(10):
        o = randint(0, 100)
        p = randint(0, 100)
        a.penup()
        a.goto(x + o, y + p - radius)
        a.pendown()
        a.pencolor("grey")
        a.fillcolor("white")
        a.begin_fill()

def grass(distance, x, y):
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.pencolor(27, 71, 25)
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