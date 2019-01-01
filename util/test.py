#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: test.py
@time: 2018/10/30 21:15
"""
def suanfa():
    list = [3,4,2,36,7,6]
    for i in range(1,len(list)):
        temp = list[i]
        j = i-1
        while j >= 0:
            if list[j] > temp:
                list[j+1] = list[j]
                list[j] = temp
            j =j-1
    print(list)
def maopaopaixu():
    list = [3, 4, 2, 36, 7, 6]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    print(list)


if __name__ == '__main__':
    # suanfa()
    maopaopaixu()