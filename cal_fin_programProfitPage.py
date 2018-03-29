from cal_view import *
import cal_fin_function as fin
import cal_pages
import matplotlib.pyplot as plt
import numpy as np

class program_profit_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 300))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.rate = StringVar()
        self.cashflow = StringVar()
        self.npv = StringVar()
        self.irr = StringVar()
        self.pi = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=4, column=0, stick=W)
        Label(self.page, text='单利终值计算:           ').grid(row=0, column=0, stick=W, pady=10)
        Label(self.page, text='每期利率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='现金流').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.cashflow).grid(row=2, column=1, stick=E)

        Button(self.page, text='计算', command=self.calculate).grid(row=4, column=2, stick=W, pady=10)

        Label(self.page, text='净现值').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.npv, state = 'readonly').grid(row=5, column=1, stick=E)
        Label(self.page, text='内部收益率').grid(row=6, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.irr, state='readonly').grid(row=6, column=1, stick=E)
        Label(self.page, text='盈利指数').grid(row=7, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.pi, state='readonly').grid(row=7, column=1, stick=E)
        Button(self.page, text='清除', command=self.clear).grid(row=4, column=1, stick=W, pady=10)

    def calculate(self):
        if (self.rate.get() == '' or self.cashflow.get() == ''):
            self.npv.set('缺少参数.')
            self.irr.set('缺少参数.')
            self.pi.set('缺少参数.')
            return
        try:
            rate = eval(self.rate.get())
            if rate <=0 or rate >= 1:
                return self.npv.set('每期利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.npv.set('每期利率输入错误')
        try:
            cashflow = self.cashflow.get()
            cashflow_split = cashflow.split(',')
            cashflow_eval = []
            n = 0
            m = 0
            while n < len(cashflow_split):
                component = eval(cashflow_split[n])
                if component < 0:
                    m = m + 1
                if m > 1:
                    self.npv.set('现金流输入错误')
                cashflow_eval.append(component)
                n = n + 1
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.npv.set('现金流输入错误')
        result = fin.profit_index(rate, cashflow_eval)
        self.npv.set('%.8f' %result[0])
        self.irr.set('%.8f' % result[1])
        self.pi.set('%.8f' % result[2])

    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.rate.set('')
        self.cashflow.set('')
        self.npv.set('')
        self.irr.set('')
        self.pi.set('')
