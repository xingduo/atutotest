#!/usr/bin/python
# coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: seleniumUtil.py
@time: 2018/8/3 23:35
"""

import logging
from util.selectBrowser import SelectBrowser


class SeleniumUtil:

    def __init__(self, browser_name):
        self.driver = SelectBrowser.get_browser(browser_name)

    def launch_browser(self, browser_name, url, time_out):
        # 获取浏览器
        try:
            # window界面最大化
            self.maxWindow(browser_name)
            # 等待页面加载
            self.waite_for_page_loading(time_out)
            # 获取url
            self.get(url)
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








