import turtle  # For drawing
import random  # For randomness
import time    # For generating a random seed

# Generate a random seed based on the current time
my_random_seed = int(time.time() * 1000)
print("My random seed number:", my_random_seed)

random.seed(my_random_seed)  # Set the random seed

turtle.speed(5)  # Set drawing speed
turtle.colormode(1)  # Set color mode

# Define colors
colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD", "#E74C3C"]

# Grid settings
steps = 30  
rows = 10  
columns = 5  
random_angle = 0.0  

# Move turtle to starting position
turtle.penup()
turtle.goto(-columns * 0.5 * steps, rows * 0.5 * steps)

# Loop through rows
for row in range(rows):
    turtle.setheading(180)  # Move left
    turtle.forward(steps * columns)
    turtle.setheading(240)  # Move slightly down
    turtle.forward(steps)
    turtle.setheading(0)  # Face right

    random_coef = ((row + 1) / rows) ** 2  # Increase randomness down the rows

    # Loop through columns
    for column in range(columns):
        random_angle = random.random() * random_coef * 90  # Generate random tilt
        turtle.left(random_angle)

        turtle.pendown()
        print(turtle.pos())  # Print position for debugging

        turtle.pencolor(random.choice(colors))  # Choose a random color

        if (row + column) % 2 == 0:
            turtle.circle(steps // 2)  # Draw a circle
        else:
            for _ in range(6):  # Draw a hexagon
                turtle.forward(steps)
                turtle.left(60)

        turtle.penup()
        turtle.right(random_angle)  # Reset rotation
        turtle.forward(steps)  # Move to the next column

turtle.exitonclick()  # Close window on click
