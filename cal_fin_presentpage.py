from cal_view import *
import numpy as np
import cal_pages

class Present_value_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 300))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.rate = StringVar()
        self.nper = StringVar()
        self.pmt = StringVar()
        self.fv = StringVar()
        self.result = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=5, column=0, stick=W)
        Label(self.page, text='现值计算:           ').grid(row=0, stick=W, pady=10)
        Label(self.page, text='每期利率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='期数').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.nper).grid(row=2, column=1, stick=E)
        Label(self.page, text='每期数额').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.pmt).grid(row=3, column=1, stick=E)
        Label(self.page, text='终值').grid(row=4, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.fv).grid(row=4, column=1, stick=E)

        Button(self.page, text='计算', command=self.calculate).grid(row=5, column=2, stick=W, pady=10)

        Label(self.page, text='结果').grid(row=6, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, state = 'readonly').grid(row=6, column=1, stick=E)
        Button(self.page, text='清除', command=self.clear).grid(row=5, column=1, stick=W, pady=10)

    def calculate(self):
        if(self.rate.get()=='' or self.nper.get()=='' or self.pmt.get()=='' or self.fv.get()==''):
            self.result.set('missing variable.')
            return
        try:
            rate = eval(self.rate.get())
            if rate <=0 or rate >= 1:
                return self.result.set('每期利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('每期利率输入错误')
        try:
            nper = eval(self.nper.get())
            if nper <=0 :
                return self.result.set('期数输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('期数输入错误')
        try:
            pmt = eval(self.pmt.get())
            if pmt <=0 :
                return self.result.set('每期数额输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('每期数额输入错误')
        try:
            fv = eval(self.fv.get())
            if fv <=0 :
                return self.result.set('终值小于等于零，投资有何意义')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('终值输入错误')

        self.result.set('%.8f'%np.pv(rate, nper, pmt, fv, when = 'end'))

    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.rate.set('')
        self.nper.set('')
        self.pmt.set('')
        self.fv.set('')
        self.result.set('')