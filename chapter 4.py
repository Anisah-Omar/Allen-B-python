# 4.3.1 - square function
import turtle

my_turtle = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
square(my_turtle)

 4.3.2 - square function w/ length param

import turtle

my_turtle = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
square(my_turtle, 50)
square(my_turtle, 200)
square(my_turtle, 63.75)
square(my_turtle, -50)
Generalization - making a function more general-purpose by adding parameters to the function definition.

# 4.3.3 - polygon function
import turtle

def polygon(t, length, n):
    t = turtle.Turtle()
    angle = 360 // n

    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(my_turtle, 50, 5)
polygon(my_turtle, 200, 3)
## keyword arguments:
polygon(t=my_turtle, length=63.75, n=6)
polygon(t=my_turtle, length=-50, n=8)
When passing arguments to a function, you can specify which parameter the argument is for; These style of arguments are keyword arguments.

4.6 Interface Design
# 4.3.4 - circle function

import math, turtle

my_turtle = turtle.Turtle()

def circle(t, r):
    circumference = math.pi * r * 2
    n = (circumference // 3) + 3	# from book
    length = circumference / n
    polygon(t, length, n)
        
circle(my_turtle, 200)
circle(t=my_turtle, r=-100)
Function Interface - summary of how the function is used:

Parameters
What the function does
Return value
4.7 Refactoring
We cannot re-use polygon() to create arc() the same way we did with circle(). Instead, we will create a general function named polyline(), then refactor polygon() to use polyline().

# polyline function
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
# refactored polygon function
def polygon(t, length, n):
    angle = 360 / n
    polyline(t=t, n=n, length=length, angle=angle)
# refactored circle function
def circle(t, r):
    arc(t=t, r=r, angle=360)
# arc function
def arc(t, r, angle):
    arc_length = get_circumference(r) * angle / 360
    n = int(math.fabs(arc_length) / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t=t, n=n, length=step_length, angle=step_angle)
Refactoring - the process of rearranging a program to improve its interfaces and facilitate code re-use.





# exercises/4.2.py

import math, turtle

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def petal(t, curve):
    n = 10  # looks pretty smooth, doesn't need math
    length = 100    # fixed size for petals
    polyline(t=t, n=n, length=length / n, angle=curve / n)
    t.lt(180 - (curve))
    polyline(t=t, n=n, length=length / n, angle=curve / n)
    t.lt(180 - (curve))

def flower(t, petals, curve, offset=0):
    t.lt(offset)
    for i in range(petals):
        petal(t=t, curve=curve)
        # rotate for next petal
        t.lt(360 / petals)

# instantiate turtle
my_turtle = turtle.Turtle()


# testing
## draw test flower
flower(t=my_turtle, petals=7, curve=45, offset=15)

## reset position, change color to red
my_turtle.pencolor("red")
my_turtle.pu()
my_turtle.setpos(0,0)
my_turtle.seth(0)
my_turtle.pd()

## draw second test flower
flower(t=my_turtle, petals=10, curve=100)

## reset position, change color to cyan
my_turtle.pencolor("cyan")
my_turtle.pu()
my_turtle.setpos(0,0)
my_turtle.seth(0)
my_turtle.pd()

## draw third test flower
flower(t=my_turtle, petals=20, curve=10)
