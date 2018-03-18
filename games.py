from tkinter import *
from tkinter.ttk import *
import new_game_1 as ng_1


def build(main_menu):
    view_menu = Menu(main_menu, tearoff=0)
    view_menu.add_command(label='alien', command=lambda: ng_1.run_game())
    main_menu.add_cascade(label='游戏', menu=view_menu)
