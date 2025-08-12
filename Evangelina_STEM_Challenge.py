import turtle 
import random
t = turtle.Turtle()
  
# for background
# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("blue")
#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(4)

# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()
  
# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()
  
# for door and
# windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
t.right(90)
t.forward(15)
t.right(90)
t.forward(75)
t.circle(3)

# Create the Tree
# Draw the trees
t.penup()
t.goto(-200, -200)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-150, -150)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-100, -200)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the birds
t.penup()
t.goto(0, 50)
t.pendown()
t.color("black")
t.shape("triangle")
t.shapesize(0.5, 0.5)
t.stamp()

t.penup()
t.goto(50, 70)
t.pendown()
t.stamp()


# Create the Sun
# Set the turtle's position to the top-left corner
t.penup()
t.setposition(-280, 280)
t.pendown()

t.fillcolor('white')
t.begin_fill()

for i in range(36):
  t.forward(25)
  t.right(10)

t.end_fill()

# Draw the birds
t.penup()
t.goto(0, 50)
t.pendown()
t.color("black")
t.shape("triangle")
t.shapesize(0.5, 0.5)
t.stamp()

t.penup()
t.goto(50, 70)
t.pendown()
t.stamp()

#create xmas tree

# move turtle to bottom left corner
t.penup()
t.goto(-380, -250)
t.pendown()

# set turtle speed and color
t.speed(0)
t.color("green", "green")

# draw Christmas tree
t.begin_fill()
t.left(90)
t.forward(200)
t.right(90)
t.circle(-50, 120)
t.left(60)
t.circle(-50, 120)
t.right(90)
t.forward(200)
t.end_fill()

# set turtle color and position for trunk
t.color("brown", "brown")
t.penup()
t.goto(-180, -220)
t.pendown()

# draw trunk
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.end_fill()

# move turtle to draw star on top of tree
t.penup()
t.goto(-110, 70)
t.pendown()

# set turtle color and draw star
# Define a function to draw a star
def draw_star(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

# Draw 3 stars
for i in range(3):
    x = random.randint(-250, -150)
    y = random.randint(-50, 150)
    draw_star(x, y+10)
    draw_star(x-10, y-10)
    draw_star(x+10, y-10)

# draw grass 
# Set the turtle's position to the left bottom corner of the screen
t.penup()
t.goto(-300, -400)
t.pendown()

# Set the turtle's color to green
t.color("black")

# Draw the grass from left to right
t.left(90) # turn right 90 degrees to face up
for i in range(200):
    t.forward(200)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)

# Done!
turtle.done()
