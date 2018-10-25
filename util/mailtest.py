#coding: utf-8 -*-
# @Time    : 2018/8/6 19:15
# @Author  : 留仙洞
# @FileName: mailtest.py
# @Software: PyCharm
import sys
import xlrd
import os
import turtle
class A():

    # def __init__(self):
    #     self.test_a = self.test_a()
    #
    # def test_a(self):
    #     self.m ="hello"
    #
    # def test_b(self):
    #     self.test_a
    #     n=self.m + "world"
    #     print(n)
    def a(self):
        turtle.pensize(1)
        turtle.color('red')
        turtle.fillcolor('pink')
        turtle.speed(5)
        turtle.up()
        turtle.goto(-30,100)
        turtle.down()
        turtle.begin_fill()
        turtle.left(90)
        turtle.circle(120,180)
        turtle.circle(360,70)
        turtle.left(38)
        turtle.circle(360,70)
        turtle.circle(120,180)
        turtle.end_fill()
        turtle.up()
        turtle.goto(-100,-100)
        turtle.down()
        turtle.color('red', 'yellow')
        turtle.begin_fill()
        while True:
            turtle.forward(200)
            turtle.left(170)
            if abs(turtle.pos()) < 1:
                break
        turtle.end_fill()
        turtle.done()



if __name__ == '__main__':
    # excel = xlrd.open_workbook('C:\\Users\wb.liuxiandong\Desktop\\book\\test.xlsx')
    # table = excel.sheets()[0]
    # cols = table.ncols
    # print(cols)
    # print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))
    # print(sys.path[0])
    _a = A()
    _a.a()

