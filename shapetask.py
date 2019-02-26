import shapes
import random

rect1 = shapes.Rectangle()

rect1.set_x(100)
rect1.set_y(100)
rect1.set_width(random.randint(50,200))
rect1.set_height(random.randint(50,100))
rect1.set_color("red")
rect1.draw()

rect2= shapes.Rectangle()

rect2.set_x(200)
rect2.set_y(200)
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.draw()

oval1 = shapes.Oval()
oval1.randomize()
oval1.draw()
