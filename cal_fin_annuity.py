from cal_view import *
import cal_pages

class capm_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (385, 400))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.rate = StringVar()
        self.nper = StringVar()
        self.pmt = StringVar()
        self.grow = StringVar()
        self.result = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=5, column=0, stick=W)
        Label(self.page, text='年金现值计算:           ').grid(row=0, stick=W, pady=10)
        Label(self.page, text='每期收益率').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.rate).grid(row=1, column=1, stick=E)
        Label(self.page, text='期数').grid(row=2, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.nper).grid(row=2, column=1, stick=E)
        Label(self.page, text='每期所得').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.pmt).grid(row=3, column=1, stick=E)
        Label(self.page, text='收益增长率').grid(row=4, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.grow).grid(row=4, column=1, stick=E)
        Button(self.page, text='清除', command=lambda: self.clear()).grid(row=5, column=1, stick=W)

        Button(self.page, text='计算', command=self.calculate).grid(row=5, column=2, stick=W, pady=10)

        Label(self.page, text='结果').grid(row=6, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, state = 'readonly').grid(row=6, column=1, stick=E)

    def calculate(self):
        if(self.rate.get()=='' or self.pmt.get()==''):
            self.result.set('missing variable.')
            return
        try:
            rate = eval(self.rate.get())
            if rate <=0 or rate >= 1:
                return self.result.set('每期收益率输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('每期收益率输入错误')
        try:
            pmt = eval(self.pmt.get())
            if pmt <=0:
                return self.result.set('期数输入错误')
        except (SyntaxError, ZeroDivisionError, NameError):
            return self.result.set('期数输入错误')
        if(self.grow.get()=='' and self.nper.get()==''):
            self.result.set('%.8f'%(pmt /  rate))
            return
        if (self.grow.get() == ''):
            try:
                nper = eval(self.nper.get())
                if pmt <= 0:
                    return self.result.set('每期所得输入错误')
            except (SyntaxError, ZeroDivisionError, NameError):
                return self.result.set('每期所得输入错误')
            self.result.set('%.8f' % (pmt / rate * (1 - 1 * (1 + rate)**-nper)))
            return
        if (self.nper.get() == ''):
            try:
                grow = eval(self.grow.get())
                if grow <= 0 or grow >= 1:
                    return self.result.set('收益增长率输入错误')
            except (SyntaxError, ZeroDivisionError, NameError):
                return self.result.set('收益增长率输入错误')
            if grow >= rate:
                self.result.set("赶快去买这个年金！！！")
                return
            self.result.set('%.8f' % (pmt / (rate - grow)))
            return
        grow = eval(self.grow.get())
        nper = eval(self.nper.get())
        if grow >= rate:
            self.result.set("赶快去买这个年金！！！")
            return
        self.result.set('%.8f'%(pmt / (rate - grow)*(1 - ((1 + grow) / (1 + rate))**nper)))

    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.rate.set('')
        self.nper.set('')
        self.pmt.set('')
        self.grow.set('')
        self.result.set('')