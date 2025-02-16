import turtle as santa
import random

wn = santa.Screen()
wn.bgcolor("dark green")

santa.speed(0)  

# colors for ornaments
ornamentcolor = ["white", "blue", "red"]

def ornament(size):
    santa.penup()
    santa.forward(5 * size)
    santa.left(45)
    santa.pendown()
    santa.color(random.choice(ornamentcolor))
    
    
    for i in range(9):
        branch(size)
        santa.left(20)

def branch(size):
    for i in range(10):  
        for i in range(10):  
            santa.forward(10.0 * size / 6)
            santa.backward(10.0 * size / 6)
            santa.right(45)
        santa.left(90)
        santa.backward(10.0 * size / 6)
        santa.left(45)
    santa.right(90) 
    santa.forward(10.0 * size)

# ornaments
rows = 5  
cols = 5  
spacing = 100  

for row in range(rows):
    for col in range(cols):
        x = col * spacing - (cols * spacing) / 2  
        y = row * spacing - (rows * spacing) / 2  
        sf_size = random.randint(2, 10)  #
        santa.penup()
        santa.goto(x, y)
        santa.pendown()
        ornament(sf_size)  

santa.hideturtle()  
wn.exitonclick()  

