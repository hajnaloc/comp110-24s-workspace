"""TODO: Yellow Church with a window and chimney in the green country side with flowers in the field in front of it and the sun shining high above!"""

__author__ = "730468225"
from turtle import Turtle, colormode, done
import random

colormode(255)

# Drawing Functions


def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle, this will be the base main area of the church. It will be shaded yellow!"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_triangle(turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw an equilateral triangle. This will be the roof of our church whcih will be able to keep the people dry as they go about there prayers!"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()


def draw_circle(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle. This will be the glorious sun that is shining over the fields of peonys and the church!"""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_house(turtle: Turtle) -> None:
    """Draw a basic house. This will put the house together, main rectangle base with a roof, a single window and a chimney!"""
    # Draw the base
    draw_rectangle(turtle, -100, -100, 200, 150)
    
    # Draw the roof
    draw_triangle(turtle, -100, 50, 200)

    # Draw the door
    draw_rectangle(turtle, -20, -100, 40, 80)
    
    # Draw the window
    draw_rectangle(turtle, -70, -30, 40, 40)

    # Draw the chimney
    draw_rectangle(turtle, 50, 20, 20, 60)
    draw_rectangle(turtle, 50, 70, 40, 20)

    # Draw the sun
    draw_circle(turtle, 150, 150, 30)


def draw_ground_with_flowers(turtle: Turtle) -> None:
    """Draw the ground with flowers. Here we will have the vast open green grass in front of the church and in it there will be five red peoney flowers!"""
    # Draw ground
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(0, 150, 0)  # Green color for ground
    turtle.goto(300, -100)
    turtle.goto(300, -300)
    turtle.goto(-300, -300)
    turtle.goto(-300, -100)
    turtle.end_fill()

    # Define the region for flowers
    flower_region_x = (-300, 300)
    flower_region_y = (-300, -100)

    # Draw flowers
    for _ in range(5):
        x = random.randint(*flower_region_x)
        y = random.randint(*flower_region_y)
        draw_circle(turtle, x, y, 10)
        turtle.color("red")  # Flower color
        turtle.penup()
        turtle.goto(x, y - 20)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()

# Main 


def main() -> None:
    """Main function will call each of the parts of my drawing together and actually draw the yellow church with the sun and the green field of flowers!"""
    leo = Turtle()

    # Setting pen color and fill color
    leo.pencolor("pink")
    leo.fillcolor(32, 67, 93)
    leo.color("green", "yellow")

    draw_house(leo)
    draw_ground_with_flowers(leo)

    leo.speed(8)
    leo.hideturtle()

    done()


if __name__ == "__main__":
    main()