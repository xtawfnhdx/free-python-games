import turtle

state = {'turn': 0}
widthH = 100
widthC = 120


def draw():
    turtle.clear()

    agent = state["turn"] / 10
    turtle.right(agent)
    turtle.forward(widthH)
    turtle.dot(widthC, 'red')
    turtle.back(widthH)

    turtle.right(120)
    turtle.forward(widthH)
    turtle.dot(widthC, 'blue')
    turtle.back(widthH)

    turtle.right(120)
    turtle.forward(widthH)
    turtle.dot(widthC, 'yellow')
    turtle.back(widthH)

    turtle.right(120)

    turtle.update()


def check():
    if state['turn'] > 0:
        state['turn'] = 10
        draw()
    turtle.ontimer(check, 20)


def flick(x, y):
    if state['turn'] == 0:
        state['turn'] = 1
    else:
        state['turn'] = 0
    check()


def fkey():
    state['turn'] = 1


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.width(20)
draw()
# 方式1 点击屏幕
turtle.onscreenclick(flick)

# 方式2 按空格键
turtle.onkey(fkey, 'space')
turtle.listen()
check()
turtle.done()
