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
from util.config import Config

class SuperAction:
    '''
    解析Excel表格，读取sheet等操作
    '''
    def __init__(self, case_name=None):
        self.page_dir = os.path.dirname(
            os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        # super(SuperAction, self).__init__(browser_name=Config())
        self.browser_name = Config()
        self.driver = SelectBrowser().get_browser()
        self.tables = self.get_table(case_name)
        self.rows = self.get_rows()
        self.cols = self.get_cols()

    def parse_excel(self,SeleniumUtil):
        for table in self.tables:
            for row in range(1,self.rows):
                action_value = table.cell_value(row,2)
                ele = table.cell_value(row,3)
                ele_locate_way = table.cell_value(row,4)
                ele_locate_value = table.cell_value(row,5)
                test_data = table.cell_value(row,6)
                if action_value == '打开浏览器':
                    SeleniumUtil.launch_browser(self.browser_name)
                if action_value == '输入URL':
                    SeleniumUtil.get(ele_locate_value)
                if action_value == '输入':
                    SeleniumUtil.input(ele_locate_way,ele_locate_value)
                if action_value == '点击':
                    SeleniumUtil.click(self.get_locate_way(ele_locate_way,ele_locate_value))

    def get_table(self,case_name):
        file_dir = self.page_dir + '\case\\' + case_name + '.xlsx'
        data = xlrd.open_workbook(file_dir)
        tables = data.sheets()
        return tables

    def get_rows(self):
        # file_dir = self.page_dir + '\case\\' + case_name + '.xlsx'
        # data = xlrd.open_workbook(file_dir)
        # tables = data.sheets()
        # tables = self.get_table(c)
        for table in self.tables:
            rows = table.nrows
        return rows

    def get_cols(self):
        for table in self.tables:
            cols = table.nrows
        return cols


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
