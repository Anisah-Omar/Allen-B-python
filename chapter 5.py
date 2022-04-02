exercises/5.2.1.py

def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else:
        print("No, that doesn't work")


check_fermat(1, 2, 3, 4)

 exercises/5.2.2.py

# fancy it up a bit
print("CHECK FERMAT")
print("--------------------------------")

print("Input a value for a: ", end="")
a = int(input())
print("Input a value for b: ", end="")
b = int(input())
print("Input a value for c: ", end="")
c = int(input())
print("Input a value for n: ", end="")
n = int(input())

def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else:
        print("No, that doesn't work")

print("")
print("checking if {} + {} == {}".format(a**n, b**n, c**n))
print("...")

check_fermat(a=a, b=b, c=c, n=n)

exercises/5.3.1.py

def is_triangle(a, b, c):
    check_a = bool(a <= b + c)
    check_b = bool(b <= a + c)
    check_c = bool(c <= a + b)

    if check_a and check_b and check_c:
        print("Yes")
    else:
        print("No")

is_triangle(3, 4, 5)
is_triangle(100, 1, 2)
is_triangle(2, 3, 5)
is_triangle(2, 3, 6)

exercises/5.3.2.py

print("side a: ", end="")
side_a = int(input())
print("side b: ", end="")
side_b = int(input())
print("side c: ", end="")
side_c = int(input())

def is_triangle(a, b, c):
    check_a = bool(a <= b + c)
    check_b = bool(b <= a + c)
    check_c = bool(c <= a + b)

    if check_a and check_b and check_c:
        print("Yes")
    else:
        print("No")

is_triangle(a=side_a, b=side_b, c=side_c)

 exercises/5.6.1.py

import turtle

def koch(t, length):
    if length >= 3:
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
    else:
        t.fd(length)

my_turtle = turtle.Turtle()

koch(t=my_turtle, length=120*4)

 exercises/5.6.2.py

import turtle

def koch(t, length):
    if length >= 3:
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
    else:
        t.fd(length)

def snowflake(t, length):
    for i in range(3):
        koch(t=t, length=length)
        t.rt(120)

my_turtle = turtle.Turtle()

snowflake(t=my_turtle, length=60)

exercises/5.6.3.py

# implementation of the Cesàro fractal variant

import turtle

def koch(t, length, angle):
    if length >= 3:
        koch(t=t, length=length/3, angle=angle)
        t.lt(angle)
        koch(t=t, length=length/3, angle=angle)
        t.rt(angle*2)
        koch(t=t, length=length/3, angle=angle)
        t.lt(angle)
        koch(t=t, length=length/3, angle=angle)
    else:
        t.fd(length)

def snowflake(t, length, angle):
    for i in range(3):
        koch(t=t, length=length, angle=angle)
        t.rt(120)

my_turtle = turtle.Turtle()

snowflake(t=my_turtle, length=240, angle=85)
