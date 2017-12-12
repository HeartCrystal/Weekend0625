from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/")
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_link_text("登录").click()
# 对同一个元素,分别采用javaScript的方式和Selenium的方式定位了两次
# 其中selenium的方式比较简单,我们可不可以把selenium的定位传入javaScript脚本中呢?
# 可以用关键字 arguments 来实现.arguments是参数的意思
# deng_lu = driver.find_element_by_link_text("登录")
# print打印 type类型
# print(type(deng_lu))
# 把页面元素作为javascript脚本中的参数传入进去
# 把selenium定位的元素作为参数传进javascript脚本中,代替原来javascript定位的语句
# arguments后面的中括号0,表示javascript语句后面的一个参数
# driver.execute_script("arguments[0].removeAttribute('target')",deng_lu)
# deng_lu.click()
# 在selenium元素定位中,有些元素比较复杂,不容易定位,必须用javascript定位
# 用javascript定位接selenium操作,用return 关键字
denglu = driver.execute_script('return document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]')
denglu.click()
# javascript和selenium的元素定位可以互相转换
# selenium一个提供了8种元素定位的方式
# id ,name , class_name , link_text ,  css Selector,Xpath , tag_name,partial_link_text
# 有个别页面元素,用这8种定位都定位不到,你就可以考虑用javascript的方式来定位
