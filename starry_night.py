import turtle as t

from random import randint, random

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)

    t.end_fill()

def draw_planet(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(50)
    t.end_fill()   

# main code

t.Screen().bgcolor('dark blue')
while True:
    ranPts = randint(2, 5) * 2 +1
    randSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    col = (random(), random(), random())
    x = randint(-350, 300)
    y = randint(-250, 250)
    draw_star(ranPts, randSize, ranCol, ranX ,ranY)
    # draw_planet(col, x, y)




