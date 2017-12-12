from webdriver import ActionChains
from webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select

# def define 定义的意思
# def是方法的关键字,后面直接接方法名
# () 括号里面是需要改变的参数
# 冒号表示声明结束
#  在python语言中,遇到冒号,下一行就要空4格
def switchWindow(driver , args) :
    driver.execute_script("arguments[0].removeAttribute('target')", args)
    args.click()

driver = webdriver.Chrome()
driver.implicitly_wait(30)
# 回家之后发现窗口最大化执行不了? 原因是浏览器版本更新了
# 1.需要去selenium官网上下载最新的chromedrver.exe
# 2.关闭谷歌更新
driver.maximize_window()
driver.get("http://localhost/index.php")
denglu = driver.find_element_by_link_text("登录")
# driver.execute_script("arguments[0].removeAttribute('target')",denglu)
# denglu.click()
switchWindow(driver,denglu)
username = driver.find_element_by_id("username")
username.send_keys("zqtest1")
# selenium 高级元素操作 . 1.模拟tab键
# Action 行为, 动作   Chain链表  s表示一组动作的行为组成的链表
# 在网页上左键单机叫动作,双击也是,发送按键也是
# 所有在页面上能执行的动作都可以在这个类中找到
# tab键是一个特殊的按键,所有键盘上的特殊键,都存放在keys这个类里
# 引入包的快捷键 Alt+回车
# 链表最后一定要指明链表结束 , perform是链表结束的标志
# perform 执行的意思,只有程序见到perform才开始执行,否则send_keys...语句只在缓存中不会执行
ActionChains(driver).send_keys(Keys.TAB).send_keys("zqtest1").perform()
username.submit()
driver.find_element_by_link_text("进入商城购物").click()
# 找到搜索框页面元素,并且命名为imput_box
imput_box = driver.find_element_by_name("keyword")
# 在搜索框中输入iphone
imput_box.send_keys("iphone")
# 提交搜索结果
imput_box.submit()
# 右键copy出来的xpath
img_path = "/html/body/div[3]/div[2]/div[3]/div/div[1]/a"
# 通过xpath获得商品图片这个元素
img = driver.find_element_by_xpath(img_path)
# driver.execute_script("arguments[0].removeAttribute('target')",img)
# img.click()
switchWindow(driver,img)
# 加入购物车
driver.find_element_by_id("joinCarButton").click()
# 去购物车结算
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
# 添加新地址
driver.find_element_by_class_name("add-address").click()
# 收货人
driver.find_element_by_name("address[address_name]").send_keys("张三")
# 手机号
driver.find_element_by_name("address[mobile]").send_keys("13800000000")
# 收获地址
# 下拉框的操作
# select 选择的意思, html指的是下拉框
select1 = driver.find_element_by_id("add-new-area-select")
# 下拉框是一种特殊的网页元素,在selenium里有一个单独的类select用来表示下拉框
# 把下拉框从一个webElement的类型,转换成select的类型
# 在select这个类里,selenium为我们封装好了操作下拉框的方法
# 比如.select_by_value(),select_by_visible_text
# Select(select1).select_by_value("370000")
# visible_text,可见文本
# Select(select1).select_by_visible_text("河北省")
# index 索引 , 按顺序数的 , 3代表第4个选项 , 即河北省
Select(select1).select_by_index(3)
# find_elements()方法  ,返回一个webElement的集合
select2 = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(select2).select_by_value("130200")
# 第三个下拉框
# select3 = driver.find_element_by_class_name("add-new-area-select")[2]
# tag 标签 tag_name 标签名
# 通过标签名找到页面中所有select标签,根据下标选择第几个下拉框
select3 = driver.find_elements_by_tag_name("select")[2]
Select(select3).select_by_visible_text("开平区")
# 地址
driver.find_element_by_name("address[address]").send_keys("开平区某街某乡某")
# 邮编
driver.find_element_by_name("address[zipcode]").send_keys("10010")


