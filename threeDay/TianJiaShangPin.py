import time
from selenium import webdriver
# 从谷歌selenium中导入webdriver网页驱动,用来操作浏览器
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from threeDay.readCsvFile import readCsv

driver = webdriver.Chrome() # 通过网页驱动打开浏览器
driver.implicitly_wait(30) # 隐式等待30秒
driver.maximize_window()   # 窗口最大化
driver.get("http://localhost/admin.php") # 打开后台登录界面
driver.find_element_by_name("username").send_keys("admin")
# 代表一组动作和行为,用perform方法表示这组行为动作的结束
ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
# 通过按tab键,切换到密码输入框


for row in readCsv():
    product_name = row[0]
    image_path = row[1]
    driver.find_element_by_link_text("商品管理").click()
    driver.find_element_by_link_text("添加商品").click()
    iFrame = driver.find_element_by_css_selector("#mainFrame") # 定位到frame标签
    driver.switch_to.frame(iFrame) # 切换到(那个)frme,"id或者name",或者用更多的方式定位元素之后.直接把元素作为参数传入frame()方法
    driver.find_element_by_name("name").send_keys(product_name)
    # 在执行测试用例时读取Excel中的第一列,根据第一列的内容,添加商品名称
    driver.find_element_by_id("1").click()
    driver.find_element_by_id("2").click()
    driver.find_element_by_id("6").click()
    # 实现双击操作
    ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
    select1 = driver.find_element_by_name("brand_id")
    Select(select1).select_by_value("1")
    # 图片上传
    driver.find_element_by_link_text("商品图册").click()
    # 首先找到真正负责文件上传的控件,然后直接send_keys就可以了
    # 为什么把\换成/?因为\表示转义 \n 表示回车键 \t 表示tab键 \r和\n经常一起使用表示回车换行
    # 键盘上有些按键不能直接输入,比如说回车键,比如tab
    # 在计算机语言中 \\两个双斜杠表示一个单斜杠
    # \\ 和 /在这里都可以用,那种方式更好?
    #  正斜杠更好,正斜杠可以跨平台
    time.sleep(2)
    # 发送图片路径,也需要在客户端去查找,implcitly只管页面加载,所以需要用time.sleep(),在工作中遇到测试用例执行不稳定时,考虑添加time.sleep()
    driver.find_element_by_name("file").send_keys(image_path) #图片路径
    # by_class_name()方法不支持多个class,我们可以用css selector的方式,通过一个元素的多个class定位该元素,只需要去掉空格,在每一个class前面加一个小数点
    driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
    time.sleep(3)# 操作弹出框之前必须要加时间time.sleep(),implicitly_wait不管用
    driver.switch_to.alert.accept()
    driver.find_element_by_class_name("button_search").click()
    # 提交按钮在子frame中,selenium当前在该页面中工作
    # 不能直接找到商品管理所在的页面,必须先切换回根节点所在的页面
    # 从子frame切换回主frame
    # 从子frame切换为主frame,default 默认的,content内容,表示回到页面的根节点
    driver.switch_to.default_content()
    # #parent父母的意思,切换回父框架
    # driver.switch_to.parent_frame()

# 作业修改个人资料
# 登录-->账号设置-->个人资料-->补全信息-->确定
