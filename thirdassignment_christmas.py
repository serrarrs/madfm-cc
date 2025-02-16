import turtle as t

# screen
t.bgcolor("sky blue")
t.speed(0)
t.hideturtle()

# base
t.penup()
t.goto(0, -300)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(250)
t.end_fill()

# triangle
t.penup()
t.goto(-120, -60)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(3):
    t.forward(250)
    t.left(120)
t.end_fill()

# pom - pom
t.penup()
t.goto(5, 140)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

# trim
t.penup()
t.goto(-105, -80)
t.pendown()
t.color("white")
for i in range(12):
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.pendown()

# message
t.penup()
t.goto(-150, -200)
t.pendown()
t.color("white")
t.write("Happy Christmas", font=("Consolas", 25, "bold"))




t.hideturtle()

t.done()
