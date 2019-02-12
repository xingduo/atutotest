#!/usr/bin/python
# coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: seleniumUtil.py
@time: 2018/8/3 23:35
"""
# from selenium import webdriver
from selenium.webdriver.support.ui import Select
import logging
from util.selectBrowser import SelectBrowser
from util.config import Config


class SeleniumUtil:

    def __init__(self):
        self.config = Config()
        self.driver = SelectBrowser().get_browser()
        # super(SeleniumUtil,self).__init__(chrome_options=chrome_options)

    def launch_browser(self, browser_name):
        # 获取浏览器
        try:
            # window界面最大化
            self.max_window(browser_name)
            # 等待页面加载
            # self.waite_for_page_loading(time_out)
            # 获取url
            # self.get(url)
        except Exception:
            logging.warning('注意：页面没有完全加载出来，刷新重试！！')
            # 刷新页面
            self.refesh()

    def max_window(self, browser_name):
        logging.info('最大化浏览器:%s' % browser_name)
        self.driver.maximize_window()

    def waite_for_page_loading(self, time_out):
        logging.info('等待页面加载！！')
        self.driver.implicitly_wait(time_out)

    def get(self, url):
        logging.info('获取url:%s' % url)
        self.driver.get(url)

    def refesh(self):
        logging.info('刷新！')
        self.driver.refresh()

    def input(self,ele,ele_value,key):
        self.driver.find_element(ele,ele_value).send_keys(key)

    def click(self,ele,value = None):
        self.driver.find_element(ele,value).click()

    def selectByValue(self,ele,value):
        s = Select(self.driver.find_element(ele))
        s.select_by_value(value)

    def selectByIndex(self,ele,index):
        s = Select(self.driver.find_element(ele))
        s.select_by_index(index)








