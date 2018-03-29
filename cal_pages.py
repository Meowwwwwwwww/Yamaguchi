from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from cal_view import *
from tkinter import font
import pandas
import GreedySnake as gs
import alien_invasion as ai
import xlrd
import xlwt
from xlutils.copy import copy
import cal_fin_presentpage as calpre
import cal_fin_futurepage as calfut
import cal_fin_simplepage as calsim
import cal_fin_programProfitPage as calpro
import cal_fin_capm as calcapm
import cal_fin_security as calsec
import cal_fin_stockPage as calsto
import cal_fin_annuity as calann
import cal_fin_OneOneRegression as caloor
import cal_fin_TwoOneRegression as calwor
import random
import YiFunction as yif
import webbrowser as web


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 190))  # 设置窗口大小
        # self.root.resizable(FALSE, FALSE)
        # self.font_1 = font.Font(family='宋体', size=12, weight='bold')
        self.font_1 = font.Font(family='华文彩云', size=14, weight='bold')
        # self.root.title("Yamaguchi 1.0")
        self.username = StringVar()
        self.password = StringVar()
        self.create_page()

    def create_page(self):
        self.main_menu = Menu()
        # 创建最上层主菜单
        # 创建Calculator菜单, 并加入到主菜单
        calc_menu = Menu(self.main_menu, tearoff=0)
        calc_menu.add_command(label='退出', command=lambda: exit())
        calc_menu.add_command(label='忘记密码', command=lambda: self.forget())
        calc_menu.add_command(label='修改密码', command=lambda: self.change())
        calc_menu.add_command(label='普通模式', command=lambda: self.ordinary_mode())
        self.main_menu.add_cascade(label='菜单', menu=calc_menu)
        self.root['menu'] = self.main_menu

        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户:   ', font=self.font_1).grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码:   ', font=self.font_1).grid(row=2, stick=W, pady=15)
        # Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Entry(self.page, textvariable=self.password).grid(row=2, column=1, stick=E)
        # Button(self.page, text='    登陆    ', command=self.login_check).grid(row=3, stick=W, pady=10)
        Button(self.page, text='    登陆    ', command=self.login_check).grid(row=3, column=0, stick=W, pady=10)
        Button(self.page, text='    注册    ', command=lambda: self.register()).grid(row=3,column=1,  pady=10, stick=E)
        # Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=W)
        # Button(self.page, text=' 普通模式 ', command=lambda: self.ordinary_mode()).grid(row=3, column=1, stick=E)

    def login_check(self):
        name = self.username.get()
        secret = self.password.get()
        workbook = xlrd.open_workbook('account.xls')
        sheet = workbook.sheet_by_index(0)
        col_1 = sheet.col_values(0)
        col_2 = sheet.col_values(1)
        if name not in col_1:
            showinfo(title='错误', message='账号不存在！')
            self.username.set('')
            self.password.set('')
        elif name in col_1 and secret in col_2:
            self.page.destroy()
            ChineseVipPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')

    def ordinary_mode(self):
        self.page.destroy()
        self.main_menu.destroy()
        Ordinary(self.root)

    def register(self):
        self.page.destroy()
        self.main_menu.destroy()
        Register(self.root)

    def forget(self):
        self.page.destroy()
        self.main_menu.destroy()
        Forget(self.root)

    def change(self):
        self.page.destroy()
        self.main_menu.destroy()
        Change(self.root)


