import turtle
import random
import time
from utils import vector

myself = vector(-0, -0)
ballList = []


def draw():
    turtle.clear()
    for ball in ballList:
        turtle.goto(ball.x, ball.y)
        turtle.dot(20, 'black')

    turtle.goto(myself.x, myself.y)
    if deathCheck():
        turtle.dot(10, 'red')
    else:
        turtle.dot(10, 'blue')

    turtle.update()


def addball():
    if 0 == random.randrange(5):
        ball = vector(200, random.randrange(-200, 200))
        ballList.append(ball)


def moveball():
    for ball in ballList:
        ball.x -= 5

    ballListNew = ballList.copy()
    ballList.clear()

    for ball in ballListNew:
        if ball.x > -200:
            ballList.append(ball)

    myself.y -= 7


def fclicl(x, y):
    myself.y += 30


def deathCheck():
    for ball in ballList:
        if abs(ball - myself) < 15:
            return True
        if myself.y < -200 or myself.y > 200:
            return True


def main():
    addball()
    moveball()
    draw()
    if deathCheck():
        time.sleep(1)
        ShowEnd()
        return
    turtle.ontimer(main, 100)


def ShowStart():
    turtle.clear()
    turtle.up()
    turtle.goto(-40, 50)
    turtle.down()
    turtle.write("START", font=("宋体", 25, "normal"))
    time.sleep(1)
    turtle.clear()


def ShowEnd():
    turtle.clear()
    turtle.up()
    turtle.goto(-70, 50)
    turtle.down()
    turtle.write("Game Over!", font=("宋体", 25, "normal"))
    time.sleep(1)
    turtle.clear()


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
ShowStart()
turtle.up()
turtle.onscreenclick(fclicl)
main()
turtle.done()
