from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter import font
import tkinter as tk
import cal_buttons as cb
import alien_invasion as ai
from tkinter import filedialog
import xlrd
import math
import cal_fin_presentpage as calpre
import cal_fin_futurepage as calfut
import cal_fin_simplepage as calsim
import cal_fin_programProfitPage as calpro
import cal_fin_capm as calcapm
import cal_fin_security as calsec
import cal_fin_stockPage as calsto
import cal_fin_annuity as calann
import cal_fin_OneOneRegression as caloor
import cal_fin_TwoOneRegression as calwor
import random


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


class Trial(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.text = StringVar
        self.create_trial_calculator()

    def create_trial_calculator(self):
        # 创建文本框
        text = StringVar()
        Entry(self, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=10, ipady=15)
        style = Style()
        style.configure('TButton', padding=3)
        # 创建按钮
        cb.create_trial_button(self, text)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.font_1 = font.Font(family='华文彩云', size=40, weight='bold')
        self.itemName = StringVar()
        self.photo = tk.PhotoImage(file="14.png")  # file：t图片路径
        self.create_page()

    def create_page(self):
        # self.page = Frame()
        # self.page.pack()
        # Label(self, text='信息查询').pack()
        Label(self, text="敬  请  期  待", justify=LEFT, font=self.font_1).pack(side=BOTTOM)  # 自动对齐
        # Label(self, text="    ", justify=LEFT, font=self.font_1).pack(side=BOTTOM)  # 自动对齐
        Label(self, text="    ", justify=LEFT).pack(side=BOTTOM)  # 自动对齐

        # 创建一个图片管理类
        Label(self, text="    ", justify=LEFT).pack(side=TOP)  # 自动对齐
        # Label(self, text="    ", justify=LEFT).pack(side=TOP)  # 自动对齐
        Label(self, image=self.photo).pack(side=TOP)  # 自动对齐


class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.mean = StringVar()
        self.median = StringVar()
        self.standard = StringVar()
        self.variance = StringVar()
        self.kurtosis = StringVar()
        self.skewness = StringVar()
        self.filename = None
        self.create_page()

    def create_page(self):
        font_1 = font.Font(family='华文彩云', size=6, weight='bold')
        # list = [mean.get(), median.get(), standard_deviation.get(), variance.get(), kurtosis.get(), skewness.get()]
        Label(self, text='     ').grid(column=0, row=0, columnspan=2)
        Label(self, text='均值:').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.mean).grid(row=1, column=1, stick=E)
        Label(self, text='中位数:').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.median).grid(row=2, column=1, stick=E)
        Label(self, text='标准差:').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.standard).grid(row=3, column=1, stick=E)
        Label(self, text='方差:').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.variance).grid(row=4, column=1, stick=E)
        Label(self, text='偏度:').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.kurtosis).grid(row=5, column=1, stick=E)
        Label(self, text='峰度:').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.skewness).grid(row=6, column=1, stick=E)
        Label(self, text='     ', font=font_1).grid(column=0, row=7, columnspan=2)
        Button(self, text='  导入文件 ', command=lambda: self.file()).grid(row=8, column=0, stick=W, pady=10,
                                                                       ipadx=6, ipady=5)
        Button(self, text='    清空    ', command=lambda: self.clear()).grid(row=8, column=1, pady=10, stick=E, ipadx=6,
                                                                         ipady=5)

    def file(self):
        filename = filedialog.askopenfilename()
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        col = sheet.col_values(0)
        # 求中位数
        col.sort()
        n = len(col)
        m = int(n / 2)
        if n == 0:
            self.median.set('None')
        elif n % 2 == 0:
            self.median.set((col(m) + col(m + 1)) / 2)
        else:
            self.median.set(col[m])
        # 求平均数
        sum = 0
        for nums in col:
            sum += nums
        self.mean.set(sum / n)
        mean = sum/n
        # print('平均数：' + str(mean))
        # 求方差
        sum_1 = 0
        for nums in col:
            sum_1 += (nums - float(self.mean.get())) ** 2
        self.variance.set(sum_1 / n)
        variance = sum_1/n
        # print('方差：' + str(variance))
        self.standard.set(variance**0.5)
        # print('标准差： ' + str(standard))
        # 求峰度偏度
        sum_2 = 0
        for nums in col:
            sum_2 += (nums - mean) ** 3
        self.kurtosis.set(sum_2 / float(self.standard.get()) ** (3/2))
        # print('偏度：' + str(kurtosis))
        sum_3 = 0
        for nums in col:
            sum_3 += (nums - mean) ** 4
        self.skewness.set(sum_3 / float(self.standard.get()) ** 4)
        # print('峰度：' + str(skewness))

    def clear(self):
        self.mean.set('')
        self.median.set('')
        self.standard.set('')
        self.variance.set('')
        self.kurtosis.set('')
        self.skewness.set('')


class Games(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        Label(self, text='').pack()
        # 创建 飞机大战 的按钮
        Button(self, text='飞机大战', command=lambda: ai.run_game()).pack(side=TOP, expand=YES, fill=BOTH, padx=4, pady=15,
                                                                      ipadx=20, ipady=10)
        # 创建 贪吃蛇 的按钮
        Button(self, text='贪吃蛇').pack(side=BOTTOM, expand=YES, fill=BOTH, padx=4, pady=15, ipadx=20, ipady=10)


    def run_alien(self):
        ai.rungame()


