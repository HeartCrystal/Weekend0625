import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from model.connDb import connDb
from model.myUnitTest import MyUnitTest


class ZhuCeTest(MyUnitTest):
    """注册模块测试"""
    def test_zhu_ce(self):
        """注册的用例-正常情况"""
        username = "changcheng731"
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # find_elememt这个方法是find_element_by的方法一样
        # self.driver.find_element_by_name("username")
        # PageObject的目标是把find_element这样的语句,修改成input_username("changcheng")
        # self.driver.find_element(By.CssSelector, "sdsd>sdasds>sds") 这样的语句根本看不出来是什么页面元素, 可读性非常差, 代码维护成本太高, 经常会有执行一段时间以后,网页前端一修改, 代码难以维护,无奈只能重新开发.
        # 所以我们要用page object这种设计模式,改善这种情况
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys("123654")
        self.driver.find_element(By.NAME, "userpassword2").send_keys("123654")
        self.driver.find_element(By.NAME, "mobile_phone").send_keys("13512354567")
        self.driver.find_element(By.NAME, "email").send_keys("changesffsd@adesf.com")
        base_path = os.path.dirname(__file__)
        # 如果想把路径信息显示在测试报告中
        # 只需要print(base_path) 就可以了
        print(base_path) # 结果应该是以WeekendDay4结尾? 还是以WeekendDay4/test_case结尾?
        # path = base_path + "/image/zhuce.png"
        # path = WeekendDay4/test_case/image/zhuce.png
        # 如何删掉中间的test_case? str操作的方法
        # replace 替换的意思
        # 从c:/../WeekendDay4/test_case
        # 替换成 c:/../WeekendDay4/image/zhuce.png
        path = base_path.replace("test_case", "image/zhuce.png")
        self.driver.get_screenshot_as_file(path)
        self.driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(5)
        # result = self.driver.find_element(By.CSS_SELECTOR, "div.site-nav-right.fr > a:nth-child(1)").text
        # self.assertIn(username, result)
        time.sleep(3)
        result = connDb()
        print(result[1])
        self.assertEqual(result[1], username)


