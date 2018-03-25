from tkinter import *
from tkinter.messagebox import *
from cal_view import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.username = StringVar()
        self.password = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.login_check).grid(row=3, stick=W, pady=10)
        # Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=W)
        Button(self.page, text='普通模式', command=lambda: self.ordinary_mode()).grid(row=3, column=1, stick=E)

    def login_check(self):
        name = self.username.get()
        secret = self.password.get()
        if name == '' and secret == '':
            self.page.destroy()
            ChineseVipPage(self.root)
            print(name)
            print(secret)
        else:
            print(name)
            print(secret)
            showinfo(title='错误', message='账号或密码错误！')

    def ordinary_mode(self):
        self.page.destroy()
        Ordinary(self.root)


class Ordinary(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (480, 300))  # 设置窗口大小
        self.root.title = '普通模式'
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
        calc_menu.add_command(label='VIP模式(试用)', command=lambda: main.vip_calculator())
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


class ChineseVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 380))
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
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

        self.menubar.add_command(label='基础计算', command=self.inputData)
        self.menubar.add_command(label='科学计算', command=self.queryData)
        self.menubar.add_command(label='统计计算', command=self.countData)
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
        self.aboutPage.pack()
        self.games.pack_forget()

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


class JapaneseVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 380))
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
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
        self.aboutPage.pack()
        self.games.pack_forget()

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

    def chinese(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        ChineseVipPage(self.root)

    '''def japanese(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        self.JapaneseVipPage(self.root)'''

    def english(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        EnglishVipPage(self.root)


class EnglishVipPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (385, 380))
        self.createPage()

    def createPage(self):
        self.basic_calculator = Calculator(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
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
        self.aboutPage.pack()
        self.games.pack_forget()

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

    def chinese(self):
        self.basic_calculator.pack()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.games.pack_forget()
        ChineseVipPage(self.root)

    def japanese(self):
        self.basic_calculator.pack_forget()
        self.sci_calculator.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
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
        self.createPage()

    def createPage(self):
        self.basic_calculator = InputFrame(self.root)  # 创建不同Frame
        self.sci_calculator = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.games = Games(self.root)
        self.basic_calculator.pack()  # 默认显示数据录入界面

        # 设置菜单栏
        self.menubar = Menu(self.root)
        self.menubar.add_command(label='返回', command=self.login)
        self.menubar.add_command(label='基础计算', command=self.inputData)
        self.menubar.add_command(label='科学计算', command=self.queryData)
        self.menubar.add_command(label='统计计算', command=self.countData)
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
        self.aboutPage.pack()
        self.games.pack_forget()

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
