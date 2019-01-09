#!/usr/bin/python
# coding:utf-8
import unittest
from util.superAction import SuperAction
from util.seleniumUtil import SeleniumUtil
import HTMLTestRunner
from selenium import webdriver
class Login(unittest.TestCase):
    def __init__(self,browser_name):
        self.browser_name = browser_name
        self.driver = SeleniumUtil(self.browser_name)
    def test_login(self):
        SuperAction.parse_excel('Login','test_login',SeleniumUtil)