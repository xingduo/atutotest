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
        self.page_dir = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        # self.seleniumUtil =
        # print(self.page_dir)

    # def excel(self):


    def get_locate_way(self,key,value):
        '''
        元素的定位方式
        :return:
        '''
        if key:
            if key.lower() == 'xpath':
                element_locator = value
                print(element_locator)
            if key.lower() == 'id':
                element_locator = By.ID
                print(element_locator)


    def get_page_element_locator(self,founction,case_name):
        '''
        :return:返回定位方式和定位值
        '''
        # 定义用例的路径
        file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # 打开Excel文件

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
        for n in range(ncols):
            if row_values[n] == '动作':
                locate_column_index = n
                print(locate_column_index)
        for j in range(1,nrows):
            locator = table.row_values(n,locate_column_index)
            print(locator)

    def parse_excel(self,founction,case_name):
        '''
        解析Excel用例
        :return:
        '''
        # 定义用例的路径
        file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        # 打开Excel文件
        locate_by_way_value = 0
        locate_by_way = 0
        test_data_column_index = 0
        action_column_index = 0
        locate_column_index = 0
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
        # for j in range(ncols):
        # print(row_values)
        for i in range(ncols):
            if row_values[i] == '动作':
                action_column_index = i
                # print(action_column_index)
            elif row_values[i] == '元素定位':
                locate_column_index = i
                print(locate_column_index)
            elif row_values[i] == '元素定位方式':
                locate_by_way = i
            elif row_values[i] == '元素定位值':
                locate_by_way_value = i
            elif row_values[i]  == '测试数据':
                test_data_column_index = i
                # print(test_data_column_index)
        for n in range(1,nrows):
            locate_way = table.cell_value(n,locate_by_way)
            locate_way_value = table.cell_value(n,locate_by_way_value)
            print(locate_way)
            find_by_id = WebDriver.find_element(locate_way,locate_way_value)
            print(find_by_id)




        for k in range(1,nrows):
            logging.info('正在解析Excel：' + founction + '.xlsx用例：'+ case_name + '的第' + str(k) + '行步骤...' )
            print('正在解析Excel：' + founction + '.xlsx用例：'+ case_name + '的第' + str(k) + '行步骤...')
            action = table.cell_value(k,action_column_index)
            # print(action)
            if action:
                if action == '打开链接':
                    data = table.cell_value(k,test_data_column_index)
                    print(data)
                elif action == '导航链接':
                    data = table.cell_value(k,test_data_column_index)
                    print(data)
                elif action == '输入':
                    data = table.cell_value(k,test_data_column_index)
                    print(data)
            #待续，还有很多情况需要补充

            else:
                break

if __name__ == '__main__':
    # s = SuperAction().get_page_element_locator('test','Sheet1')
    s = SuperAction().parse_excel('test','Sheet1')
    # s1 = SuperAction().get_page_element_locator('Xpath','id')
    # print(s)
    print(s)
