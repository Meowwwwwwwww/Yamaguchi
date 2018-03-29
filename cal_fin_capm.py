from cal_view import *
import numpy as np
import cal_pages
import matplotlib.pyplot as plt

class capm_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 335))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.market_rate = StringVar()
        self.secure_rate = StringVar()
        self.beta = StringVar()
        self.result = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=4, column=0, stick=W)
        Label(self.page, text='CAPM计算:           ').grid(row=0, column=0, stick=W, pady=10)
        Label(self.page, text='市场利率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.market_rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='无风险利率').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.secure_rate).grid(row=2, column=1, stick=E)
        Label(self.page, text='β系数').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.beta).grid(row=3, column=1, stick=E)
        Button(self.page, text='清除', command=lambda: self.clear()).grid(row=7, column=0, stick=W)

        Button(self.page, text='计算', command=self.calculate).grid(row=4, column=1, stick=W, pady=10)

        Label(self.page, text='CAPM模型（SML）方程:').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, state='readonly', width = 32).grid(row=6, stick=E)
        Button(self.page, text='画图', command=self.plot).grid(row=7, column=1, stick=W, pady=10)




    def calculate(self):
        try:
            mart = eval(self.market_rate.get())
            if mart <=0 or mart >= 1:
                return self.result.set('市场利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('市场利率输入错误')
        try:
            sert = eval(self.secure_rate.get())
            if sert <=0 or sert >= 1:
                return self.result.set('无风险利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('无风险利率输入错误')
        try:
            beta = eval(self.beta.get())
            if beta <=0 :
                return self.result.set('β系数输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('β系数输入错误')
        if (self.market_rate.get() == '' or self.secure_rate.get() == ''or self.beta.get() == ''):
            self.result.set('missing variable.')
            return
        premium = mart - sert
        Ri = sert + beta * premium
        if premium <= 0:
            self.result.set('市场是有风险的！')
            return
        self.result.set("Ri = %.2f + %.2f * (%.2f - %.2f) = %.2f " %(sert, beta, mart, sert, Ri))


    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.market_rate.set('')
        self.secure_rate.set('')
        self.beta.set('')
        self.result.set('')

    def plot(self):
        try:
            mart = eval(self.market_rate.get())
            if mart <= 0 or mart >= 1:
                return self.result.set('市场利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('市场利率输入错误')
        try:
            sert = eval(self.secure_rate.get())
            if sert <= 0 or sert >= 1:
                return self.result.set('无风险利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('无风险利率输入错误')
        try:
            beta = eval(self.beta.get())
            if beta <= 0:
                return self.result.set('β系数输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('β系数输入错误')
        if (self.market_rate.get() == '' or self.secure_rate.get() == '' or self.beta.get() == ''):
            self.result.set('missing variable.')
            return
        premium = mart - sert
        if premium <= 0:
            self.result.set('市场是有风险的！')
            return
        x = np.arange(-0.2, 1, 0.05)
        y = sert + (x) * premium
        plt.grid()
        plt.xlabel('β value')
        plt.ylabel('Interest rate')
        plt.plot(x, y)
        plt.show()