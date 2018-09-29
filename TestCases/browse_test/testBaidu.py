# coding=utf-8
# !/usr/bin/env python
from selenium import webdriver
from GetElementTool import *
from Start_End import *
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import ctime
from time import  sleep

class TestBaiduSearch(unittest.TestCase):
    def setUp(self):
        print ctime()
        test = GetElementTool()
        test_Info=test.getSearchInfo()
        self.url = test_Info["url"]
        self.explorer = test_Info["explorer"]
        print (ctime())
    def tearDown(self):
        print ("test end !")

    def testSearch(self):
        if 'Firefox'in self.explorer :
            print (u"加载浏览器" + ctime())
            driver = webdriver.Firefox()
            print (u"加载浏览器完成" + ctime())
        else:
            driver = webdriver.Chrome()
        print (ctime())
        driver.get(self.url)
        print (ctime())
        driver.find_element_by_id('kw').send_keys(u'selenium')
        driver.find_element_by_css_selector('#su').click()
        element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,u'selenium')))
        title=unicode(driver.title)
        print title
        self.assertEqual(title,u'selenium')
        # element.click()
        driver.find_element_by_css_selector('.favurl').click()
        driver.quit()



if __name__ == '__main__':
    unittest.main()




