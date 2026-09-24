import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("BMW M5 CS - Python Turtle")

t = turtle.Turtle()
t.speed(0)
t.pensize(4)

# ---------- CAR BODY ----------
t.penup()
t.goto(-400, -120)
t.pendown()

t.fillcolor("darkgray")
t.begin_fill()

t.goto(-350, -70)
t.goto(-280, 20)
t.goto(-160, 90)
t.goto(40, 110)
t.goto(180, 70)
t.goto(300, 0)
t.goto(390, -60)
t.goto(400, -120)
t.goto(-400, -120)

t.end_fill()

# ---------- WINDOWS ----------
t.penup()
t.goto(-230, 25)
t.pendown()

t.fillcolor("lightblue")
t.begin_fill()

t.goto(-150, 80)
t.goto(-40, 90)
t.goto(-20, 30)
t.goto(-230, 25)

t.end_fill()

# Front window
t.penup()
t.goto(-5, 30)
t.pendown()

t.fillcolor("lightblue")
t.begin_fill()

t.goto(10, 90)
t.goto(120, 65)
t.goto(190, 15)
t.goto(-5, 30)

t.end_fill()

# ---------- FRONT GRILLE ----------
t.penup()
t.goto(300, -60)
t.pendown()

t.fillcolor("black")
t.begin_fill()

t.goto(360, -55)
t.goto(370, -105)
t.goto(305, -105)
t.goto(300, -60)

t.end_fill()

# Grille lines
for x in range(310, 365, 10):
    t.penup()
    t.goto(x, -65)
    t.pendown()
    t.goto(x, -100)

# ---------- HEADLIGHTS ----------
t.penup()
t.goto(245, -20)
t.pendown()

t.fillcolor("white")
t.begin_fill()

t.goto(300, -15)
t.goto(330, -35)
t.goto(270, -40)
t.goto(245, -20)

t.end_fill()

# ---------- WHEELS ----------
def wheel(x, y):
    t.penup()
    t.goto(x, y - 55)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    t.circle(55)
    t.end_fill()

    # Rim
    t.penup()
    t.goto(x, y - 35)
    t.pendown()

    t.fillcolor("silver")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    # Hub
    t.penup()
    t.goto(x, y - 10)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


wheel(-250, -120)
wheel(250, -120)

# ---------- SIDE LINE ----------
t.penup()
t.goto(-350, -40)
t.pendown()
t.color("red")
t.pensize(5)
t.goto(250, -40)

# ---------- DOORS ----------
t.color("black")
t.pensize(3)

t.penup()
t.goto(-120, 20)
t.pendown()
t.goto(-120, -80)

t.penup()
t.goto(70, 25)
t.pendown()
t.goto(70, -80)

# Door handles
t.penup()
t.goto(-80, -10)
t.pendown()
t.goto(-50, -10)

t.penup()
t.goto(110, -10)
t.pendown()
t.goto(140, -10)

# ---------- SIDE MIRROR ----------
t.penup()
t.goto(-10, 40)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# ---------- SPOILER ----------
t.penup()
t.goto(-340, 10)
t.pendown()

t.color("black")
t.pensize(8)
t.goto(-290, 30)

# ---------- GROUND ----------
t.penup()
t.goto(-500, -180)
t.pendown()

t.color("white")
t.pensize(3)
t.goto(500, -180)

# ---------- TEXT ----------
t.penup()
t.goto(-150, 250)
t.pendown()

t.color("white")
t.write(
    "BMW M5 CS",
    font=("Arial", 35, "bold")
)

t.hideturtle()

turtle.done()