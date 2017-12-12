# 登录测试
# 为什么有的链接弹新窗口?有的链接不弹新的窗口?
# target = "_blank".target 目标  _black 空白的
# 在一个空白的新窗口打开网站对应的新窗口,没有这个属性,就在原来的窗口打开
# 知道了html这个特点后,可以想到一种新的窗口切换方式
# 把target属性删掉,然后在点击登录链接,这时就不会有新窗口出现了
# 如何把手动删除target属性的步骤记录下来,保持下来?用javascript
# 如何把javascript脚本写到python语言中
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/index.php")
# 在点击链接之前,执行javasript语句
# execute执行  script脚本
# 在Python语言中,你可以用双引号表示一段字符串
# 也可以用但引号表示一段字符串
# 如果字符串中含有单引号,那么最外层你就用双引号表示
# 如果字符串中含有双引号,那么最外层就用单引号表示
driver.execute_script("document.getElementsByClassName('site-nav-right fr')[0].childNodes[1].removeAttribute('target')")
# driver.execute_script("")
# javascript 只有getElementById和getElementByClassName
# 没有getElementByClassName
driver.find_element_by_link_text("登录").click()
