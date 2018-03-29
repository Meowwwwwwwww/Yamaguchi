from cal_view import *
import numpy as np
import cal_pages
import tkinter
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp   ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import statsmodels.api as sm

class TwoOneRegression_page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (480, 700))  # 设置窗口大小
        self.root.title = 'Yamaguchi 1.0'
        self.file = StringVar()
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
        Label(self.page, text='平面截距:').grid(row=5, column=0, stick=W, pady=10)
        Entry(self.page, textvariable=self.b, width=32, state='readonly').grid(row=5, column=1,columnspan = 3, stick=E)
        Label(self.page, text='平面系数1、2:').grid(row=6, column=0, stick=W, pady=10)
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
            return self.k.set("文件输入错误!")
        xx, yy = np.meshgrid(np.linspace(0, 10, 10), np.linspace(0, 100, 10))
        zz = 1.0 * xx + 3.5 * yy + np.random.randint(0, 100, (10, 10))

        # 构建成特征、值的形式
        X, Z = np.column_stack((xx.flatten(), yy.flatten())), zz.flatten()

        # 建立线性回归模型
        regr = linear_model.LinearRegression()

        # 拟合
        regr.fit(X, Z)

        # 不难得到平面的系数、截距
        a, b = regr.coef_, regr.intercept_
        self.k.set(a)
        self.b.set(b)

        # 给出待预测的一个特征
        x = np.array([[5.8, 78.3]])

        # 方式1：根据线性方程计算待预测的特征x对应的值z（注意：np.sum）
        print(np.sum(a * x) + b)

        # 方式2：根据predict方法预测的值z
        print(regr.predict(x))

        est = sm.OLS(Z, X).fit()
        print(est.summary())

        est = sm.OLS(Z, X).fit()
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





    def financialPage(self):
        self.page.destroy()
        cal_pages.FinancialPage(self.root)

    def clear(self):
        self.file.set('')
        self.k.set('')
        self.b.set('')
        Label(self.page, text='', wraplength=450, justify='right').grid(row=9, columnspan=4)

    def plot(self):
        xx, yy = np.meshgrid(np.linspace(0, 10, 10), np.linspace(0, 100, 10))
        zz = 1.0 * xx + 3.5 * yy + np.random.randint(0, 100, (10, 10))

        # 构建成特征、值的形式
        X, Z = np.column_stack((xx.flatten(), yy.flatten())), zz.flatten()

        # 建立线性回归模型
        regr = linear_model.LinearRegression()

        # 拟合
        regr.fit(X, Z)

        # 不难得到平面的系数、截距

        # 给出待预测的一个特征
        x = np.array([[5.8, 78.3]])

        # 画图
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # 1.画出真实的点
        ax.scatter(xx, yy, zz)

        # 2.画出拟合的平面
        ax.plot_wireframe(xx, yy, regr.predict(X).reshape(10, 10))
        ax.plot_surface(xx, yy, regr.predict(X).reshape(10, 10), alpha=0.3)

        plt.show()




