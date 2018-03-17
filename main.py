from tkinter import *
from tkinter.ttk import *
import statistic as st
import finance as fn


def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


def button(master, text, command):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text, command=command)
    w['width'] = 6
    # w['height'] = 3
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w


def back(text):
    """将text最末的字符删除并返回"""
    if len(text) > 0:
        return text[:-1]
    else:
        return text


def calc(text):
    """用eval方法计算表达式字符串"""
    try:
        if (sep_flag.get() == 0):
            return eval(del_sep(text))
        else:
            return add_sep(str(eval(del_sep(text))))
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Error'


def add_sep(text):
    """向参数传入的数字串中添加千位分隔符

    这里考虑了三种情况: 无整数部份, 无小数部份, 同时有整数和小数部份
    由于字符串是不可改变的, 这里由字符串生成列表以便执行insert操作和
    extend操作, 操作完成后最由列表生成字符串返回
    """
    dot_index = text.find('.')
    if dot_index > 0:
        text_head = text[:dot_index]
        text_tail = text[dot_index:]
    elif dot_index < 0:
        text_head = text
        text_tail = ''
    else:
        text_head = ''
        text_tail = text

    list_ = [char for char in text_head]
    length = len(list_)
    tmp_index = 3
    while length - tmp_index > 0:
        list_.insert(length - tmp_index, ',')
        tmp_index += 3
    list_.extend(text_tail)
    new_text = ''
    for char in list_:
        new_text += char

    return new_text


def del_sep(text):
    """删除数字串中所有的千位分隔符"""
    return text.replace(',', '')


# 开始界面的实现
root = Tk()
root.title("Calculator")  # 添加标题

main_menu = Menu()  # 创建最上层主菜单

# 创建Calculator菜单, 并加入到主菜单
calc_menu = Menu(main_menu, tearoff=0)
calc_menu.add_command(label='Quit', command=lambda: exit())
main_menu.add_cascade(label='Calculator', menu=calc_menu)

# 创建View菜单, 并加入到主菜单
# 其中"Show Thousands Separator"菜单项是一个Checkbutton
text = StringVar()
sep_flag = IntVar()
sep_flag.set(0)
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label='Show Thousands Separator', variable=sep_flag,
                          command=lambda t=text: t.set(add_sep(t.get())))
main_menu.add_cascade(label='View', menu=view_menu)

root['menu'] = main_menu  # 将主菜单与root绑定

# 创建统计模块菜单
st.build(main_menu)
root['menu'] = main_menu

# 创建财务及金融模块菜单
fn.build(main_menu)
root['menu'] = main_menu

# 创建文本框
Entry(root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)

style = Style()
style.configure('TButton', padding=3)

# 创建第一行三个按钮
fedit = frame(root)
button(fedit, 'Backspace', lambda t=text: t.set(back(t.get())))
button(fedit, 'Clear', lambda t=text: t.set(''))
button(fedit, '±', lambda t=text: t.set('-(' + t.get() + ')'))

# 每行四个, 创建其余四行按钮
for key in ('789/', '456*', '123-', '0.=+'):
    fsymb = frame(root)
    for char in key:
        if char == '=':
            button(fsymb, char, lambda t=text: t.set(calc(t.get())))
        else:
            button(fsymb, char, lambda t=text, c=char: t.set(t.get() + c))

root.mainloop()