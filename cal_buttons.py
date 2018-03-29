from tkinter import *
from tkinter.ttk import *
import cal_scientific_computing as sc


def back(text):
    """将text最末的字符删除并返回"""
    if len(text) > 0:
        return text[:-1]
    else:
        return text


def button(master, text, command):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text, command=command)
    w['width'] = 6
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2, ipadx=8, ipady=6)
    return w


def button_trial(master, text):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text)
    w['width'] = 6
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2, ipadx=8, ipady=6)
    return w


def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
    return w


def create_vip_button(root, text):
    # 创建第一行六个按钮
    first_line = frame(root)
    # button(first_line, 'X^', lambda t=text: t.set(sc.cos(float(t.get())))) # 待修改
    button(first_line, 'lg', lambda t=text: t.set((sc.lg(float(t.get())))))
    button(first_line, 'X^(-1)', lambda t=text: t.set(sc.reciprocal(float(t.get()))))
    button(first_line, 'X^0.5', lambda t=text: t.set(sc.sqrt(float(t.get()))))
    button(first_line, 'X^2', lambda t=text: t.set(sc.square(float(t.get()))))
    # button(first_line, '(', lambda t=text, c='(': t.set(t.get() + c))
    # button(first_line, ')', lambda t=text, c=')': t.set(t.get() + c))

    # 创建第二行六个按钮
    second_line = frame(root)
    # button(second_line, 'log', lambda t=text: t.set(bf.back(t.get()))) # 待修改
    # button(second_line, 'lg', lambda t=text: t.set((sc.lg(float(t.get())))))
    button(second_line, 'ln', lambda t=text: t.set(sc.ln(float(t.get()))))
    button(second_line, 'sin', lambda t=text: t.set(sc.sin(float(t.get()))))
    button(second_line, 'cos', lambda t=text: t.set(sc.cos(float(t.get()))))
    button(second_line, 'tan', lambda t=text: t.set(sc.tan(float(t.get()))))

    '''ew_line = frame(root)
    button(new_line, 'ln', lambda t=text: t.set(sc.ln(float(t.get()))))
    button(new_line, 'arcsin', lambda t=text: t.set(sc.sin(float(t.get()))))
    button(new_line, 'arccos', lambda t=text: t.set(sc.cos(float(t.get()))))
    button(new_line, 'arctan', lambda t=text: t.set(sc.tan(float(t.get()))))'''

    # 创建第三行五个按钮
    third_line = frame(root)
    button(third_line, '7', lambda t=text, c='7': t.set(t.get() + c))
    button(third_line, '8', lambda t=text, c='8': t.set(t.get() + c))
    button(third_line, '9', lambda t=text, c='9': t.set(t.get() + c))
    button(third_line, 'DEL', lambda t=text: t.set(bf.back(t.get())))
    button(third_line, 'AC', lambda t=text: t.set(''))

    # 创建第四行五个按钮
    forth_line = frame(root)
    button(forth_line, '4', lambda t=text, c='4': t.set(t.get() + c))
    button(forth_line, '5', lambda t=text, c='5': t.set(t.get() + c))
    button(forth_line, '6', lambda t=text, c='6': t.set(t.get() + c))
    button(forth_line, '*', lambda t=text, c='*': t.set(t.get() + c))
    button(forth_line, '/', lambda t=text, c='/': t.set(t.get() + c))

    # 创建第五行五个按钮
    fifth_line = frame(root)
    button(fifth_line, '1', lambda t=text, c='1': t.set(t.get() + c))
    button(fifth_line, '2', lambda t=text, c='2': t.set(t.get() + c))
    button(fifth_line, '3', lambda t=text, c='3': t.set(t.get() + c))
    button(fifth_line, '+', lambda t=text, c='+': t.set(t.get() + c))
    button(fifth_line, '-', lambda t=text, c='-': t.set(t.get() + c))

    # 创建第六行五个按钮
    sixth_line = frame(root)
    button(sixth_line, '0', lambda t=text, c='0': t.set(t.get() + c))
    button(sixth_line, '.', lambda t=text, c='.': t.set(t.get() + c))
    button(sixth_line, '(', lambda t=text, c='(': t.set(t.get() + c))
    button(sixth_line, ')', lambda t=text, c=')': t.set(t.get() + c))
    button(sixth_line, '=', lambda t=text: t.set(sc.calc(t.get())))


