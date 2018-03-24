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


def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
    return w


def create_button_1(root, text):
    # 创建按钮
    # 创建第三行五个按钮
    third_line = frame(root)
    button(third_line, '7', lambda t=text, c='7': t.set(t.get() + c))
    button(third_line, '8', lambda t=text, c='8': t.set(t.get() + c))
    button(third_line, '9', lambda t=text, c='9': t.set(t.get() + c))
    button(third_line, 'DEL', lambda t=text: t.set(back(t.get())))
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
