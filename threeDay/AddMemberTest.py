# 添加会员测
# 为什么要用单元测试框架 unittest?
# 组织和执行测试用例,一次运行多条测试用例
import os
import unittest
import time
from selenium import webdriver
# python 中类的声明,用class关键字
# 类名后面有一个括号,用来表示继承
# unit 单元  test测试, testcase 测试用例
# 1.应用unittest框架的第一步,继承TestCase这个类
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class AddMemberTest(unittest.TestCase):
    # 2.重写Testcase这个类的SetUp方法和tearDown方法.
    # setUp构建,测试用例的预置条件,每个测试用例之前都要执行的步骤
    def setUp(self):
        # driver,在方法内部声明,表示局部变量,只能在该方法中使用
        # 在driver前面加上self关键字,表示成员变量,类似与java中的this
        # 成员变量在类的内部,所有方法都可以访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

    # trarDown  tear是哭的意思,tearDown 拆毁的意思
    # 在测试用例执行完,应该把测试环境回复到执行前的状态,避免污染下一次测试用例的执行.
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    # 测试用例,前面必须用test开头
    # 测试框架组织和执行测试用例,依靠就是约定
    # 测试框架规定了以test开头的方法就是测试用例,会自动执行
    # 其他不以test开头的方法不会被执行,
    def test_deng_lu(self):
        driver = self.driver
        driver.get("http://localhost/admin.php")  # 打开后台登录界面
        admin_name = "admin"
        driver.find_element_by_name("username").send_keys("admin")
        # 代表一组动作和行为,用perform方法表示这组行为动作的结束
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(
            Keys.ENTER).perform()  # 通过按tab键,切换到密码输入框

        time.sleep(5)
        # 截图
        # get 获得, screenshot 截图  as file 把截图保存成文件
        base_path = os.path.dirname(__file__)
        path = base_path + "/image/hou_tai_homepage.png"
        driver.get_screenshot_as_file(path)

        # 获取页面标题,通过标题判断页面是否跳转正确
        # print(driver.title)#从页面抓取实际结果
        # self.assertEqual(driver.title,"会员管理中心")
        # 获取URL,通过网址判断页面正确
        # print(driver.current_url) # 获取到当前的网址
        # asser 断言的意思,预期结果和实际结果的比较,来判断测试用例是否通过,如果通过,就没有提示信息
        # unittest 这个框架为我们提供了丰富的断言方法
        # self.assertIn("m=admin&c=index&a=index",driver.current_urlr)

        # 获取页面元素的文本信息,用于测试用例校验
        # 因为登录名是可变的,所以这个文本是随着登录名变化的
        welcome_text = driver.find_element_by_css_selector("div.welcome > a:nth-child(1)").text
        self.assertIn(admin_name,welcome_text)
        # 断言有一个特点:一旦断言失败,当前方法后面的语句就不会被执行


    def switch_window(self):
        pass # 这种方法属于库方法,不需要直接执行,用于被测试用例调用