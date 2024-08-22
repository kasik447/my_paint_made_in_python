from turtle import *


def draw_square(color):
    ti.pendown()
    ti.color('gray', color)
    ti.begin_fill()
    for i in range(4):
        ti.forward(40)
        ti.left(90)
    ti.end_fill()
    ti.penup()


def draw_symbol(symbol, indent):
    ti.forward(indent)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, font=('Arial', 12, 'normal'))
    ti.penup()


def circle_t(size):
    ti.pendown()
    ti.begin_fill()
    ti.color('gray')
    ti.circle(size)
    ti.end_fill()
    ti.penup()


ti = Turtle()
ti.penup()
ti.speed(0)

# Фон
indent = -20
ti.goto(-200, 80)
draw_symbol('Фон:', 5)
ti.goto(-200, 30)
draw_square('black')
draw_symbol('N', -20)
ti.goto(-200, -20)
draw_square('white')
draw_symbol('D', -20)


# Палитра
y = 180
indent = 42
ti.goto(-190, y)
draw_square('red')
draw_symbol('R', indent)

ti.goto(-130, y)
draw_square('orange')
draw_symbol('O', indent)

ti.goto(-70, y)
draw_square('yellow')
draw_symbol('Y', indent)

ti.goto(-10, y)
draw_square('green')
draw_symbol('G', indent)

ti.goto(50, y)
draw_square('light blue')
draw_symbol('L', indent)

ti.goto(110, y)
draw_square('blue')
draw_symbol('B', indent)

ti.goto(170, y)
draw_square('violet')
draw_symbol('V', indent)

#Толщина пера 
x = 200
y = 150
indent = 30
ti.goto(x, 140)
circle_t(5)
draw_symbol('1', indent)

ti.goto(x, 100)
circle_t(10)
draw_symbol('2', indent)

ti.goto(x, 53)
circle_t(15)
draw_symbol('3', indent)

ti.goto(x, 0)
circle_t(20)
draw_symbol('4', indent)

ti.goto(x, -60)
circle_t(25)
draw_symbol('5', indent)

ti.ht()
