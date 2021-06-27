import random
import turtle

from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    return value


def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random.random() - 0.5)
    aim.rotate(random.random() * 10 - 5)

    turtle.clear()
    turtle.goto(ant.x, ant.y)
    turtle.dot(4)

    turtle.ontimer(draw, 100)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()
draw()
turtle.done()
