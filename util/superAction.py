#!/usr/bin/python
# coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: superAction.py
@time: 2018/8/5 1:03
"""
import os
from selenium.webdriver.common.by import By
import logging
import xlrd
from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from util.seleniumUtil import SeleniumUtil

class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''

    def __init__(self, founction, sheet_name):
        self.page_dir = os.path.dirname(
            os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
            # self.seleniumUtil =  # print(self.page_dir)
        self.table,self.ncols,self.nrows = self.get_excel(founction, sheet_name)

    def get_excel(self, founction, sheet_name):
        '''
        元素的定位方式
        :return:
        '''
        # 定义用例的路径
        file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # 打开Excel文件
        excel = xlrd.open_workbook(file_dir) #使用self主要是后面的方法中需要引用到
        table = excel.sheet_by_name(sheet_name)  # 打开sheet文件
        ncols = table.ncols  # 获取列数
        nrows = table.nrows  # 获取行数
        return table,ncols,nrows

    def get_page_element_locator(self, founction, sheet_name, row_index, colum_index):
        '''
        :param sheet 测试用例表中的sheet
        :param row_index 用例表中的行
        :param colum_index 用例表中的列
        :param founction 页面名字
        :return:返回定位方式和定位值
        '''
        self.get_excel(founction,sheet_name)
        locator_split = []
        element_locator_way_list = []
        element_locator_value_list = []

        locator = self.table.row_values(row_index,colum_index) #获取元素定位的列的值
        # locator_split = locator[0].split('.') #由于元素定位的方式为：page.case,所以需要将它分开
        # print(locator_split[1])
        for i in range(1,self.nrows):
            '''
           根据行数循环 ,
           如果获取到的别名和指定的别名相同，
           就存储当前行的定位值和定位方式
           '''
            element_locator_way = self.table.row_values(i,4,5)
            element_locator_value = self.table.row_values(i,5,6)
            # print( element_locator_way, element_locator_value)
            element_locator_way_list.append(element_locator_way)
            element_locator_value_list.append(element_locator_value)
        return element_locator_way_list,element_locator_value_list

    def get_locate_way(self):
        '''
        @:param locateway 定位方式
        @:param locatevalue 定位值
        :return element_locator 定位的方式
        '''

    def parse_excel(self):
        '''
        解析Excel用例
        :return:
        '''
        row_value_list = []
        all_rows_value_list = []
        # 定义用例的路径
        # file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # excel = xlrd.open_workbook(file_dir)
        # logging.info('打开' + founction + '.xlsx' + '文件')
        # # 获取sheet表名字
        # table = excel.sheet_by_name(case_name)
        # logging.info('获取用例' + case_name + '的名字')
        # # 获取列总数
        # ncols = table.ncols
        # # 获取行总数
        # nrows = table.nrows

        for row in range(1, self.nrows):
            # 列出每行所有的单元格的值
            row_values = self.table.row_values(row,0,self.ncols)

            if row_values[2] == '打开链接':
                test_data = self.table.cell_value(row,6)
                SeleniumUtil.get(test_data)
                # print(test_data)
            if row_values[2] == '导航链接':
                test_data = self.table.cell_value(row,6)
                SeleniumUtil.get(test_data)
            if row_values[2] == '输入':
                ctype = self.table.cell(row,6).ctype
                test_data = self.table.cell_value(row,6)
                if ctype != 1:
                    str(test_data)
            # if row_values[2] == '':
            # 未完待续









if __name__ == '__main__':
    # s = SuperAction().get_page_element_locator('test','Sheet1')
    # s = SuperAction().get_page_element_locator('test', 'Sheet1',2,3)
    s = SuperAction('test','Sheet1').parse_excel()
