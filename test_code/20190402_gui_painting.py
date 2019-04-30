# 导入turtle包的所有内容:
from turtle import *

def DrawSquare():
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('yellow')
    forward(100)
    right(90)

def DrawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

# DrawSquare()
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

for x in range(0, 250, 50):
    DrawStar(x, 0)

done()