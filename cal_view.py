from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import cal_buttons as cb
import alien_invasion as ai


# 继承Frame类
class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.text = StringVar
        self.create_vip_calculator()

    def create_vip_calculator(self):
        # 创建文本框
        text = StringVar()
        Entry(self, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=10, ipady=15)
        style = Style()
        style.configure('TButton', padding=3)
        # 创建按钮
        cb.create_vip_button(self, text)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.create_page()

    def create_page(self):
        Label(self, text='科学界面').pack()


class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        Label(self, text='统计界面').pack()


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        Label(self, text='财务界面').pack()


class Games(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_button()
        self.create_page()

    def create_page(self):
        Label(self, text='').pack()

    def create_button(self):
        # 创建 飞机大战 的按钮
        w = Button(self, text='飞机大战', command=lambda: ai.run_game())
        w.pack(side=TOP, expand=YES, fill=BOTH, padx=4, pady=40, ipadx=40, ipady=30)
        # 创建 贪吃蛇 的按钮
        w = Button(self, text='贪吃蛇', command=lambda: run_game())
        w.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=4, pady=20, ipadx=40, ipady=30)

    def run_alien(self):
        ai.rungame()


