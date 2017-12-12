import unittest

from threeDay.MyUnitTest import MyUnitTest

class ZhuCeTest(MyUnitTest):

    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/")

    def test_zhu_ce2(self):
        driver = self.driver
        driver.get("http://localhost/")

if __name__ == '__main__':
    # 这个方法是用于执行一个文件中的所有测试用例
    unittest.main()

# 我们以前,只写了测试用例的操作步骤,没有判断执行成功还是失败
# 所有的测试用例必须要有断言,自动判断成功还是是失败
