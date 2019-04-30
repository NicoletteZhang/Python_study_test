from tkinter import *
import random
import time #调用时间函数

class Ball:
    def __init__(self,canvas,paddle,color):
        #初始化对象，即创建对象设置属性,此外__init__函数是在对象被创建的同时就设置属性的一种方法，Python会在创建新对象是自动调用这个函数
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)#（10,10）表示左上角x,y坐标，（25,25）表示右下角x,y坐标，填充色
        self.canvas.move(self.id, 245,100)#将球移动到画布中心
        self.paddle = paddle
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):#判断小球是否撞到球拍上面的函数
        paddle_pos = self.canvas.coords(self.paddle.id)#将拍子的坐标放到变量paddle_pos中
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return  True
            return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)#0表示不要水平移动，-1表示在屏幕上向上移动1个像素
        pos = self.canvas.coords(self.id)#coords画布函数，通过ID返回画布上任何画好的东西的当前x,y坐标
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True#当小球移动到底部时，=True，则停止游戏
        if self.hit_paddle(pos) == True:#判断小球是否撞到球拍上面
            self.y = -3
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # （10,10）表示左上角x,y坐标，（25,25）表示右下角x,y坐标，填充色
        self.canvas.move(self.id, 200, 300)  # 将球移动到画布中心
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#按键时调用函数，< >内为 事件名字，让对象对操作有反应
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0#move函数在变量x的方向上撞到边界则停止
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):#改变向左向右的方向
        self.x = -2
    def turn_right(self,evt):
        self.x = 2

tk = Tk()
tk.title("Game") #给窗口命名
tk.resizable(0,0)#窗口的大小不可调整，第一个参数表示长，0，0的意思是“窗口的大小在水平方向上和垂直方向上都不能改变”
tk.wm_attributes("-topmost",1)#将画布的窗口始终放到所有其他窗口之前
canvas = Canvas(tk,width=500, height=400, bd=0, highlightthickness=0)#后两个参数作用：确保画布之外没有边框，使得屏幕更美观
canvas.pack()
tk.update()#为动画做好初始化

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)