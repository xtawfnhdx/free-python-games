import random
import turtle
import freegames


def getValue():
    return (3 + random.random() * 2) * random.choice([1, -1])


ball = freegames.vector(0, 0)
aim = freegames.vector(getValue(), getValue())


def draw():
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x > 200 or x < -200:
        aim.x = -aim.x

    if y > 200 or y < -200:
        aim.y = -aim.y

    turtle.clear()
    turtle.goto(x, y)
    turtle.dot(20)

    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.penup()
draw()
turtle.done()
