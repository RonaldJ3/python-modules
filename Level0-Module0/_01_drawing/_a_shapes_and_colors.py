import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    BoB = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    BoB.shape('turtle')
    # Set your turtle's speed using .speed(2)
    BoB.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    BoB.color('green')
    BoB.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    BoB.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    BoB.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        BoB.forward(100)
        BoB.right(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    BoB.penup()
    BoB.goto(100, 150)
    BoB.pendown()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    BoB.begin_fill()
    BoB.circle(100, 360)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    BoB.end_fill()
    # Draw 3 more shapes with different fill colors!
    BoB.penup()
    BoB.goto(-200, 150)
    BoB.pendown()
    BoB.color('blue')
    BoB.begin_fill()
    for i in range(4):
        BoB.forward(100)
        BoB.right(90)
    BoB.end_fill()
    BoB.penup()
    BoB.goto(-100, -100)
    BoB.pendown()
    BoB.color('red')
    BoB.begin_fill()
    BoB.forward(100)
    BoB.right(90)
    BoB.forward(100)
    BoB.right(135)
    BoB.forward(100)
    BoB.penup()
    BoB.goto(-200, -125)
    BoB.end_fill()
    BoB.pendown()
    BoB.color('purple')
    BoB.forward(100)
    BoB.right(90)
    BoB



    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
