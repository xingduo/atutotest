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

class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''

    def __init__(self):
        self.page_dir = os.path.dirname(os.path.realpath(__file__))
        print(self.page_dir)

    def get_locate_way(self):
        '''
        获取sheet路径
        :return:
        '''
        file_path = os.getcwd()
        return file_path
    def get_page_locator(self):
        '''
        获取用例表中的sheet
        :return:
        '''




if __name__ == '__main__':
    s = SuperAction().get_locate_way()

    print(s)
