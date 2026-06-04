import turtle

sides = int(input("How many sides? "))

t = turtle.Turtle()

for i in range(sides):
    perimeter = 300
    side_length = perimeter / sides
    t.forward(side_length)
    t.left(360/sides)
turtle.done()
