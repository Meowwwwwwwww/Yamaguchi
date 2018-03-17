from tkinter import *
from tkinter.ttk import *


def build(main_menu):
    text = StringVar()
    sep_flag = IntVar()
    # 创建统计模块菜单
    sep_flag.set(0)
    view_menu = Menu(main_menu, tearoff=0)
    view_menu.add_checkbutton(label='Show Thousands Separator', variable=sep_flag,
                              command=lambda t=text: t.set(add_sep(t.get())))
    main_menu.add_cascade(label='金融计算', menu=view_menu)
