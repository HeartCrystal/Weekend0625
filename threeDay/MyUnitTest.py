import unittest

import time
from selenium import webdriver

# python中类名和文件名可以不一样,最好是不一样,文件名的首字母应该小写,类名首字母大写,比如,这个文件名更好应该叫myUnitTest
# java中public类名和文件名必须一样
class MyUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

    def tearDown(self):
        time.sleep(10) # 在开发代码时,加time.sleep,开发好以后就不用加了
        self.driver.quit()