def create_trial_button(root, text):
    # 创建第一行六个按钮
    first_line = frame(root)
    button_trial(first_line, 'lg')
    button_trial(first_line, 'X^(-1)')
    button_trial(first_line, 'X^0.5')
    button_trial(first_line, 'X^2')

    # 创建第二行六个按钮
    second_line = frame(root)
    button_trial(second_line, 'ln')
    button_trial(second_line, 'sin')
    button_trial(second_line, 'cos')
    button_trial(second_line, 'tan')

    # 创建第三行五个按钮
    third_line = frame(root)
    button_trial(third_line, '7')
    button_trial(third_line, '8')
    button_trial(third_line, '9')
    button_trial(third_line, 'DEL')
    button_trial(third_line, 'AC')

    # 创建第四行五个按钮
    forth_line = frame(root)
    button_trial(forth_line, '4')
    button_trial(forth_line, '5')
    button_trial(forth_line, '6')
    button_trial(forth_line, '*')
    button_trial(forth_line, '/')

    # 创建第五行五个按钮
    fifth_line = frame(root)
    button_trial(fifth_line, '1')
    button_trial(fifth_line, '2')
    button_trial(fifth_line, '3')
    button_trial(fifth_line, '+')
    button_trial(fifth_line, '-')

    # 创建第六行五个按钮
    sixth_line = frame(root)
    button_trial(sixth_line, '0')
    button_trial(sixth_line, '.')
    button_trial(sixth_line, '(')
    button_trial(sixth_line, ')')
    button_trial(sixth_line, '=')


def create_financial_button(root):
    first = frame(root)
    second = frame(root)
    third = frame(root)
    fourth = frame(root)
    Label(first, text='财务函数: ').pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2, ipadx=8, ipady=6)
    Button(first, text='现值计算', command=self.present).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                               ipadx=8, ipady=6)
    Button(first, text='复利终值计算', command=self.future).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                ipadx=8, ipady=6)
    Button(first, text='单利终值计算', command=self.simple).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                ipadx=8, ipady=6)
    Button(second, text='项目盈利指标', command=self.profit).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                 ipadx=8, ipady=6)
    Button(second, text='资本资产定价', command=self.capm).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                               ipadx=8, ipady=6)
    Button(second, text='股利折现模型', command=self.stock).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                ipadx=8, ipady=6)
    Button(third, text='债券定价模型', command=self.security).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                  ipadx=8, ipady=6)
    Button(third, text='年金现值计算', command=self.annuity).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                 ipadx=8, ipady=6)
    Label(fourth, text='计量函数: ').pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2, ipadx=8, ipady=6)
    Button(fourth, text='一元一次线性回归', command=self.OOregre).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                    ipadx=8, ipady=6)
    Button(fourth, text='二元一次线性回归', command=self.Oregre).pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2,
                                                                   ipadx=8, ipady=6)


def present():
    page.destroy()
    calpre.Present_value_page(root)

def future():
    self.page.destroy()
    calfut.future_value_page(root)

def simple(self):
    self.page.destroy()
    calsim.simple_interest_page(self.root)

def profit(self):
    self.page.destroy()
    calpro.program_profit_page(self.root)

def capm(self):
    self.page.destroy()
    calcapm.capm_page(self.root)

def stock(self):
    self.page.destroy()
    calsto.capm_page(self.root)

def security(self):
    self.page.destroy()
    calsec.capm_page(self.root)

def annuity(self):
    self.page.destroy()
    calann.capm_page(self.root)

def OOregre(self):
    self.page.destroy()
    caloor.OneOneRegression_page(self.root)

def Oregre(self):
    self.page.destroy()
    calwor.TwoOneRegression_page(self.root)

def Vip_Page(self):
    self.page.destroy()
    ChineseVipPage(self.root)