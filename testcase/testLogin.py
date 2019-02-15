#!/usr/bin/python
# coding:utf-8
import unittest
from util.superAction import SuperAction
from util.seleniumUtil import SeleniumUtil
import HTMLTestRunner
from selenium import webdriver
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.superAction = SuperAction(case_name="testLogin")
    def test01(self):
        self.superAction.parse_excel()
    def test02(self):
        self.superAction.parse_excel()
    def Sheet3(self):
        self.superAction.parse_excel()
