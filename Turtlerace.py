import turtle
import random

Turt = turtle.Turtle()

Turt.color("black")
Turt.shape("turtle")
Turt.penup()
Turt.goto(-160, 100)
Turt.pendown()

Turt2 = turtle.Turtle()

Turt2.color("red")
Turt2.shape("turtle")
Turt2.penup()
Turt2.goto(-160, 80)
Turt2.pendown()

Turt3 = turtle.Turtle()
Turt3.color("blue")
Turt3.shape("turtle")
Turt3.penup()
Turt3.goto(-160, 60)
Turt3.pendown()

Turt4 = turtle.Turtle()
Turt4.color("purple")
Turt4.shape("turtle")
Turt4.penup()
Turt4.goto(-160, 40)
Turt4.pendown()

for movement in range(100):
    Turt.forward(random.randint(1,10))
    Turt2.forward(random.randint(1,10))
    Turt3.forward(random.randint(1,5))
    Turt3.left(random.randint(0,10))
    Turt3.right(random.randint(0,10))
    Turt4.forward(random.randint(1,10))
    
    
