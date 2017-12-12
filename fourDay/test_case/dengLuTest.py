from fourDay.model.MyUnitTest import MyUnitTest
from fourDay.page_object.dengLuPage import DengLuPage

class DengLuTest(MyUnitTest):
    # 测试用例的方法必须以test开头
    def test_login(self):
        DengLuPage(self.driver).login()
