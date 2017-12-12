# 添加商品
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/admin.php")
driver.find_element_by_name("username").send_keys("admin")
ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB)\
    .send_keys("1234").perform()
driver.find_element_by_class_name("Btn").click()

# 验证码的问题
# 1.通过第三方软件识别图片,识别图片上的文字
# 识别图片上的文字,识别率很高.但是识别验证码的正确率就很低,
# 如果识别软件可以把验证码识别准确率很高,那么所有的网站就不需要验证
# 2.通过第三方网站识别图片上的文字,识别率很高
# 肉眼识别,需要人力成本,要付费的
# 3.让开发人员提供一个万能验证码,企业里最长用的方法,短信验证码也是一样的
# 海盗商城的验证码是1234
# 自己可以设置王能验证码
# phpfind 文件夹中www文件夹存放海盗商城代码
# 网站开发一般都是基于MVC设计模式
# m model 数据库模型层, 数据库有一个用户表hd_user ,表里包含id,name等字段
# 根据hd_user这个表创建一个类,类名就叫user,类里包含id,name等属性(成员变量)
# V   view 视图层  ,用户可见的部分,前端的Html页面
# C   controller  控制器,用来处理网站业务逻辑,判断验证码是否正确,肯定是放在Controller这层
# 网址中的M表示模块,模块指的是文件夹或者包,C 表示Controller 控制器,控制器都是class
# a 表示action,行为,类中名词用成员变量,类中动词用方法表示
# 所有通过URL就可以看出登录页面属于那个类,那个包,那个方法.
# 通过修改源代码,增加一个验证码
# 4.登录时,有一个复选框 "***某某天内免登录",一次手动登录,可以N天运行代码
# 5.读取cookie文件,问题是cookie信息一般会加密,比较复杂
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
product_name_path = "/html/body/div[2]/div[2]/dl/form/dd[1]/ul/li[1]/input"
# 切换frame
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone")
# css_selector 可以用来定位组合class,只需要在每个class前面加一个小数点
# driver.find_element_by_css_selector("name").send_keys("iphone")

driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
pin_pai = driver.find_element_by_name("brand_id")
Select(pin_pai).select_by_value("1")
# select1 = driver.find_element_by_class_name("select")
# Select(select1).select_by_value("1")

driver.find_element_by_id("jiafen").click()


driver.find_element_by_class_name("button_search").click()
