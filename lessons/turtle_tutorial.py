"""Turtle Drawing!"""

__author__ = "730468225"

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Setting color mode to RGB
colormode(255)

# Setting pen color and fill color
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

# Drawing a triangle
leo.penup()
leo.goto(-50, 0) 
leo.pendown()

# Fill triangle
leo.begin_fill()
for _ in range(3):
    leo.forward(300)
    leo.left(120)
leo.end_fill()

# Adjusting turtle speed and visibility
leo.speed(5)
leo.hideturtle()

# Turtle Bob
bob: Turtle = Turtle()
bob.speed(10)
bob.color(0, 0, 0)  
bob.penup()
bob.goto(-50, -10)  
bob.pendown()

# Create an outline with Bob
side_length: int = 300
i: int = 0
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i += 1

side_length = 300  
bob.penup()
bob.goto(-50, -10)  
bob.pendown()
for _ in range(400):  
    bob.forward(side_length)
    bob.left(122)  
    side_length *= 0.97  

done()
