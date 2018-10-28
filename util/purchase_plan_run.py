#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,HTMLTestRunner,MySQLdb,time,re,os
from util.public import MyTest


class purchase():

    def __init__(self):
        self.driver = MyTest.get_driver()

    def test_p1_001_createPurchasePlan(self):
        """优先级：P1，功能点：新增采购计划"""
        move_element=self.driver.find_element_by_xpath(".//*[@id='nav_purchase']/span")
        ActionChains(self.driver).move_to_element(move_element).perform()
        self.driver.find_element_by_xpath(".//*[@id='nav']/li[4]/div/dl[1]/dd[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='buttonFrame']/div/ul/li[1]/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='purchasePlan.warehouseId_text']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//div[@id='invalidErrorObj']/../span[5]/div/table/tr[2]/td[1]").click()
        self.driver.find_element_by_xpath(".//span[@id='addGoodsBtn']/a[1]").click()
        time.sleep(1)
        #调用MyTest类下addCommodity的方法
        add=MyTest()


        print(add.addCommodity("AA0002"))



if __name__=="__main__":
    unittest.main()


