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

import openpyxl


class TestCaseFactoryForAll:
	'''
	生成自动化测试用例工具
	'''
	
	def __init__(self):
		self.get_case_name()
		self.get_sheet_name()
	
	def get_case_name(self):
		case_path = os.path.join(os.path.dirname(os.getcwd()) + '\case\\')
		# 获取case文件夹下的所有用例文件
		case_list = os.listdir(case_path)
		# 对文件进行遍历
		for i in range(0, len(case_list)):
			# 获取文件的全名：test.xlsx
			case_full_name = case_list[i]
			# 对全名进行片切，取到后缀名前面的部分:test,不要.xlsx部分
			case_name = case_full_name.split('.')[0]
		return case_name
	
	def get_sheet_name(self):
		case_path = os.path.join(os.path.dirname(os.getcwd()) + '\case\\')
		# 获取case文件夹下的所有用例文件
		case_list = os.listdir(case_path)
		for wb in case_list:
			f_path = os.path.join(case_path + '\\' + wb)
			fb = openpyxl.load_workbook(f_path)
			sheet_name = fb.sheetnames
			print(sheet_name)
		return sheet_name
	
	def create_testcase(self, case_name):
		text = '#!/usr/bin/python\n# coding:utf-8\n' \
		       'class '+case_name.capitalize()+':\n'

		create_file_path = os.path.join(os.path.dirname(os.getcwd()) + '\\testcase')
		suffix = case_name + '.py'
		full_case_path = os.path.join(create_file_path, suffix)
		if not os.path.exists(full_case_path):
			os.mkdir(create_file_path)
			# if not os.path.exists(full_case_path):
			# 	os.mkdir(full_case_path)
		with open(full_case_path, 'w') as fb:
			# 这里应该不能这样写，open（）打开的是文件夹，而不是文件
			fb.write(text)
			fb.close()


if __name__ == '__main__':
	f = TestCaseFactoryForAll()
	f.create_testcase("login")
