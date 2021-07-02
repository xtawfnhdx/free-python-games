import turtle
import random
import utils
import time

bomList = {}
boxStart = {}
boxTotal = {}


# 显示提示信息
def showMsg(msg):
    # 画框
    turtle.up()
    turtle.seth(0)
    turtle.goto(-200, 30)
    turtle.fillcolor("BlanchedAlmond")
    turtle.begin_fill()
    turtle.down()
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

    # 写文字
    turtle.home()
    turtle.write(msg, True, align="center", font=("宋体", 20, "normal"))
    turtle.update()
    time.sleep(2)
    turtle.clear()


# 构造初始数据
def initdata():
    # 创建原始数据
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            bomList[i, j] = False
            boxStart[i, j] = False
            boxTotal[i, j] = 0

    # 随机创建10个雷
    for x in range(10):
        i = random.randrange(-175, 176, 50)
        j = random.randrange(-175, 176, 50)
        bomList[i, j] = True

    # 创建每个网格周边的雷数量
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            totalNum = 0
            for x in (-50, 0, 50):
                for y in (-50, 0, 50):
                    try:
                        if bomList[i + x, j + y]:
                            totalNum += 1
                    except:
                        continue
            boxTotal[i, j] = totalNum


# 画网格
def drawBox():
    turtle.up()
    for i in range(-200, 201, 50):
        utils.line(i, -200, i, 200)
    for j in range(-200, 201, 50):
        utils.line(-200, j, 200, j)
    turtle.update()


# 游戏结束，显示所有雷
def end():
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            if bomList[i, j]:
                shouwBom(i, j)


def checkWin():
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            if not bomList[i, j] and not boxStart[i, j]:
                return False
    return True


def fclick(x, y):
    m, n = mappings(x, y)
    # 已经点击过的点
    if boxStart[m, n]:
        return

    # 点到雷了，游戏结束
    if bomList[m, n]:
        end()
        showMsg("GAME OVER !")
        restart()
        return
    checkbox(m, n)
    if checkWin():
        end()
        showMsg("YOU WIN !")
        restart()
        return


# 验证周边数据是否为雷
def checkbox(x, y):
    if x > 175 or x < -175 or y > 175 or y < -175:
        return
    if boxStart[x, y]:
        return
    if boxTotal[x, y] > 0:
        showbox(x, y)
        return
    for i in (-50, 0, 50):
        for j in (-50, 0, 50):
            boxStart[x, y] = True
            showbox(x, y)
            checkbox(x + i, y + j)


# 点击过的网格画样式
def showbox(x, y):
    boxStart[x, y] = True
    turtle.up()
    turtle.goto(x - 20, y + 20)
    turtle.fillcolor("Silver")
    turtle.begin_fill()
    turtle.down()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x - 7, y - 13)
    turtle.down()
    if boxTotal[x, y] > 0:
        turtle.write(boxTotal[x, y], font=("宋体", 20, "normal"))
    turtle.up()
    turtle.update()


# 将点击坐标映射为限定坐标
def mappings(x, y):
    return x // 50 * 50 + 25, y // 50 * 50 + 25


# 画雷
def shouwBom(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(10, "red")
    turtle.update()
    turtle.down()


# 重启游戏
def restart():
    turtle.clear()
    showMsg("GAME START !")
    initdata()
    drawBox()


# 启动游戏
def startGames():
    sc = turtle.Screen()
    sc.title("扫雷")
    turtle.setup(410, 410)
    turtle.hideturtle()
    turtle.tracer(False)
    restart()
    turtle.onscreenclick(fclick)
    turtle.done()


if __name__ == "__main__":
    startGames()
