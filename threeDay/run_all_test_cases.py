# 这个文件用于运行所有的测试用例
import unittest

if __name__ == '__main__':
    # default 默认的,test 测试,loader 加载器
    # 调用unittest这个框架为我们提供用例加载器
    # 加载器可以为我们自动找所有的测试用例
    # discover() 发现,根据规则查找测试用例
    # suite 套件的意思,用来表示一组测试用例
    suite = unittest.defaultTestLoader.discover(".", pattern='*Test.py')
    # 执行测试用例
    # test 文本  Test 测试 runner运行器
    # TextTestRunner 运行测试用例的类
    # 为了调用类中的方法,首先需要实例化这个类(加上一个括号)
    # run() 运行测试用例里的方法,suite 表示所有的测试用例
    unittest.TextTestRunner().run(suite)
    # 这样,所有继承了unittest.TestCase的类都可以通过这种方法运行