#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,HTMLTestRunner,MySQLdb,time,re,os

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = self.get_driver()

        # return self.driver
        #
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def get_driver(self):
        driver = webdriver.Firefox()
        return driver
    def get_start(self):
        self.driver.implicitly_wait(8)
        self.driver.get("http://10.0.0.21/?u=http%3A%2F%2F10.0.0.95%2Fj_security_check")
        self.driver.find_element_by_xpath(".//*[@id='login_container']/ul[1]/li[1]/div/input").send_keys("407224831@qq.com")
        self.driver.find_element_by_xpath(".//*[@id='login_container']/ul[1]/li[2]/div/input").send_keys("111111")
        self.driver.find_element_by_xpath(".//*[@id='login_container']/input").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath(".//*[@id='nav_dashboard']/span").is_displayed()
            print("登录成功")
        except:
            print("登录失败")
            driver.get_screenshot_as_file("login.png")
    def mysql_select(self,select):
        hostname,username,passwd,db,port = "10.0.0.95","ibizdata" ,"ibizdatatest","db1",3306
        conn=MySQLdb.connect(host=hostname,user=username,passwd=passwd,port=port,db=db)
        curson=conn.cursor() #创建游标
        #sql="select * from tb1_product_info where merchant_id='000619'  order by created_date desc"
        sql=select
        print(curson.execute(sql)) #先执行语句
        ret1=curson.fetchall()  #curson.fetchall() 所有结果  tuple元组
        #print(ret1[1][0])  #打印元组中指定的值
        conn.commit()
        curson.close()
        conn.close()

    def addCommodity(self,sku):
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='searchSelectText']").send_keys(sku)
        driver.find_element_by_xpath(".//*[@id='searchSelectId']/a[2]").click()
        driver.find_element_by_xpath(".//table/tr[2]/td[text()='搜 SKU']").click()
        driver.find_element_by_xpath(".//span[@id='goodsResult']/div/div/div/div[2]/div/table/tr"
                                     "/td[1]/div/div/input").click()
        driver.find_element_by_xpath(".//div[@id='content']/../div[2]/div/span/a").click()


