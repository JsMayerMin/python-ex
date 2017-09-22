import turtle

def draw_square() :
    window = turtle.Screen()

    brad = turtle.Turtle()
        brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

draw_square()

