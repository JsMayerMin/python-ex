import turtle

def draw_square(brad) :

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)


def draw_art() :
    window = turtle.Screen()

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    for i in range(36):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.circle(100)

    angie2 = turtle.Turtle()
    angie2.shape("turtle")
    angie2.color("red")
    for x in range(3):
        angie2.forward(100)
        angie2.right(120)


draw_art()

