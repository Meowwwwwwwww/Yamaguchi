from tkinter import *
from tkinter.ttk import *

import main


def create_menu(root):
    main_menu = Menu()
    # 创建最上层主菜单

    # 创建Calculator菜单, 并加入到主菜单
    calc_menu = Menu(main_menu, tearoff=0)
    calc_menu.add_command(label='退出', command=lambda: exit())
    calc_menu.add_command(label='风格1', command=lambda: exit())
    calc_menu.add_command(label='风格2', command=lambda: exit())
    calc_menu.add_command(label='VIP模式(试用)', command=lambda: exit())
    calc_menu.add_command(label='VIP模式', command=lambda: main.vip_calculator())
    main_menu.add_cascade(label='Calculator', menu=calc_menu)
    root['menu'] = main_menu


def create_vip_menu(root):
    main_menu = Menu()
    # 创建最上层主菜单

    # 创建Calculator菜单, 并加入到主菜单
    calc_menu = Menu(main_menu, tearoff=0)
    calc_menu.add_command(label='Quit', command=lambda: exit())
    main_menu.add_cascade(label='Calculator', menu=calc_menu)
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
