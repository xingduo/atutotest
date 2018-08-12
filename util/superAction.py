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


class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''

    # table = []

    def __init__(self):
        self.page_dir = os.path.dirname(
            os.path.abspath(os.path.dirname(os.path.abspath(__file__))))  # self.seleniumUtil =  # print(self.page_dir)
        # self.get_excel = self.get_excel() #实例化get_excel方法

    def get_excel(self, founction, sheet_name):
        '''
        元素的定位方式
        :return:
        '''
        # 定义用例的路径
        file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # 打开Excel文件
        self.excel = xlrd.open_workbook(file_dir) #使用self主要是后面的方法中需要引用到
        self.table = self.excel.sheet_by_name(sheet_name)  # 打开sheet文件
        self.ncols = self.table.ncols  # 获取列数
        self.nrows = self.table.nrows  # 获取行数
        # return table,nrows,ncols

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
        element_locator_way = ''
        element_locator_value = ''

        locator = self.table.row_values(row_index,colum_index) #获取元素定位的列的值
        locator_split = locator[0].split('.') #由于元素定位的方式为：page.case,所以需要将它分开
        # print(locator_split[1])
        for i in range(self.nrows):
            '''
           根据行数循环 ,
           如果获取到的别名和指定的别名相同，
           就存储当前行的定位值和定位方式
           '''
            # if self.table.row_values(i,colum_index)[0] == locator_split[1]:
            element_locator_way = self.table.row_values(i,4,5)
            element_locator_value = self.table.row_values(i,5,6)
        return element_locator_way,element_locator_value






    def parse_excel(self, founction, case_name):
        '''
        解析Excel用例
        :return:
        '''
        # 定义用例的路径
        file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # 打开Excel文件
        # locate_by_way_value = 0
        # locate_by_way = 0
        # test_data_column_index = 0
        # action_column_index = 0
        # locate_column_index = 0
        excel = xlrd.open_workbook(file_dir)
        logging.info('打开' + founction + '.xlsx' + '文件')
        # 获取用例名字
        table = excel.sheet_by_name(case_name)
        logging.info('获取用例' + case_name + '的名字')
        # 获取单元格数量
        ncols = table.ncols
        nrows = table.nrows
        # print('行数：'+str(nrows))
        row_values = table.row_values(0)
        for i in range(ncols):
            if row_values[i] == '动作':
                action_column_index = i  # print(action_column_index)
            elif row_values[i] == '元素定位':
                locate_column_index = i  # print(locate_column_index)
            elif row_values[i] == '元素定位方式':
                locate_by_way = i
            elif row_values[i] == '元素定位值':
                locate_by_way_value = i
                print('元素定位值' + str(locate_by_way_value))
            elif row_values[i] == '测试数据':
                test_data_column_index = i  # print(test_data_column_index)
        # for n in range(1,nrows):

        for k in range(1, nrows):
            logging.info('正在解析Excel：' + founction + '.xlsx用例：' + case_name + '的第' + str(k) + '行步骤...')
            print('正在解析Excel：' + founction + '.xlsx用例：' + case_name + '的第' + str(k) + '行步骤...')
            action = table.cell_value(k, action_column_index)
            locate_way = table.cell_value(k, locate_by_way)
            print('locate_way' + locate_way)
            locate_way_value = table.cell_value(k, locate_by_way_value)
            print('locate_way_value' + locate_way_value)
            # if locate_way == 'id':

            # element = WebDriver.find_element(By.ID,locate_way_value)
            # print(element)
            # print(action)
            if action:
                if action == '打开链接':
                    data = table.cell_value(k, test_data_column_index)
                    print(data)
                elif action == '导航链接':
                    data = table.cell_value(k, test_data_column_index)
                    print(data)
                elif action == '输入':
                    data = table.cell_value(k, test_data_column_index)

                    print(data)
            # 待续，还有很多情况需要补充

            else:
                break


if __name__ == '__main__':
    # s = SuperAction().get_page_element_locator('test','Sheet1')
    s = SuperAction().get_page_element_locator('test', 'Sheet1',2,3)
    # s1 = SuperAction().get_page_element_locator('Xpath','id')
    # print(s)
    print(s)
