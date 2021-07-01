import turtle
import random
import utils

boms = {}
show = {}
boxTotal = {}


def message():
    # 创建原始数据
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            boms[i, j] = False
            show[i, j] = False
            boxTotal[i, j] = -1

    # 随机创建10个雷
    for x in range(10):
        i = random.randrange(-175, 176, 50)
        j = random.randrange(-175, 176, 50)
        boms[i, j] = True

    # 创建每个网格周边的雷数量
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            totalNum = 0
            for x in (-50, 0, 50):
                for y in (-50, 0, 50):
                    try:
                        if boms[x, y]:
                            totalNum += 1
                    except:
                        continue
            boxTotal[i, j] = totalNum


# 画网格
def Draw():
    for i in range(-200, 200, 50):
        utils.line(i, -200, i, 400)
        for j in range(-200, 200, 50):
            utils.line(i, j, i + 400, j)

    turtle.update()


def end():
    for i in range(-175, 176, 50):
        for j in range(-175, 176, 50):
            if boms[i, j]:
                shouwBom(i, j)


def fclick(x, y):
    x = mappings(x)
    y = mappings(y)
    # if show[x, y]:
    #     return

    # 点到雷了，游戏结束
    if boms[x, y]:
        end()


def mappings(num):
    return num // 50 * 50 + 25


def shouwBom(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(10, "red")
    turtle.update()
    turtle.down()


turtle.setup(410, 410)
turtle.hideturtle()
turtle.tracer(False)
Draw()
message()
print(show[-175, -175])
turtle.up()
turtle.onscreenclick(fclick)
turtle.done()
