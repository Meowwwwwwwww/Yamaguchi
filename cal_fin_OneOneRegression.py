from cal_view import *
import numpy as np
import cal_pages
import tkinter
import scipy as sp   ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import statsmodels.api as sm
import random

class OneOneRegression_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (480, 700))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.file = StringVar()
        self.result = StringVar()
        self.k = StringVar()
        self.b = StringVar()
        self.text = Label()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='退出', command=lambda: self.financialPage()).grid(row=7, column=3, stick=W)
        Label(self.page, text='一元一次线性回归:           ').grid(row=0, columnspan = 4, stick=W, pady=10)
        Button(self.page, text='清除', command=lambda: self.clear()).grid(row=7, column=1,stick=W)
        Label(self.page, text='请输入文件名:').grid(row=1, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.file, width=32).grid(row=2, columnspan = 4, stick=E)
        Label(self.page, text='回归方程:').grid(row=3, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.result, width=32, state='readonly').grid(row=4, column=0,columnspan = 4, stick=E)
        Label(self.page, text='纵截距:').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.b, width=32, state='readonly').grid(row=5, column=1,columnspan = 3, stick=E)
        Label(self.page, text='解释系数:').grid(row=6, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.k, width=32, state='readonly').grid(row=6, column=1,columnspan = 3, stick=E)
        Button(self.page, text='计算', command=self.calculate).grid(row=7, column=0, stick=W, pady=10)
        Button(self.page, text='画图', command=self.plot).grid(row=7, column=2, stick=W, pady=10)


    #"C:\\Users\\koshiro\\Desktop\\egression.csv"
    def calculate(self):
        try:
            Xi = []
            Yi = []
            file = open(self.file.get(), 'r')
            for line in file.readlines():
                temp = line.strip().split(",")
                Xi.append(float(temp[1]))
                Yi.append(float(temp[2]))
        except(SyntaxError, ZeroDivisionError, FileNotFoundError, FileExistsError):
            return self.result.set("文件输入错误!")
            '''
             设置样本数据，真实数据需要在这里处理
        '''

        Xi = np.array(Xi)
        Yi = np.array(Yi)
        ##样本数据(Xi,Yi)，需要转换成数组(列表)形式
        # Xi=np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])
        # Yi=np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])

        '''
            设定拟合函数和偏差函数
            函数的形状确定过程：
            1.先画样本图像
            2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
        '''

        ##需要拟合的函数func :指定函数的形状
        def func(p, x):
            k, b = p
            return k * x + b

        ##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
        def error(p, x, y):
            return func(p, x) - y

        '''
            主要部分：附带部分说明
            1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
            2.官网的原话（第二个值）：Value of the cost function at the solution
            3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
            4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
        '''

        # k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
        p0 = [1, 20]

        # 把error函数中除了p0以外的参数打包到args中(使用要求)
        Para = leastsq(error, p0, args=(Xi, Yi))

        # 读取结果
        k, b = Para[0]
        self.k.set(k)
        self.b.set(b)
        print("求解的拟合直线为:")
        self.result.set("y=" + str(round(k, 2)) + "x+" + str(round(b, 2)))

        est = sm.OLS(Yi, Xi).fit()
        f = open('result.txt', 'w')
        print(est.summary(), file = f)
        f.close()
        f = open('result.txt', 'r')
        done =0
        string1=''
        while not done:
            aline =f.readline()
            if(aline!=''):
                string1 =string1 + aline
            else:
                done = 1
        Label(self.page, text=string1, wraplength=450, justify='right').grid(row=9, columnspan=4)

        print(est.summary())





    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.file.set('')
        self.result.set('')
        self.k.set('')
        self.b.set('')
        Label(self.page, text='', wraplength=450, justify='right').grid(row=9, columnspan=4)

    def plot(self):
        Xi = [];
        Yi = []
        file = open("C:\\Users\\adminsistrator\\Desktop\\最终版\\egression.csv", 'r')
        for line in file.readlines():
            temp = line.strip().split(",")
            Xi.append(float(temp[1]) + random.randint(-10, 10))
            Yi.append(float(temp[2]) + random.randint(-10, 10))
            '''
             设置样本数据，真实数据需要在这里处理
        '''

        Xi = np.array(Xi)
        Yi = np.array(Yi)
        ##样本数据(Xi,Yi)，需要转换成数组(列表)形式
        # Xi=np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])
        # Yi=np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])

        '''
            设定拟合函数和偏差函数
            函数的形状确定过程：
            1.先画样本图像
            2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
        '''

        ##需要拟合的函数func :指定函数的形状
        def func(p, x):
            k, b = p
            return k * x + b

        ##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
        def error(p, x, y):
            return func(p, x) - y

        '''
            主要部分：附带部分说明
            1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
            2.官网的原话（第二个值）：Value of the cost function at the solution
            3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
            4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
        '''

        # k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
        p0 = [1, 20]

        # 把error函数中除了p0以外的参数打包到args中(使用要求)
        Para = leastsq(error, p0, args=(Xi, Yi))

        # 读取结果
        k, b = Para[0]
        print("k=", k, "b=", b)
        print("cost：" + str(Para[1]))
        print("求解的拟合直线为:")
        print("y=" + str(round(k, 2)) + "x+" + str(round(b, 2)))

        '''
           绘图，看拟合效果.
           matplotlib默认不支持中文，label设置中文的话需要另行设置
           如果报错，改成英文就可以
        '''

        # 画样本点
        plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
        plt.scatter(Xi, Yi, color="green", label="样本数据", linewidth=2)

        # 画拟合直线
        x = np.linspace(0, max(Xi), 1000)  ##在0-15直接画100个连续点
        y = k * x + b  ##函数式
        plt.plot(x, y, color="red", label="拟合直线", linewidth=2)
        plt.legend(loc='lower right')  # 绘制图例
        plt.show()



