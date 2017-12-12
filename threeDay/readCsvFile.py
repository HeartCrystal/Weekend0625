# csv文件是工作最常用的读取配置文件的类型,因为读取简单
import csv
# 引入csv代码库,csv代码库是默认的,python内置的代码库,不需要单独下载
# path = "C:/Users/51Testing/PycharmProjects/WeekDay2/three_day/data/product_info.csv"
# 为了更好的移植性,我们应该采用相对路径
import os  # os 是操作系统的意思

# 在python遇到冒号:下面的语句就退一个table键
# 表示下面的4句话.属于readCsv()这个方法
# phthon 中没有{},所有对格式的要求非常严格
# 比方法声明这一行,后退4个空格的语句就是方法体
def readCsv():
    # _file_是ptthon 内置的变量,代表当前文件(当前代码文件)
    #  ps.path.dirname()可以获得文件路径
    project_path = os.path.dirname(__file__)
    # print(project_path
    path = project_path + "/data/product_info.csv"
    # open() 用于打开文件
    # reader() 用于读取文件的数据,必须先打开,在读取
    # csv.reader(open(path))
    file = open(path) #打开这个文件
    data = csv.reader(file) #读这个文件
    # return 关键字,表示方法的返回值
    return data

# 在main函数表示,这段代码只有在当前页面运行时才会被执行,从其他页面运行时,这部分语句不会被执行.可以用来调试代码,用于测试readCsv()这个方法有没有问题
if __name__ == '__main__':
    # 方法必须调用才能运行
    data = readCsv()
    n = 1
    for row in data:
        print("第" + str(n) + "行数据")
        print(row[0])  #第一列数据
        print(row[1])  # 第二列数据
        n=n+1