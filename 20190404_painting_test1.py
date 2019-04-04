# coding:utf-8
from turtle import *

def nose(x,y):
    pu()
    goto(x,y)
    pd()
    seth(-30)
    begin_fill()

    a = 0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()

    pu()
    seth(90)
    fd(25)
    seth(0)
    fd(10)
    pd()
    pencolor(255,155,192)
    seth(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

    pu()
    seth(0)
    fd(20)
    pd()
    pencolor(255,155,192)
    seth(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

def head(x,y):
    color((255,155,192),"pink")
    pu()
    goto(x,y)
    seth(0)
    pd()
    begin_fill()
    seth(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    seth(161)
    circle(-300,15)
    pu()
    goto(-100,100)
    pd()
    seth(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3)
            fd(a)
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()

# def ears(x,y):
#
# def eyes(x,y):
#
# def cheek(x,y):
#
# def mouth(x,y):
#
# def body(x,y):
#
# def hands(x,y):
#
# def foot(x,y):
#
# def tail(x,y):

def setting(): #参数设置
    pensize(4)
    hideturtle()
    colormode(255)
    color((255,155,192),"pink")
    setup(840,500)
    speed(100)

def main():
    setting()
    nose(-100,100)
    head(-69,167)
    # ears(0,160)
    # eyes(0,140)
    # cheek(80,10)
    # mouth(-20,30)
    # body(-32,-8)
    # hands(-56,-45)
    # foot(2,-177)
    # tail(148,-155)
    done()

main()