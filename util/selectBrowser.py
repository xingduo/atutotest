#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: selectBrowser.py
@time: 2018/8/3 23:36
"""
import logging
from Lib import platform
from selenium import webdriver
import configparser

class SelectBrowser:

    '''
         选择浏览器，不同的系统有不同的常用的浏览器
    '''


    def get_browser(self,browser):
        '''
        获取浏览器
        :return:
        '''
        # 获取系统平台
        platform_ = platform.system()
        logging.info('当前的操作系统是' + platform_)
        logging.info('启动的浏览器是' + browser)
        if platform_ == 'Windows':
            if browser == 'ie':
                driver = webdriver.Ie()
                return driver
            elif browser == 'chrome':
                driver = webdriver.Chrome()
                return driver
            elif browser == 'firefox':
                driver = webdriver.Firefox()
                return driver
            else:
                logging.error(browser + '浏览器在该系统上没有找到，目前只支持IE，Chrome、Firefox...')
        elif platform_ == 'Linux':
            if browser == 'chrome':
                driver = webdriver.Chrome()
                return driver
            elif browser == 'firefox':
                driver = webdriver.Firefox
                return driver
            else:
                logging.error(browser + '浏览器在该系统上没有找到，目前只支持Chrome、Firefox...')
        elif platform_ == 'Mac':
            if browser == 'chrome':
                driver = webdriver.Chrome()
                return driver
            elif browser == 'firefox':
                driver = webdriver.Firefox()
                return driver
            else:
                logging.error(browser + '浏览器在该系统上没有找到，目前只支持Chrome、Firefox...')
        else:
            logging.error('很遗憾！没有找到对应的系统！目前只支持Windows、Linux以及Mac系统...')
            return None

'''

if __name__ == '__main__':
    s = SelectBrowser()
    s.getBrowser()
'''

