# encoding:utf-8
"""
@author: lydiazhuhailing

@copyright: 2022 .com. All rights reserved.

@contact:百度搜索
"""
import os

from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from HTMLTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self) -> None:
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                    {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'})
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidu(self):
        '''搜索关键字：HTMLTestRunner'''
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element(By.ID, 'kw').clear()
        driver.find_element(By.ID, 'kw').send_keys('HTMLTestRunner')
        driver.find_element(By.ID, 'su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, 'HTMLTestRunner_百度搜索')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
