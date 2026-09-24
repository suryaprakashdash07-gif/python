import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw bird body
t.penup()
t.goto(-50, -50)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(80)
t.end_fill()

# Draw head
t.penup()
t.goto(30, 70)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw eye
t.penup()
t.goto(60, 100)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(7)
t.end_fill()

# Draw beak
t.penup()
t.goto(78, 80)
t.pendown()
t.fillcolor("red")
t.begin_fill()

for i in range(3):
    t.forward(30)
    t.left(120)

t.end_fill()

# Draw wing
t.penup()
t.goto(-20, 20)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.circle(45)
t.end_fill()

# Draw legs
t.penup()
t.goto(-30, -120)
t.pendown()
t.forward(50)

t.penup()
t.goto(30, -120)
t.pendown()
t.forward(50)

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()