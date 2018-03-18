from tkinter import *
from tkinter.ttk import *
import menus
import buttons
import button_functions as bf
import statistic as st
import finance as fn
import games


def button(master, text, command):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text, command=command,)
    w['width'] = 5
    # w['height'] = 3
    w.pack(side=LEFT, expand=YES,fill=BOTH, padx=3, pady=2, ipadx=12, ipady=6)
    return w


def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
    return w


def calc(text):
    """用eval方法计算表达式字符串"""
    try:
        if (sep_flag.get() == 0):
            return eval(text)
        else:
            return add_sep(str(eval(text)))
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Errorrrr'


# 开始界面的实现
root = Tk()
root.title("Yamaguchi 1.0")  # 添加标题

text = StringVar()
main_menu = Menu()
# 创建最上层主菜单

# 创建Calculator菜单, 并加入到主菜单
calc_menu = Menu(main_menu, tearoff=0)
calc_menu.add_command(label='Quit', command=lambda: exit())
main_menu.add_cascade(label='Calculator', menu=calc_menu)

# 创建View菜单, 并加入到主菜单
# 其中"Show Thousands Separator"菜单项是一个Checkbutton
sep_flag = IntVar()
sep_flag.set(0)
view_menu = Menu(main_menu, tearoff=0)
'''view_menu.add_checkbutton(label='Show Thousands Separator', variable=sep_flag,
                          command=lambda t=text: t.set(add_sep(t.get())))'''
main_menu.add_cascade(label='View', menu=view_menu)
root['menu'] = main_menu  # 将主菜单与root绑定

# 创建统计模块菜单
st.build(main_menu)
root['menu'] = main_menu

# 创建金融模块菜单
fn.build(main_menu)
root['menu'] = main_menu

# 创建游戏模块菜单
games.build(main_menu)
root['menu'] = main_menu

# 创建文本框
Entry(root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)

style = Style()
style.configure('TButton', padding=3)

# 创建按钮
# buttons.create_button(root)
# 创建第一行六个按钮
first_line = frame(root)
button(first_line, 'X^', lambda t=text: t.set(bf.back(t.get())))
button(first_line, 'X^(-1)', lambda t=text: t.set(''))
button(first_line, 'X^0.5', lambda t=text: t.set('-(' + t.get() + ')'))
button(first_line, 'X^2', lambda t=text: t.set('-(' + t.get() + ')'))
button(first_line, '(', lambda t=text: t.set('-(' + t.get() + ')'))
button(first_line, ')', lambda t=text: t.set('-(' + t.get() + ')'))

# 创建第二行六个按钮
second_line = frame(root)
button(second_line, 'log', lambda t=text: t.set(bf.back(t.get())))
button(second_line, 'lg', lambda t=text: t.set(''))
button(second_line, 'ln', lambda t=text: t.set('-(' + t.get() + ')'))
button(second_line, 'sin', lambda t=text: t.set('-(' + t.get() + ')'))
button(second_line, 'cos', lambda t=text: t.set('-(' + t.get() + ')'))
button(second_line, 'tan', lambda t=text: t.set('-(' + t.get() + ')'))

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
button(sixth_line, '*x10', lambda t=text, c='x10': t.set(t.get() + c))
button(sixth_line, 'Ans', lambda t=text, c='Ans': t.set(t.get() + c))
button(sixth_line, '=', lambda t=text: t.set(calc(t.get())))

root.mainloop()

