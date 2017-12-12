import os
import unittest
import time
from email.mime.text import MIMEText
from smtplib import SMTP
from fourDay.package.HTMLTestRunner import HTMLTestRunner

def send_email(new_path):
    # 1.用二进制的方式打开测试报告
    new_file = open(new_path, 'rb')
    # 读取测试报告中的正文
    report = new_file.read()
    new_file.close()
    # 2. 把二进制的文件流转成MIME的格式
    # m multi...多用途的 I internet 互联网 M 邮件 E extension 扩展
    # MIME 多用途互联网邮件扩展, 是最常用邮件传输格式
    # 邮件正文的格式一共有三种比较常用, plain 纯文本格式的邮件
    # html html格式的邮件, richtext 富文本格式的邮件
    msg = MIMEText(report, _subtype='html', _charset="utf-8")
    # MIMEText本身是字典类型的, 可以通过键值对的形式设置标题,以及发件人和收件人
    msg["Subject"] ="自动化测试报告"
    msg["from"] = 'bwftest126@126.com'
    msg["to"] = "changchengxc@126.com"
    # 3. 通过smtp协议 s simple 简单 m mail邮件 t 传输 p 协议,
    # 创建协议
    smtp = SMTP()
    # 连接邮件服务器
    smtp.connect("smtp.126.com")
    # 4. 通过协议登录邮箱, 这里应该填写客户端授权码
    smtp.login('bwftest126@126.com', 'abc123asd654')
    smtp.sendmail('bwftest126@126.com', "changchengxc@126.com", msg.as_string())
    smtp.quit()




if __name__ == '__main__':
    # 1.找所有的测试用例
    suite = unittest.defaultTestLoader.discover("./test_case", pattern='*Test.py')
    # 2. 运行找到的测试用例
    # unittest.TextTestRunner().run(suite)
    # 3.生成测试报告, 和运行测试用例类似, 不是生成文本的结果,而是生成html的结果
    # 把HTMLTestRunner.py复制到C:\Users\51Testing\AppData\Local\Programs\Python\Python35\Lib
    # 首先要确定, html测试报告生成在哪个路径下,叫什么名字
    base_path = os.path.dirname(__file__)
    times = time.strftime("%Y-%m-%d_%H%M%S")
    path = base_path + "/Report/auto_test_report"+ times +".html"
    # stream 文件流的意思, 应该传进去的不是路径,而是一个文件
    file = open(path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="自动化测试报告", description="操作系统:Win7, 浏览器:Chrome").run(suite)
    file.close()
    send_email(path)
    # 如何让每次生成的测试报告不覆盖原来的?
    # 为什么会覆盖? 因为重名了
    # 怎么保证不重名? 而且每次运行前不用修改代码
    # 用时间戳, 用报告生成的时间来区别每次的报告
    # 怎么去生成一个时间戳?
    # str 是String的缩写, f 是format 格式化的意思
    # time.strftime() 获取一个格式化的时间
    # 格式可以自己设计 %Y year表示年, %m month月, %d day日
    # %H hour小时, %M minute分  %S second秒
    # times = time.strftime("%Y-%m-%d_%H%M%S")
    # 因为每次生成测试报告肯定在一秒以上,所以永远不会重名,
    # 截图也可以用时间戳的方法
    # 如果有一秒以内的情况,在执行前加上time.sleep(1)



