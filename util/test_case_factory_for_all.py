#!/usr/bin/python
# coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: test_case_factory_for_all.py
@time: 2018/11/13 23:45
"""
import os
import sys
import openpyxl


class TestCaseFactoryForAll:
	'''
	生成自动化测试用例工具
	'''
	
	def __init__(self):
		self.case_names = self.get_case_name()
		self.sheet_names = self.get_sheet_name()
		self.create_testcase(self.case_names, self.sheet_names)
	
	def get_case_name(self):
		
		case_names = []
		global case_full_name
		case_path = os.path.join(os.path.dirname(os.getcwd()) + '\case\\')
		# 获取case文件夹下的所有用例文件
		case_list = os.listdir(case_path)
		# 对文件进行遍历
		for i in range(0, len(case_list)):
			# 获取文件的全名：test.xlsx
			case_full_name = case_list[i]
			# 对全名进行片切，取到后缀名前面的部分:test,不要.xlsx部分
			case_name = case_full_name.split('.')[0]
			case_names.append(case_name)
		return case_names
	
	def get_sheet_name(self):
		global sheet_names
		case_path = os.path.join(os.path.dirname(os.getcwd()) + '\case\\')
		# 获取case文件夹下的所有用例文件
		case_list = os.listdir(case_path)
		for wb in case_list:
			f_path = os.path.join(case_path + '\\' + wb)
			fb = openpyxl.load_workbook(f_path)
			sheet_names = fb.sheetnames  # sheet_names.append(sheet_name)
		return sheet_names
	
	def create_testcase(self, case_names, sheet_names):
		for case_name in case_names:
			class_name_text = '#!/usr/bin/python\n# coding:utf-8\n' \
			                  'import unittest\n' \
			                  'from util.superAction import SuperAction\n' \
			                  'from util.seleniumUtil import SeleniumUtil\n' \
			                  'import HTMLTestRunner\n' \
			                  'from selenium import webdriver\n' \
			                  'class ' + case_name.capitalize() + '(unittest.TestCase)'':\n'
			def_init = '    def setUp(self):\n' \
			           '        super(' + case_name.capitalize() + ',self).__init__()\n' \
			                                                       '        self.driver = SeleniumUtil()\n' \
			                                                       '        self.superAction = SuperAction(case_name="'+case_name+'")\n'
			create_file_path = os.path.join(os.path.dirname(os.getcwd()) + '\\testcase')
			suffix = case_name + '.py'
			full_case_path = os.path.join(create_file_path, suffix)
			with open(full_case_path, 'w') as fb:
				fb.write(class_name_text)
				fb.write(def_init)
				fb.close()
			for sheet_name in sheet_names:
				print(sheet_name)
				def_name = '    def ' + sheet_name + '(self):\n'
				case_method = '        self.superAction.parse_excel(SeleniumUtil)\n'

				# if not os.path.exists(full_case_path):
				# 	os.mkdir(create_file_path)
				full_case_path = os.path.join(create_file_path, suffix)
				with open(full_case_path, 'a') as f:
					f.write(def_name)
					f.write(case_method)
					f.close()


if __name__ == '__main__':
	f = TestCaseFactoryForAll()
	
	f.create_testcase(f.case_names, f.sheet_names)
