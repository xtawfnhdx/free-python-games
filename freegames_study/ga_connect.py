import turtle
from freegames import vector, line

turns = {'red': 'yellow', 'yellow': 'red'}
#rows:用来存储每一列已经有几个着色
state = {'player': 'yellow', 'rows': [0] * 8}
print(state)

def grid():
    turtle.bgcolor('light blue')
    for x in range(-150, 200, 50):
        #划线
        line(x, -200, x, 200)
    #画圆
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            turtle.up()
            turtle.goto(x, y)
            turtle.dot(40, 'white')


def tap(x, y):
    player=state['player']
    rows=state['rows']

    #获取当前列已经有几个着色
    row=int((x+200)//50)
    count=rows[row]

    #计算要着色的圆的位置
    x=((x+200)//50)*50-200+25
    y=count*50-200+25

    turtle.up()
    turtle.goto(x,y)
    turtle.dot(40,player)
    turtle.update()

    rows[row]=count+1
    state['player']=turns[player]


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.onscreenclick(tap)
turtle.done()
