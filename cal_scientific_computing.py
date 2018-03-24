from tkinter import *
from tkinter.ttk import *
import math


def exponent(x, power):
    return x**power


def square(x):
    return x*x


def reciprocal(x):
    return 1/x


def sqrt(x):
    return math.sqrt(x)


def sin(x):
    return math.sin(x*math.pi/180)


def cos(x):
    return math.cos(x*math.pi/180)


def tan(x):
    if x % 90 == 0:
        return "tan90 doesn't exist"
    else:
        return math.tan(x*math.pi/180)


def lg(x):
    return math.log(x, 10)


def ln(x):
    return math.log(x, math.pi)


def log(x, base):
    return math.log(x, base)


def calc(text):
    """用eval方法计算表达式字符串"""
    try:
        return eval(text)
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Error'

