import turtle as t

def rectangle(horizental, vertical, color):
    t.pendown() # start drawing
    t.pensize(3)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3): # draw recangle
        t.forward(horizental)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup() # stop drawing
t.penup()
t.speed('slow') # turtle spped
t.bgcolor('Dodger blue')

# feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'grey')# draw the left leg
t.goto(-55, -50)
rectangle(-15, 100, 'grey') # draw the right leg

# body
t.goto(-90, 100)
rectangle(100, 150, 'red')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'grey') #  upper right arm
t.goto(-150, 110)
rectangle(15, 40, 'grey') # lower right arm

t.goto(10, 70)
rectangle(60, 15, 'grey') # upper left arm
t.goto(55, 110)
rectangle(15, 40, 'grey') # lower left arm

# neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# head
t.goto(-85, 170)
rectangle(80, 50, 'red')

# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')# draw the white part of the eye
t.goto(-60, 160)
t.goto(-55, 155)
rectangle(5, 5, 'black')# draw the right pupil
t.goto(-40, 155)
rectangle(5, 5, 'black')# draw the left pupil

# mouth
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'black')

t.hideturtle() # make the turtle invisible


# hands
t.goto(-155, 130)
rectangle(25, 25, 'green')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'green')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())