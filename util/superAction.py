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

import logging
import xlrd
class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''

    def __init__(self):
        self.page_dir = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        # self.seleniumUtil =
        # print(self.page_dir)

    # def excel(self):


    def get_locate_way(self):
        '''
        获取sheet路径
        :return:
        '''

    def get_page_locator(self):
        '''
        获取用例表中的sheet
        :return:
        '''

    def parse_excel(self,founction,case_name):
        '''
        解析Excel用例
        :return:
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
        print('行数：'+str(nrows))
        row_values = table.row_values(0)

        # print(row_values)
        for i in range(ncols):
            if row_values[i] == '动作':
                action_column_index = i
                # print(action_column_index)
            elif row_values[i] == '元素定位':
                locate_column_index = i
                # print(locate_column_index)
            elif row_values[i]  == '测试数据':
                test_data_column_index = i
                print(test_data_column_index)
        for i in range(1,nrows):
            logging.info('正在解析Excel：' + founction + '.xlsx用例：'+ case_name + '的第' + str(i) + '行步骤...' )
            action = table.row_values(i,action_column_index)
            print(action)
            if action is not None:
                if action == '打开链接':
                    data = table.row_values(i,test_data_column_index)
                    print(data)
                elif action == '导航链接':
                    data = table.row_values(i,test_data_column_index)
                    print(data)













if __name__ == '__main__':
    s = SuperAction().parse_excel('test','Sheet1')

    print(s)