class Ordinary(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (480, 300))  # 设置窗口大小
        self.root.resizable(FALSE, FALSE)
        self.cal = StringVar()
        # self.style = Style()
        # self.style.configure('TButton', padding=3)
        self.create_page()

    def create_page(self):
        self.main_menu = Menu()
        # 创建最上层主菜单
        # 创建Calculator菜单, 并加入到主菜单
        calc_menu = Menu(self.main_menu, tearoff=0)
        calc_menu.add_command(label='退出', command=lambda: exit())
        calc_menu.add_command(label='VIP模式(试用)', command=lambda: self.vip_trial())
        calc_menu.add_command(label='返回登录界面', command=lambda: self.mainpage())
        self.main_menu.add_cascade(label='菜单', menu=calc_menu)
        self.root['menu'] = self.main_menu

        # 文本框
        self.textbox = Frame(self.root)  # 创建Frame
        self.textbox.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
        Entry(self.textbox, textvariable=self.cal).pack(expand=YES, fill=BOTH, padx=2, pady=10, ipady=15)

        # 第一行
        self.first_line = Frame(self.root)  # 创建Frame
        self.first_line.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
        Button(self.first_line, text='7', command=lambda: self.add('7')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                              , pady=2, ipadx=2, ipady=3)
        Button(self.first_line, text='8', command=lambda: self.add('8')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                              , pady=2, ipadx=2, ipady=3)
        Button(self.first_line, text='9', command=lambda: self.add('9')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                              , pady=2, ipadx=2, ipady=3)
        Button(self.first_line, text='DEL', command=lambda: self.back()).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                                , pady=2, ipadx=2, ipady=3)
        Button(self.first_line, text='AC', command=lambda: self.clear()).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)

        # 第二行
        self.second_line = Frame(self.root)
        self.second_line.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
        Button(self.second_line, text='4', command=lambda: self.add('4')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.second_line, text='5', command=lambda: self.add('5')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.second_line, text='6', command=lambda: self.add('6')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.second_line, text='*', command=lambda: self.add('*')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.second_line, text='/', command=lambda: self.add('/')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)

        # 第三行
        self.third_line = Frame(self.root)
        self.third_line.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
        Button(self.third_line, text='1', command=lambda: self.add('1')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2,
                                                                              pady=2, ipadx=2, ipady=3)
        Button(self.third_line, text='2', command=lambda: self.add('2')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.third_line, text='3', command=lambda: self.add('3')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.third_line, text='+', command=lambda: self.add('+')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.third_line, text='-', command=lambda: self.add('-')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)

        # 第四行
        self.forth_line = Frame(self.root)
        self.forth_line.pack(side=TOP, expand=YES, fill=BOTH, anchor='s')
        Button(self.forth_line, text='0', command=lambda: self.add('0')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.forth_line, text='.', command=lambda: self.add('.')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.forth_line, text='(', command=lambda: self.add('(')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2,
                                                                              pady=2, ipadx=2, ipady=3)
        Button(self.forth_line, text=')', command=lambda: self.add(')')).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)
        Button(self.forth_line, text='=', command=lambda: self.calc()).pack(side=LEFT, expand=YES, fill=BOTH, padx=2
                                                                               , pady=2, ipadx=2, ipady=3)

    def add(self, name):
        self.cal.set(self.cal.get() + name)

    def calc(self):
        """用eval方法计算表达式字符串"""
        try:
            self.cal.set(eval(self.cal.get()))
            print(1)
        except (SyntaxError, ZeroDivisionError, NameError):
            self.cal.set('Error')

    def back(self):
        if len(self.cal.get()) > 0:
            self.cal.set(self.cal.get()[:-1])
        else:
            self.cal.set(self.cal.get())

    def clear(self):
        self.cal.set('')

    def mainpage(self):
        self.first_line.destroy()
        self.second_line.destroy()
        self.third_line.destroy()
        self.forth_line.destroy()
        self.textbox.destroy()
        self.main_menu.destroy()
        LoginPage(self.root)

    def vip_trial(self):
        self.first_line.destroy()
        self.second_line.destroy()
        self.third_line.destroy()
        self.forth_line.destroy()
        self.textbox.destroy()
        self.main_menu.destroy()
        VipTrial(self.root)


class ChineseVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 380))
        # self.root.resizable(FALSE, FALSE)
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        # self.financial = FinancialPage(self.root)
        self.games = Games(self.root)
        self.basic_calculator.pack()  # 默认显示数据录入界面

        # 设置菜单栏
        self.menubar = Menu(self.root)
        calc_menu = Menu(self.menubar, tearoff=0)
        calc_menu.add_command(label='退出', command=lambda: exit())
        # calc_menu.add_command(label='中文', command=lambda: self.chinese())
        calc_menu.add_command(label='English', command=lambda: self.english())
        calc_menu.add_command(label='日本语', command=lambda: self.japanese())
        calc_menu.add_command(label='返回', command=lambda: self.login())
        self.menubar.add_cascade(label='菜单', menu=calc_menu)

        self.menubar.add_command(label='计算器', command=self.inputData)
        self.menubar.add_command(label='信息查询', command=self.queryData)
        self.menubar.add_command(label='统计分析', command=self.countData)
        self.menubar.add_command(label='财务计算', command=self.finanCial)
        self.menubar.add_command(label='易经', command=self.Yi)
        # self.menubar.add_command(label='游戏', command=self.gameS)

        game_menu = Menu(self.menubar, tearoff=0)
        game_menu.add_command(label='飞机大战', command=lambda: ai.run_game())
        game_menu.add_command(label='贪吃蛇', command=lambda: gs.main())
        self.menubar.add_cascade(label='游戏', menu=game_menu)

        self.root['menu'] = self.menubar

    def inputData(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.games.pack_forget()

    def queryData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack()
        self.countPage.pack_forget()
        self.games.pack_forget()


    def countData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack()
        self.games.pack_forget()

    def finanCial(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        FinancialPage(self.root)

    def gameS(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.games.pack()

    def login(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        LoginPage(self.root)

    '''def chinese(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        self.ChineseVipPage(self.root)'''

    def japanese(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.games.destroy()
        JapaneseVipPage(self.root)

    def english(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.games.destroy()
        EnglishVipPage(self.root)

    def Yi(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        YiPage(self.root)


class JapaneseVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 360))
        self.root.resizable(FALSE, FALSE)
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        # self.financial = FinancialPage(self.root)
        self.games = Games(self.root)
        self.basic_calculator.pack()  # 默认显示数据录入界面

        # 设置菜单栏
        self.menubar = Menu(self.root)
        calc_menu = Menu(self.menubar, tearoff=0)
        calc_menu.add_command(label='离', command=lambda: exit())
        calc_menu.add_command(label='中文', command=lambda: self.chinese())
        calc_menu.add_command(label='English', command=lambda: self.english())
        # calc_menu.add_command(label='日本语', command=lambda: self.japanese())
        calc_menu.add_command(label='戻る', command=lambda: self.login())
        self.menubar.add_cascade(label='メニュー', menu=calc_menu)

        self.menubar.add_command(label='科学計算', command=self.inputData)
        self.menubar.add_command(label='データ検索', command=self.queryData)
        self.menubar.add_command(label='統計分析', command=self.countData)
        self.menubar.add_command(label='財務計算', command=self.aboutDisp)
        self.menubar.add_command(label='ゲーム', command=self.gameS)
        self.root['menu'] = self.menubar

    def inputData(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()

    def queryData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()


    def countData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()
        self.games.pack_forget()

    def aboutDisp(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack()
        self.games.pack_forget()
        FinancialPage(self.root)

    def gameS(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack()

    def login(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        # self.aboutPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        LoginPage(self.root)

    def chinese(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        # self.aboutPage.destroy()
        self.games.destroy()
        ChineseVipPage(self.root)

    '''def japanese(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        self.JapaneseVipPage(self.root)'''

    def english(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        # self.aboutPage.destroy()
        EnglishVipPage(self.root)


class EnglishVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 360))
        self.root.resizable(FALSE, FALSE)
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        # self.aboutPage = AboutFrame(self.root)
        self.games = Games(self.root)
        self.basic_calculator.pack()  # 默认显示数据录入界面

        # 设置菜单栏
        self.menubar = Menu(self.root)
        calc_menu = Menu(self.menubar, tearoff=0)
        calc_menu.add_command(label='exit', command=lambda: exit())
        calc_menu.add_command(label='中文', command=lambda: self.chinese())
        # calc_menu.add_command(label='English', command=lambda: self.english())
        calc_menu.add_command(label='日本语', command=lambda: self.japanese())
        calc_menu.add_command(label='return', command=lambda: self.login())
        self.menubar.add_cascade(label='menu', menu=calc_menu)

        self.menubar.add_command(label='calculator', command=self.inputData)
        self.menubar.add_command(label='info query', command=self.queryData)
        self.menubar.add_command(label='statistics', command=self.countData)
        self.menubar.add_command(label='finance', command=self.aboutDisp)
        self.menubar.add_command(label='games', command=self.gameS)
        self.root['menu'] = self.menubar

    def inputData(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()

    def queryData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()


    def countData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()

    def aboutDisp(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack()
        self.games.pack_forget()
        FinancialPage(self.root)

    def gameS(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack()

    def login(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.aboutPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        LoginPage(self.root)

    def chinese(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()
        ChineseVipPage(self.root)

    def japanese(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack_forget()
        self.games.pack_forget()
        JapaneseVipPage(self.root)

    '''def english(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.EnglishVipPage(self.root)'''


class VipTrial(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 380))
        self.root.resizable(FALSE, FALSE)
        self.createPage()

    def createPage(self):
        self.basic_calculator = Trial(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        # self.aboutPage = FinancialPage(self.root)
        self.games = Games(self.root)
        self.basic_calculator.pack()  # 默认显示数据录入界面

        # 设置菜单栏
        self.menubar = Menu(self.root)
        calc_menu = Menu(self.menubar, tearoff=0)
        calc_menu.add_command(label='退出', command=lambda: exit())
        # calc_menu.add_command(label='中文', command=lambda: self.chinese())
        calc_menu.add_command(label='English')
        calc_menu.add_command(label='日本语')
        calc_menu.add_command(label='返回', command=lambda: self.login())
        self.menubar.add_cascade(label='菜单', menu=calc_menu)

        self.menubar.add_command(label='科学计算', command=self.inputData)
        self.menubar.add_command(label='信息查询', command=self.queryData)
        self.menubar.add_command(label='统计分析', command=self.countData)
        self.menubar.add_command(label='财务计算', command=self.aboutDisp)
        self.menubar.add_command(label='游戏', command=self.gameS)
        self.root['menu'] = self.menubar

    def inputData(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()

    def queryData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()


    def countData(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()
        self.games.pack_forget()

    def aboutDisp(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        # self.aboutPage.pack()
        self.games.pack_forget()
        FinancialPage(self.root)

    def gameS(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack()

    def login(self):
        self.basic_calculator.destroy()
        self.sci_calculator.destroy()
        self.countPage.destroy()
        self.aboutPage.destroy()
        self.games.destroy()
        self.menubar.destroy()
        LoginPage(self.root)

    '''def chinese(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        self.ChineseVipPage(self.root)'''

    def japanese(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        JapaneseVipPage(self.root)

    def english(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        EnglishVipPage(self.root)


class Register(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (275, 375))
        self.root.resizable(FALSE, FALSE)
        self.nickname = StringVar()
        self.email_address = StringVar()
        self.password = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.city = StringVar()
        self.name = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='注册界面').grid(column=0, row=0, columnspan=2)
        Label(self.page, text='账户名:   ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.nickname).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码:      ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password).grid(row=2, column=1, stick=E)
        Label(self.page, text='电子邮箱:   ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.email_address).grid(row=3, column=1, stick=E)
        Label(self.page, text='姓名:   ').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.name).grid(row=4, column=1, stick=E)
        Label(self.page, text='性别:   ').grid(row=5, stick=W, pady=10)
        Entry(self.page, textvariable=self.gender).grid(row=5, column=1, stick=E)
        Label(self.page, text='年龄:   ').grid(row=6, stick=W, pady=10)
        Entry(self.page, textvariable=self.age).grid(row=6, column=1, stick=E)
        Label(self.page, text='所在城市:   ').grid(row=7, stick=W, pady=10)
        Entry(self.page, textvariable=self.city).grid(row=7, column=1, stick=E)
        Button(self.page, text='    注册    ', command=lambda: self.register()).grid(row=8, column=0, stick=W, pady=10)
        Button(self.page, text='    返回    ', command=lambda: self.login_page()).grid(row=8, column=1, pady=10, stick=E)

    def register(self):
        workbook = xlrd.open_workbook('account.xls')
        sheet = workbook.sheet_by_index(0)
        cols = sheet.col_values(0)
        if self.password.get() == '':
            showinfo(title='错误', message='密码不能为空！')
        elif self.nickname.get() not in cols:
            old_excel = xlrd.open_workbook('account.xls')
            sheet = old_excel.sheet_by_index(0)
            new_excel = copy(old_excel)
            ws = new_excel.get_sheet(0)
            ws.write(sheet.nrows, 0, str(self.nickname.get()))
            ws.write(sheet.nrows, 1, str(self.password.get()))
            ws.write(sheet.nrows, 2, str(self.email_address.get()))
            ws.write(sheet.nrows, 3, str(self.name.get()))
            ws.write(sheet.nrows, 4, str(self.gender.get()))
            ws.write(sheet.nrows, 5, str(self.age.get()))
            ws.write(sheet.nrows, 6, str(self.city.get()))
            cols = sheet.col_values(0)
            new_excel.save('account.xls')
            showinfo(title='', message='注册成功！')
            self.page.destroy()
            LoginPage(self.root)
        else:
            showinfo(title='错误', message='账号已存在！')

    def login_page(self):
        self.page.destroy()
        LoginPage(self.root)


class Forget(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (300, 350))  # 设置窗口大小
        self.root.resizable(FALSE, FALSE)
        self.root.title = 'Yamaguchi 1.0'
        self.nickname = StringVar()
        self.email_address = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.city = StringVar()
        self.name = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='密码找回界面').grid(column=0, row=0, columnspan=2)
        Label(self.page, text='账户名:   ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.nickname).grid(row=1, column=1, stick=E)
        Label(self.page, text='电子邮箱:      ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.email_address).grid(row=2, column=1, stick=E)
        Label(self.page, text='姓名:   ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.name).grid(row=3, column=1, stick=E)
        Label(self.page, text='性别:   ').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.gender).grid(row=4, column=1, stick=E)
        Label(self.page, text='年龄:   ').grid(row=5, stick=W, pady=10)
        Entry(self.page, textvariable=self.age).grid(row=5, column=1, stick=E)
        Label(self.page, text='所在城市:   ').grid(row=6, stick=W, pady=10)
        Entry(self.page, textvariable=self.city).grid(row=6, column=1, stick=E)
        Button(self.page, text='  找回密码 ', command=lambda: self.find()).grid(row=7, column=0, stick=W, pady=10)
        Button(self.page, text='    返回    ', command=lambda: self.login_page()).grid(row=7, column=1, pady=10, stick=E)

    def find(self):
        data = pandas.read_excel('./account.xls', index_col='name')
        workbook = xlrd.open_workbook('account.xls')
        sheet = workbook.sheet_by_index(0)
        cols_nickname = sheet.col_values(0)
        cols_email = sheet.col_values(2)
        cols_name = sheet.col_values(3)
        cols_gender = sheet.col_values(4)
        cols_age = sheet.col_values(5)
        cols_city = sheet.col_values(6)
        if self.nickname.get() in cols_nickname and self.email_address.get() in cols_email and \
                        self.name.get() in cols_name and self.gender.get() in cols_gender and \
                        self.age.get() in cols_age and self.city.get() in cols_city:
            self.page.destroy()
            LoginPage(self.root)
            showinfo(title='找回成功', message='你的密码是  ' + str(data.loc[self.nickname.get(), 'password']))
        else:
            showinfo(title='错误', message='信息有误')

    def login_page(self):
        self.page.destroy()
        LoginPage(self.root)


class Change(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 167))  # 设置窗口大小
        self.root.resizable(FALSE, FALSE)
        self.username = StringVar()
        self.password = StringVar()
        self.new_password = StringVar()
        self.repeat_password = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page_2 = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户:   ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码:   ').grid(row=2, stick=W, pady=15)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        # Button(self.page, text='    登陆    ', command=self.login_check).grid(row=3, stick=W, pady=10)
        Button(self.page, text='    验证    ', command=self.login_check).grid(row=3, column=0, stick=W, pady=10)
        Button(self.page, text='    返回    ', command=lambda: self.login_page()).grid(row=3, column=1,  pady=10, stick=E)

    def login_check(self):
        name = self.username.get()
        secret = self.password.get()
        workbook = xlrd.open_workbook('account.xls')
        sheet = workbook.sheet_by_index(0)
        col_1 = sheet.col_values(0)
        col_2 = sheet.col_values(1)
        if name not in col_1:
            showinfo(title='错误', message='账号不存在！')
            self.username.set('')
            self.password.set('')
        elif name in col_1 and secret in col_2:
            self.page.destroy()
            self.page_2.pack()
            Label(self.page_2).grid(row=0, stick=W)
            Label(self.page_2, text='新密码:   ').grid(row=1, stick=W, pady=10)
            Entry(self.page_2, textvariable=self.new_password).grid(row=1, column=1, stick=E)
            Label(self.page_2, text='重复密码:   ').grid(row=2, stick=W, pady=10)
            Entry(self.page_2, textvariable=self.repeat_password).grid(row=2, column=1, stick=E)
            Button(self.page_2, text='    确定    ', command=lambda: self.change()).grid(row=3, column=0, stick=W, pady=10)
            Button(self.page_2, text='    返回    ', command=lambda: self.login_page()).grid(row=3, column=1, pady=10,
                                                                                           stick=E)
        else:
            showinfo(title='错误', message='账号或密码错误！')

    def login_page(self):
        self.page.destroy()
        self.page_2.destroy()
        LoginPage(self.root)

    def change(self):
        if self.new_password.get() == self.repeat_password.get():
            old_excel = xlrd.open_workbook('account.xls')
            sheet = old_excel.sheet_by_index(0)
            new_excel = copy(old_excel)
            ws = new_excel.get_sheet(0)
            cols = sheet.col_values(0)
            i = 0
            for name in cols:
                if name != 'a':
                    i += 1
                else:
                    break
            ws.write(i-1, 1, str(self.new_password.get()))
            new_excel.save('account.xls')
            showinfo(title='', message='修改成功！')
            self.page.destroy()
            self.page_2.destroy()
            LoginPage(self.root)
        else:
            showinfo(title='错误', message='两次输入不一致！')
            self.new_password.set('')
            self.repeat_password.set('')


class FinancialPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (400, 330))  # 设置窗口大小
        self.font_1 = font.Font(family='华文彩云', size=15, weight='bold')
        self.create_page()

    def create_page(self):
        self.menubar = Menu(self.root)
        self.menubar.add_command(label='返回', command=self.Vip_Page)
        self.root['menu'] = self.menubar
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        # Button(self.page, text='退出', command=lambda: self.Vip_Page()).grid(row=0, column=0, stick=W)
        Label(self.page, text='  财务函数:', font=self.font_1).grid(row=0, stick=W, pady=10, column=1)
        Button(self.page, text='现值计算', command=self.present).grid(row=1, column=0, stick=W, pady=10, padx=12)
        Button(self.page, text='复利终值计算', command=self.future).grid(row=1, column=1, stick=W, pady=10, padx=12)
        Button(self.page, text='单利终值计算', command=self.simple).grid(row=1, column=2, stick=W, pady=10, padx=12)
        Button(self.page, text='项目盈利指标', command=self.profit).grid(row=2, column=2, stick=W, pady=10, padx=12)
        Button(self.page, text='资本资产定价', command=self.capm).grid(row=2, column=0, stick=W, pady=10, padx=12)
        Button(self.page, text='股利折现模型', command=self.stock).grid(row=2, column=1, stick=W, pady=10, padx=12)
        Button(self.page, text='债券定价模型', command=self.security).grid(row=4, column=0, pady=10, columnspan=2)
        Button(self.page, text='年金现值计算', command=self.annuity).grid(row=4, column=1, pady=10, columnspan=2)
        Label(self.page, text=' 计量函数: ', font=self.font_1).grid(row=3, pady=10, column=1)
        Button(self.page, text='一元一次线性回归', command=self.OOregre).grid(row=5, column=0, pady=10, columnspan=2)
        Button(self.page, text='二元一次线性回归', command= self.Oregre).grid(row=5, column=1, pady=10, columnspan=2)

    def present(self):
        self.page.destroy()
        self.menubar.destroy()
        calpre.Present_value_page(self.root)

    def future(self):
        self.page.destroy()
        self.menubar.destroy()
        calfut.future_value_page(self.root)

    def simple(self):
        self.page.destroy()
        self.menubar.destroy()
        calsim.simple_interest_page(self.root)

    def profit(self):
        self.page.destroy()
        self.menubar.destroy()
        calpro.program_profit_page(self.root)

    def capm(self):
        self.page.destroy()
        self.menubar.destroy()
        calcapm.capm_page(self.root)

    def stock(self):
        self.page.destroy()
        self.menubar.destroy()
        calsto.capm_page(self.root)

    def security(self):
        self.page.destroy()
        self.menubar.destroy()
        calsec.capm_page(self.root)

    def annuity(self):
        self.page.destroy()
        self.menubar.destroy()
        calann.capm_page(self.root)

    def OOregre(self):
        self.page.destroy()
        self.menubar.destroy()
        caloor.OneOneRegression_page(self.root)

    def Oregre(self):
        self.page.destroy()
        self.menubar.destroy()
        calwor.TwoOneRegression_page(self.root)

    def Vip_Page(self):
        self.page.destroy()
        self.menubar.destroy()
        ChineseVipPage(self.root)


class YiPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (420, 500))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.Vip_Page()).grid(row=1, column=1, stick=W)
        Label(self.page, text='易经分析: ').grid(row=0, stick=W, pady=10)
        Button(self.page, text='开始', command=lambda: self.Analyse()).grid(row=1, column=0, stick=W)

    def Vip_Page(self):
        self.page.destroy()
        ChineseVipPage(self.root)

    def Analyse(self):
        text = yif.Getguaxiang()
        text_con = text[12]
        del text[12]
        gua_real = yif.decoding(text)
        Label(self.page, text=text[0]).grid(row=3, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[6]).grid(row=3, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[1]).grid(row=4, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[7]).grid(row=4, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[2]).grid(row=5, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[8]).grid(row=5, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[3]).grid(row=6, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[9]).grid(row=6, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[4]).grid(row=7, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[10]).grid(row=7, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[5]).grid(row=8, column=0, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=text[11]).grid(row=8, column=1, stick=W, pady=3, ipadx = 10)
        Label(self.page, text=gua_real[0]).grid(row=9, column=0, stick=W, pady=3, ipadx=10)
        Label(self.page, text=gua_real[1]).grid(row=9, column=1, stick=W, pady=3, ipadx=10)
        Button(self.page, text='解本卦', command=lambda :self.explain(gua_real[2])).grid(row=10, column=0, stick=W, pady=3, ipadx=10)
        Button(self.page, text='解之卦', command=lambda :self.explain(gua_real[3])).grid(row=10, column=1, stick=W, pady=3, ipadx=10)
        Label(self.page, text='').grid(row=11, column=0, columnspan=2, stick=W, pady=3, ipadx=10)
        Label(self.page, text=text_con).grid(row=12, column=0, columnspan = 2, stick=W, pady=3, ipadx=10)


    def explain(self, text):
        web.open(text, new = 0, autoraise=True)
