# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 19:15
# @Author  : 留仙洞
# @FileName: mailtest.py
# @Software: PyCharm
import sys
import xlrd
import os
if __name__ == '__main__':
    excel = xlrd.open_workbook('C:\\Users\wb.liuxiandong\Desktop\\book\\test.xlsx')
    table = excel.sheets()[0]
    cols = table.ncols
    print(cols)
    print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))
    print(sys.path[0])

