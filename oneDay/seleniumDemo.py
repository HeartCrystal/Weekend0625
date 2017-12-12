import time  # time 是python内置一个代码库
from selenium import webdriver
# 引入代码库,从谷歌公司的selenium项目中引入 webdriver,网络驱动 用来控制浏览器
# 注释的快捷键 ctry +/是多行 , shift+3是单行
# 1.打开浏览器
driver = webdriver.Chrome()
# 在driver初始化以后,可以设置浏览器全屏
driver.maximize_window()
# 在driver初始化以后,可以设置智能等待时间
# implicitly 隐式的,含蓄的  wait 等待     隐式等待
# 30,单位是秒,最多等待30秒,30秒内没找到元素,则抛出异常.
# implicitly_wait  这个参数影响后面所有的语句
# time.sleep() 只影响下一条语句.
# 在工作中有时可以组合使用
driver.implicitly_wait(30)
# 2.打开登录页面
# driver驱动的以上,get获得,通过在浏览器中输入网址,获得一个网站
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 3.输入用户名
# 在浏览器上,通过编号id 去找用户名的输入框
# find 找 element 元素 by 通过,
# 自己去注册一个用户名
# send 发送 key 键盘上所有的按键
# 发送 c,h,a,....到找到的输入框中
driver.find_element_by_id("username").send_keys("zqtest1")
# 4.输入密码
driver.find_element_by_id("password").send_keys("zqtest1")
# 5.点击登录按钮
# class_name 是class的名字,通过class的名字去找元素
# 这个方法只能用一个class的名字
# click是点击的意思!模拟鼠标左键单机事件
# 三种人选一个,因为用户名和密码和登录按钮有一个共同的父节点
# 其实他们三个控件都不能执行submit
# for表单下的所有元素都可以用于submit提交数据
# driver.find_element_by_class_name("login_btn").submit()
# driver.find_element_by_id("password").submit()
# driver.find_element_by_id("username").submit()
driver.find_element_by_class_name("login_btn").click()
# time.sleep(5)
# link链接 text文本,通过链接文本的方式来定位
# 这个方法只适用于a标签,只有a标签才是链接
driver.find_element_by_link_text("进入商城购物").click()
# 搜索商品
driver.find_element_by_name("keyword").send_keys("iPhone")
driver.find_element_by_class_name("btn1").click()
# 加入购物车
# css层叠样式表  selector选择器,定位器
# 找到目标元素的html代码--->右键copy-->copy selector
# 选择find_element_by_selector的方法,粘贴copy的代码
driver.find_element_by_css_selector("body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img").click()
# 窗口切换
# 由于点某些链接,浏览器上会增加一个新的窗口
# 这时selenium还在第一个窗口上寻找元素,当你想要在新窗口上寻找元素时
# 你就必须指定,在新窗口上工作
# 首先 , 你可以获取当前窗口的句柄 , 句柄 , 类似于门把手
# current 当前的  window  浏览器的窗口  handle 句柄
# 这句话是用来返回当前窗口的命名
handle = driver.current_window_handle
# 其次 , 你可以获取当前浏览器中一共有几个窗口
# 最后有一个小s,表示返回浏览器中所有的窗口
handles = driver.window_handles
# python的for 循环
# for 循环的关键字, item是我们自己起的名字,每一次循环,itme就代表一个窗口
# handles所有的窗口
for item in handles:
    # 如果当前循环到第一个窗口
    if item == handle:
        driver.close()
    else:
        # 如果不是第一个窗口,那么就是循环到第二个窗口
        # 这时item就是第二个窗口
        # switch_to 切换到window窗口,切换到那个窗口
        # switch_to.window(item) 切换到item这个窗口
        driver.switch_to.window(item)
# 加入购物车
driver.find_element_by_id("joinCarButton").click()

# 进行结算
# 去购物车结算
driver.find_element_by_class_name("shopCar_T_span3").click()
# 清空购物车
driver.find_element_by_class_name("shopCar_btn_02").click()

time.sleep(2)
# 弹出框的操作
# alert  弹出框   accept  接受
# 点击弹出框的确认按钮
driver.switch_to.alert.accept()
# 点击弹出框的取消按钮. dismiss 拒绝
# driver.switch_to.alert.dismiss()

# 添加一个时间等待,用例运行结束后10秒后退出
# 引入代码库的快捷键,Alt+Enter
# time 时间 sleep睡觉的意思,让selenium程序休息10秒
# time.sleep(10)
# 当测试用例结束,退出浏览器
# driver.quit()