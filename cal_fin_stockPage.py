from cal_view import *
import cal_fin_function as fin
import cal_pages

class capm_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 270))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.rate = StringVar()
        self.div0 = StringVar()
        self.grow = StringVar()
        self.result = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=4, column=0, stick=W)
        Label(self.page, text='现值计算:           ').grid(row=0, stick=W, pady=10)
        Label(self.page, text='每期折现率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='第0期股利').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.div0).grid(row=2, column=1, stick=E)
        Label(self.page, text='股利增长率').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.grow).grid(row=3, column=1, stick=E)
        Button(self.page, text='清除', command=lambda: self.clear()).grid(row=4, column=1, stick=W)

        Button(self.page, text='计算', command=self.calculate).grid(row=4, column=2, stick=W, pady=10)

        Label(self.page, text='结果').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, state = 'readonly').grid(row=5, column=1, stick=E)

    def calculate(self):
        try:
            rate = eval(self.rate.get())
            if rate <=0 or rate >= 1:
                return self.result.set('每期折现率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('每期折现率输入错误')
        try:
            div0 = eval(self.div0.get())
            if div0 <=0 :
                return self.result.set('买这种股票有意思吗？')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('第0期股利输入错误')
        if(self.rate.get()=='' or self.div0.get()==''):
            self.result.set('缺少参数.')
            return
        try:
            grow = eval(self.grow.get())
            if grow <=0 or grow >=1:
                return self.result.set('股利增长率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('%.8f'%(div0  /  rate))
        if grow >= rate:
            self.result.set("赶快去买这支股票！！！")
            return
        self.result.set('%.8f'%(div0 * (1 + grow) / ( rate - grow)))

    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.rate.set('')
        self.div0.set('')
        self.grow.set('')
        self.result.set('')