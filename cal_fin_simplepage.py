from cal_view import *
import cal_fin_function as fin
import cal_pages

class simple_interest_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 270))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.rate = StringVar()
        self.pmt = StringVar()
        self.pv = StringVar()
        self.result = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=4, column=0, stick=W)
        Label(self.page, text='单利终值计算:           ').grid(row=0, column=0, stick=W, pady=10)
        Label(self.page, text='每期利率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='期数').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.pmt).grid(row=2, column=1, stick=E)
        Label(self.page, text='现值').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.pv).grid(row=3, column=1, stick=E)

        Button(self.page, text='计算', command=self.calculate).grid(row=4, column=2, stick=W, pady=10)

        Label(self.page, text='结果').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, state = 'readonly').grid(row=5, column=1, stick=E)
        Button(self.page, text='清除', command=self.clear).grid(row=4, column=1, stick=W, pady=10)

    def calculate(self):
        if (self.rate.get() == '' or self.pmt.get() == '' or self.pv.get() == ''):
            self.result.set('缺少参数.')
            return
        try:
            rate = eval(self.rate.get())
            if rate <=0 or rate >= 1:
                return self.result.set('每期利率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('每期利率输入错误')
        try:
            pmt = eval(self.pmt.get())
            if pmt <=0 :
                return self.result.set('期数输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('期数输入错误')
        try:
            pv = eval(self.pv.get())
            if pv <=0 :
                return self.result.set('现值为零、为负，再怎么努力也是白费.')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('现值输入错误')

        self.result.set(fin.simple_interest(rate, pmt, pv ))

    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.rate.set('')
        self.pmt.set('')
        self.pv.set('')
        self.result.set('')