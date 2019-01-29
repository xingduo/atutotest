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
from xlutils.copy import copy
import xlutils
# from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from util.seleniumUtil import SeleniumUtil
from util.selectBrowser import SelectBrowser

class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''
    def __init__(self, founction, sheet_name,index = None, browser_name=None):
        self.page_dir = os.path.dirname(
            os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        super(SuperAction, self).__init__(browser_name=browser_name)
        self.driver = SelectBrowser.get_browser(browser_name)
        self.file_dir = self.page_dir + '\case\\' + founction + '.xlsx'
        self.data = xlrd.dopen_workbook(self.file_dir)
        self.tables = self.data.sheets()
        self.rows = self.table.nrows
        self.cols = self.table.ncols
        
    def parse_excel(self,SeleniumUtil):
        for table in range(self.tables):
            for row in range(1,self.rows):
                action_value = table.cell_value(row,2)
                ele = table.cell_value(row,3)
                ele_locate_way = table.cell_value(row,4)
                ele_locate_value = table.cell_value(row,5)
                test_data = table.cell_value(row,6)
                if action_value == '打开浏览器':
                    SeleniumUtil.launch_browser()


    def get_page_element_locator(self, founction, sheet_name, row_index, colum_index):
        '''
        :param sheet 测试用例表中的sheet
        :param row_index 用例表中的行
        :param colum_index 用例表中的列
        :param founction 页面名字
        :return:返回定位方式和定位值
        '''
        element_locator_way_list = []
        element_locator_value_list = []

        # 获取元素定位的列的值
        locator = self.table.row_values(row_index,colum_index)

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

    def get_locate_way(self,locate_way, locate_value):
        '''
        @:param locateway 定位方式
        @:param locatevalue 定位值
        :return element_locator 定位的方式
        '''
        
        if locate_way == By.ID.lower():
            elementLocator = self.driver.find_element_by_id(locate_value)
        elif locate_way == By.CLASS_NAME.lower():
            elementLocator = self.driver.find_element_by_class_name(locate_value)
        elif locate_way == By.XPATH.lower():
            elementLocator = self.driver.find_element_by_xpath(locate_way)
        elif locate_way == By.NAME.lower():
            elementLocator = self.driver.find_element_by_name(locate_value)
        elif locate_way == By.TAG_NAME.lower():
            elementLocator = self.driver.find_element_by_tag_name(locate_value)
        elif locate_way  == By.LINK_TEXT.lower():
            elementLocator = self.driver.find_element_by_link_text(locate_value)
        elif locate_way == By.CSS_SELECTOR.lower():
            elementLocator = self.driver.find_element_by_css_selector(locate_value)
        elif locate_way == By.PARTIAL_LINK_TEXT.lower():
            elementLocator = self.driver.find_element_by_partial_link_text(locate_value)
        else:
            logging.error("你选择的定位方式：["+locate_way+"] 不被支持!")
        return elementLocator
         

if __name__ == '__main__':
    s = SuperAction().get_page_element_locator('test','Sheet1')
    # s = SuperAction().get_page_element_locator('test', 'Sheet1',2,3)
    # s = SuperAction().parse_excel()
