import turtle as t
from random import randint


screen = t.Screen()
screen.bgcolor('light blue')
screen.delay(0)


t.pensize(20)
t.speed(0)
t.penup()
t.goto(0, -100)
t.pendown()
t.color('green')

# L-system 
gens = 8 
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 10
angle = lambda: randint(20, 60)
stack = []
color = [0.2, 0.1, 0.0]  
thickness = 5

# Function 
def apply_rules(axiom):
    return ''.join([rule_1 if char == chr_1 else char for char in axiom])


def get_result(gens, axiom):
    for _ in range(gens):
        axiom = apply_rules(axiom)
    return axiom

axiom = get_result(gens, axiom)
t.left(90)  
t.pensize(thickness)

# Drawing the L-system
for char in axiom:
    t.color(color)
    if char == 'F' or char == 'X':
        t.forward(step)
    elif char == '@':
        step -= 6
        color[1] = min(1, color[1] + 0.04) 
        thickness = max(1, thickness - 2)
        t.pensize(thickness)
    elif char == '+':
        t.right(angle())
    elif char == '-':
        t.left(angle())
    elif char == '[':
        angle_, pos_ = t.heading(), t.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
    elif char == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        t.pensize(thickness)
        t.setheading(angle_)
        t.penup()
        t.goto(pos_)
        t.pendown()

screen.exitonclick()
