import random
import turtle
from freegames import vector

ball = vector(-200, -200)
spend = vector(0, 0)
targets = []


def tap(x, y):
    if not isside(ball):
        ball.x = -199
        ball.y = -199
        spend.x = (x + 200) / 25
        spend.y = (y + 200) / 25


def draw():
    turtle.clear()

    for tar in targets:
        turtle.goto(tar.x, tar.y)
        turtle.dot(20, 'blue')

    if not isside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(10, 'red')

    turtle.update()


def isside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def move():
    if random.randrange(40)==0:
        y=random.randrange(-150.150)
        ta=vector(200,y)
        targets.append(ta)

    for t in targets:
        t.x=-0.5

