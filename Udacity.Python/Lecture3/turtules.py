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

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.circle(100)

    angie2 = turtle.Turtle()
    angie2.shape("turtle")
    angie2.color("red")
    for x in range(0,3):
        angie2.forward(100)
        angie2.right(120)


draw_square()

