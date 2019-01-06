#!/usr/bin/python
# coding:utf-8
import unittest
from util.superAction import SuperAction
from util.seleniumUtil import SeleniumUtil
class Login(unittest.TestCase):
    def login(self):
        SuperAction.parse_excel('Login','login',SeleniumUtil)