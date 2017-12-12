from selenium.webdriver.common.by import By

class DengLuPage:
    url = "http://localhost/index.php?m=user&c=public&a=login"
    # (,,) 这是python中的元组,类似于数组, 区别是元组中元素类型可以不一样
    # 采用元组保存元素的定位方式
    # 以后前端页面一旦发生变化, 我只需要修改元素的定位方式就可以了
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    login_btn_loc = (By.CSS_SELECTOR, ".login_btn.fl")

    # __init__ python的构造方法
    # 每次实例化这个类,相当于打开登录页面, 需要指定在哪个浏览器上打开这个页面,所以需要把driver属性传入构造方法
    def __init__(self, driver):
        # 当你想调用这个类的方法时, 首先你必须创建这个类的对象
        # 构造方法就是创建对象时调用的方法
        # 创建页面对象时, 把driver作为参数传进来,赋值给成员变量,方便其他方法调用
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def input_username(self, username):
        # 在编程中,应该尽量避免写字符串常量,比如"changcheng"
        # 这样的坏处是, 如果你想用不同账号名测试时,必须修改代码
        self.driver.find_element(*self.username_loc).send_keys(username)


    def input_password(self, password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn_loc).click()

    #  有时,我们想一句话执行登录功能
    # 少数情况, 我们要测试登录功能,我们需要输入不同用户名和密码进行测试,
    # 多数情况,登录只是其他操作的一个前提条件,我们就用changcheng这个账号登录就可以了
    # 那么我们可不可以给login()方法的用户名和密码设一个默认值?
    # 如果用户没有提供用户名和密码,用默认值登录
    # 如果用户提供,那么用用户的
    # 如何设置默认值?
    def login(self, username="changcheng", password="123654"):
        self.open_page()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def find_element(self, *loc):
        self.driver.find_element(*loc)
        # selenium中自带find_element的方法,需要传两个参数,
        # 第一个参数是元素定位的方式, 第二个参数是页面中该方式的具体的属性
        # self.driver.find_element(By.ID, "username") 等于 self.driver.find_element(*username_loc)
        # 星号的作用是把一个元组,的所有元素拆开
        # 如果没有星号传进来的是一个数组,要想得到数组中的每一元素,需要循环遍历, 但是有了星号,直接可以获得每个元素
        # 例子: 如果 loc = (1,2)
        # 那么 *loc = 1 和 2

        # 把find_element这句话单独封装,有一个好处, 因为页面元素有可能定位不到, 所以以后可以考虑,在元素定位之前,前判断这个元素是否存着, 如果元素存在,那么再去执行元素操作, 如果不存在打印异常信息

