import random
import turtle
from freegames import vector

# 定义红球的初始位置
ball = vector(-200, -200)
# 定义红球的移动距离
spend = vector(0, 0)
# 篮球列表
targets = []


def tap(x, y):
    if not isside(ball):
        ball.x = -199
        ball.y = -199
        spend.x = (x + 200) / 25
        spend.y = (y + 200) / 25


def draw():
    # 清屏，重新绘制
    turtle.clear()

    for tar in targets:
        turtle.goto(tar.x, tar.y)
        turtle.dot(20, 'blue')

    if isside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(10, 'red')
    # 刷新屏幕，在禁用追踪时使用
    turtle.update()


def isside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def move():
    if random.randrange(40) == 0:
        y = random.randrange(-150, 150)
        ta = vector(200, y)
        targets.append(ta)

    for t in targets:
        t.x -= 0.5

    if isside(ball):
        spend.y -= 0.35
        ball.move(spend)

    dupe = targets.copy()
    targets.clear()

    for t in dupe:
        # 篮球20+红球10的距离的一半
        if abs(t - ball) > 15:
            targets.append(t)

    draw()

    for t in targets:
        if not isside(t):
            return
    turtle.ontimer(move, 50)


turtle.setup(420, 420, 370, 0)
# 隐藏乌龟
turtle.hideturtle()
turtle.up()
# 关闭追踪，关闭轨迹
turtle.tracer(False)
# 绑定tap函数到鼠标点击屏幕事件
turtle.onscreenclick(tap)
move()
# 暂停画笔绘制，但绘图窗体不关闭
turtle.done()
