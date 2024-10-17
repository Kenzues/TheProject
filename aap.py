import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
colors = ["red", "yellow", "blue", "red", "green", "white"]

# Draw a colorful spiral
for i in range(200):
    spiral_turtle.color(colors[i % 6])
    spiral_turtle.width(i // 100 + 1)  # Increase the width every 100 steps
    spiral_turtle.forward(i)
    spiral_turtle.left(59)  # Changing the angle creates a spiral pattern

# Finish up
spiral_turtle.hideturtle()
turtle.done()
